#!/usr/bin/env python3
"""Validate the Overdeliver corpus and regenerate its audit metadata."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
METADATA = {"REPOSITORY_MANIFEST.json", "FINAL_VALIDATION.json"}
REQUIRED_VENDOR_FIELDS = {
    "name", "category", "official_url", "official_evidence",
    "not_proven", "fit", "confidence", "status", "notes",
}
REQUIRED_SOURCE_FIELDS = {
    "source_id", "url", "source_type", "evidence_observed", "verification_status",
    "official_or_regulator", "local_artifact", "notes",
}
SECRET_PATTERNS = [
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{24,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def read_csv(name: str) -> tuple[list[dict[str, str]], list[str]]:
    with (ROOT / name).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def repository_paths() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return sorted(
        (ROOT / line for line in result.stdout.splitlines() if line and line not in METADATA),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def malformed(rows: list[dict[str, str]], required: set[str]) -> list[int]:
    return [
        index
        for index, row in enumerate(rows, start=2)
        if not required.issubset(row) or any(not (row.get(field) or "").strip() for field in required)
    ]


def main() -> None:
    vendors, vendor_fields = read_csv("VENDOR_DIRECTORY.csv")
    sources, source_fields = read_csv("SOURCE_LEDGER.csv")
    url_results = json.loads((ROOT / "URL_VERIFICATION.json").read_text(encoding="utf-8"))

    malformed_vendor_rows = malformed(vendors, REQUIRED_VENDOR_FIELDS)
    malformed_ledger_rows = malformed(sources, REQUIRED_SOURCE_FIELDS)
    missing_raw_artifacts = [
        row["local_artifact"] for row in sources if not (ROOT / row["local_artifact"]).is_file()
    ]
    duplicate_vendor_names = len(vendors) - len({row["name"] for row in vendors})
    duplicate_vendor_urls = len(vendors) - len({row["official_url"] for row in vendors})

    paths = repository_paths()
    manifest = [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in paths
    ]

    redaction_count = 0
    secret_matches: list[str] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if path.name == Path(__file__).name:
            continue
        redaction_count += text.count("[REDACTED_PUBLIC_CAPTURE_TOKEN]")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                secret_matches.append(f"{path.relative_to(ROOT)}:{pattern.pattern}")

    browser_verified_directory_rows = sum(
        row["status"] == "current_browser_verified" for row in vendors
    )
    integrity_pass = not any(
        (
            malformed_vendor_rows,
            malformed_ledger_rows,
            missing_raw_artifacts,
            duplicate_vendor_names,
            duplicate_vendor_urls,
            secret_matches,
        )
    )
    summary = {
        "vendor_records": len(vendors),
        "source_records": len(sources),
        "unique_vendor_names": len({row["name"] for row in vendors}),
        "unique_vendor_urls": len({row["official_url"] for row in vendors}),
        "http_200": url_results["http_200_count"],
        "http_403": url_results["http_403_count"],
        "browser_verified": url_results["browser_verified_count"],
        "browser_verified_directory_rows": browser_verified_directory_rows,
        "missing_raw_artifacts": len(missing_raw_artifacts),
        "malformed_vendor_rows": len(malformed_vendor_rows),
        "malformed_ledger_rows": len(malformed_ledger_rows),
        "duplicate_vendor_names": duplicate_vendor_names,
        "duplicate_vendor_urls": duplicate_vendor_urls,
        "published_file_count": len(manifest) + len(METADATA),
        "content_file_count": len(manifest),
        "public_capture_redaction_placeholders": redaction_count,
        "integrity_pass": integrity_pass,
        "secret_scan": "no unredacted credential-pattern matches" if not secret_matches else secret_matches,
    }

    validation = {
        "summary": summary,
        "missing_raw_artifacts": missing_raw_artifacts,
        "malformed_vendor_rows": malformed_vendor_rows,
        "malformed_ledger_rows": malformed_ledger_rows,
        "manifest": manifest,
        "metadata_files_excluded_from_manifest": sorted(METADATA),
    }
    repository_manifest = {
        "validation": {
            "summary": summary,
            "missing_raw_artifacts": missing_raw_artifacts,
            "malformed_rows": {
                "vendor": malformed_vendor_rows,
                "source_ledger": malformed_ledger_rows,
            },
        },
        "file_count": len(manifest) + len(METADATA),
        "content_file_count": len(manifest),
        "metadata_files_excluded_from_hash_map": sorted(METADATA),
        "sha256": {entry["path"]: entry["sha256"] for entry in manifest},
    }

    (ROOT / "FINAL_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (ROOT / "REPOSITORY_MANIFEST.json").write_text(
        json.dumps(repository_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))
    if not integrity_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

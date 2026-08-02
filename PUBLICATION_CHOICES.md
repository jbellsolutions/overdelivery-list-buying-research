# Publication Choices and Verification Record

## What was published

This repository is published as a public, source-grounded research explorer under the name **Overdeliver**.

- **GitHub repository:** https://github.com/jbellsolutions/overdelivery-list-buying-research
- **Visibility:** Public
- **Default branch:** `main`
- **Repository entry point:** `index.html`
- **Business-process entry point:** `BUSINESS_PROCESS.md`
- **Web snapshot:** This same directory is published as a static here.now site so the report can be read without cloning the repository.
- **Live here.now site:** https://arctic-signal-9v2e.here.now/

## Why these choices

1. **Public GitHub repository:** The deliverable is a research corpus, not an application containing credentials or private customer data. Public visibility makes the CSVs, evidence files, verification records, and operating guide inspectable and forkable.
2. **`main` as the default branch:** This keeps the repository immediately readable for a non-technical reviewer and matches GitHub's standard default-branch behavior.
3. **Static HTML as the web entry point:** `index.html` renders the complete 98-record provider directory and 112-record source ledger with search and filters, plus the process, diligence controls, verification limits, and direct links into the full Markdown, CSV, JSON, and raw-capture corpus.
4. **Full evidence corpus retained:** The repository includes the agent research, source ledger, vendor directory, raw official captures, URL verification, and validation artifacts instead of presenting only a polished summary.
5. **Raw capture safety redactions:** A small number of retrieved pages contained client-side analytics, tracking, or public-page integration tokens. Those literal values were replaced with `[REDACTED_PUBLIC_CAPTURE_TOKEN]` before publication. The surrounding evidence and source context remain intact; the tokens are not part of the research conclusion.
6. **Authenticated here.now publication:** The local here.now credentials were present, so the permanent authenticated publish path was selected instead of an anonymous 24-hour site. The site is published from the repository root, where `index.html` is at the site root.
7. **No anonymous claim workflow:** Because the authenticated path is used, no temporary claim URL is required. The live site URL returned by the publish operation is the source of truth.

## Corpus and audit facts

- 98 normalized vendor/provider records
- 112 source-ledger records
- 92 official URLs returned HTTP 200
- 6 Industry Dive advertising pages were marked for manual/browser recheck after HTTP 403 responses
- 0 other URL failures
- 0 malformed CSV rows
- 0 duplicate vendor names
- 0 duplicate vendor URLs
- Raw official captures and agent research are retained for provenance

## Verification contract

The publication is considered complete only when all of the following are true:

- GitHub reports the repository as public and the `main` branch contains the committed corpus.
- The GitHub tree includes `README.md`, `index.html`, both CSVs, the validation JSON, `PUBLICATION_CHOICES.md`, `AGENT_RESEARCH/`, and `RAW_OFFICIAL_FETCHES/`.
- The here.now URL returns HTTP 200 and renders the title **Overdeliver**.
- The web explorer renders all 98 provider records and all 112 source-ledger records without requiring a download.
- The web snapshot exposes working relative links to the principal deliverables and retained source captures.
- No credential file, local `.herenow` state, `.env` file, private key, GitHub token, or unredacted integration token is committed.

## Scope boundary

This is an evidence-backed operating guide and research repository, not legal advice and not a guarantee that any listed provider's current terms, consent basis, pricing, or inventory remain unchanged. Confirm current media kits, sender responsibility, suppression, offer clearance, and applicable law before buying or deploying media.

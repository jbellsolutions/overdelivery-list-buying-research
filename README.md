# Over Delivery List-Buying Repository

Research repository for building direct-response list intelligence and buying media in the Brian Kurtz / *Over Delivery* tradition.

## What this repository contains

- `ULTIMATE_GUIDE.md` — operating framework, channel map, buying process, and recommended starting lanes.
- `VENDOR_DIRECTORY.csv` — normalized vendor/provider records with provenance and confidence.
- `SOURCE_LEDGER.csv` — source URLs, evidence type, retrieval/verification notes, and coverage.
- `BUYER_DUE_DILIGENCE.md` — questions and controls before paying for a list, solo, or email placement.
- `AGENT_RESEARCH/` — raw/near-raw research returned by the 10 independent research agents.
- `LOCAL_ARCHIVE_SOURCE_MAP.md` — what the attached Brian Kurtz / Over Delivery archive contributes, including file paths and historical caveats.
- `PUBLICATION_CHOICES.md` — the publication decisions, safety redactions, live-link verification contract, and scope limits.

## Core distinction

This is not a list of “email tools.” It separates:

1. **List owners / publishers** — own the audience and control inventory.
2. **List brokers / managers** — represent multiple owners and clear offers.
3. **Solo-ad providers / email-media brokers** — sell a dedicated send or email placement.
4. **Newsletter sponsorship marketplaces** — broker sponsored placements across publishers.
5. **Affiliate networks / management firms** — connect offers and publishers, but are not automatically media inventory.
6. **Tracking / compliance infrastructure** — measurement and permission controls, not audience access.

## Evidence standard

A provider is not “reputable” because a directory or sales page says so. A high-confidence record should have:

- a current official page or media kit;
- a clear description of what is actually sold;
- evidence of audience ownership, publisher representation, or network role;
- current buying mechanics and contact path;
- permission/terms language where available;
- corroboration or a clearly labeled uncertainty when claims are not independently verifiable.

Historical names from the archive are preserved as **historical context**, not silently promoted to current providers.

## Kurtz decision lens

The guide uses these archive-derived tests:

- Does the audience have demonstrated buyer/subscriber behavior, not merely reach?
- Is the offer congruent with the audience and the publisher’s relationship?
- What did the source actually test, and what did it learn?
- What happens to complaints, unsubscribes, refunds, and partner trust?
- Is the provider selling a real audience relationship, or only traffic claims?

## Execution and provider readiness

The required five-round council classified this as broad, authenticated/current web research with a structured synthesis deliverable. It compared hosted browser, search/discovery, raw HTTP, and local/file lanes; selected hosted browser orchestration for discovery and verification; and required URL provenance, deduplication, and source-level confidence as the verification contract. Hosted cloud providers were not ready in this run; the council/readiness gate selected local Super Browser Playwright for the bounded six-page manual recheck. The fallback was narrow official-page HTTP verification plus browser evidence and the local archive, not silent invention.


The Super Browser council completed five review rounds before execution. Hosted cloud alternatives remained unavailable or unverified, while local Playwright passed the readiness gate for this bounded public-page check. The live-source pass contains **112 source-ledger records and 98 normalized provider/discovery records**. The original direct HTTP pass returned **92 HTTP 200 results and 6 HTTP 403 results**; the six 403 pages now have separate high-confidence browser captures and remain transparently marked as direct-HTTP 403 in `URL_VERIFICATION.json`. The public-release decisions and safety redactions are recorded in `PUBLICATION_CHOICES.md`. Raw captures, browser evidence, agent reports, and URL verification results are retained under `RAW_OFFICIAL_FETCHES/`, `AGENT_RESEARCH/`, and `URL_VERIFICATION.json`. Both ten-agent research batches returned usable outputs. Exact publisher formats, pricing, consent/provenance, and list-transfer rights still require current media-kit and terms review.

# Ten-Agent Status — Final

Batch: `deleg_3520614a`

## Completed and merged

1. Classic direct-response list brokerage/list-rental ecosystem — full summary preserved; current candidates merged.
2. Major list brokers/list-management firms — report preserved as `02_list_brokerage_market_map.md`; candidates and risks merged.
3. Solo-ad marketplaces/providers — full summary preserved; marketplace, broker, directory, and lead-network distinctions merged.
5. Affiliate networks and affiliate-management companies — report preserved as `05_affiliate_network_research.md`; current network/agency/software distinctions merged.
8. Trade associations, conferences, directories, and communities — full summary preserved; discovery infrastructure merged.
9. Compliance and buyer due diligence — full report preserved; practical compliance evidence merged into the buyer materials.
10. Brian Kurtz / OverDeliver archive analysis — full source map preserved; historical claims and live-validation flags merged.

## Timed out and deliberately not padded

4. Newsletter sponsorship/email advertising platforms — timed out after 8 API calls.
6. Specialist email media-buying/performance-email agencies — timed out after 9 API calls.
7. Publisher-side rentable email audiences — timed out after 10 API calls.

These lanes were subsequently covered by the second delegation batch `deleg_2d3d68eb`; they are no longer open research gaps. The second batch returned publisher-owned newsletter/media candidates, newsletter marketplaces, additional affiliate/platform checks, compliance research, discovery channels, and a skeptical verification pass.

## Second batch — `deleg_2d3d68eb`

All ten lanes completed and were merged:

1. Consumer direct-mail brokers/list managers.
2. Newsletter sponsorship/email marketplaces.
3. Solo-ad marketplaces and sellers.
4. Affiliate networks/performance partnerships.
5. List brokers and media-planning databases.
6. B2B/professional newsletter publishers.
7. Consumer, finance, and enthusiast publishers.
8. U.S./UK/EU compliance and due diligence.
9. Media-buying communities and discovery channels.
10. Skeptical verification/editor pass.

The six Industry Dive advertising pages that returned HTTP 403 to direct automated retrieval were subsequently rechecked in bounded Super Browser Playwright runs. Browser text captures, screenshots, and run reports are retained; the directory now labels them `current_browser_verified` while preserving the original direct-HTTP 403 results separately.

## Merge controls

Every promoted candidate was deduplicated by organization/official URL and directly re-checked against its official URL. New live captures are stored under `RAW_OFFICIAL_FETCHES/`. Current rows carry explicit `not_proven`, `confidence`, and `status` fields. Agent assertions that were marketing claims, stale, redirected, gated, or unverified remain labeled as such.

# Provider Scoring Rubric

This repository does not rank providers by advertised reach alone.

## Evidence score

- **A / high:** current official page clearly states role and mechanics; terms/media kit or operational page is available; no key claim is inferred.
- **B / medium:** current official page supports a useful role but audience ownership, inventory, or permission is not fully exposed.
- **C / low:** directory/profile/testimonial or thin homepage evidence only.
- **H / historical:** valuable archive or historical evidence, but current availability not verified.

## Buying-fit score

- **5:** directly exposes audience inventory and source/selection/reporting controls.
- **4:** strong marketplace or publisher-discovery layer with clear buying mechanics.
- **3:** partner/network layer that can produce media access only after partner-level clearance.
- **2:** data/modeling/hygiene or infrastructure that supports buying but is not media inventory.
- **1:** historical, opaque, or insufficiently evidenced.

## Risk flags

- `permission_unknown`
- `owner_not_clear`
- `performance_claim_unverified`
- `marketplace_seller_variance`
- `publisher_description_not_guarantee`
- `data_file_not_send_permission`
- `network_not_inventory`
- `pricing_not_public`
- `terms_needs_current_review`

## Required record fields

`name, category, official_url, channel, role, audience_type, buying_mechanic, evidence_url, what_is_verified, what_is_not_proven, fit_score, evidence_grade, risk_flags, current_status, last_checked, notes`

A provider may be high-confidence as a **discovery platform** and low-confidence as a **list-quality recommendation**. Those are intentionally separate judgments.

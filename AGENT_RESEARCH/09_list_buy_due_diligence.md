# Buyer Due Diligence for List Rental, Solo Ads, and Email Media Buys

**Scope:** operational controls for buyers of rented-list placements, solo ads, and affiliate email promotion. Not legal advice; applicability varies by recipient location, sender/advertiser roles, sector, and contract structure.

## Executive rule

Treat a list seller's statement that a list is “opt-in” as a lead, not proof. Do not launch until the seller can identify the collection source, consent language, parties/brands covered, channel, timestamp, and suppression process. A buyer can remain responsible even when another party sends the email.

## Pre-buy checklist

### 1. Seller and inventory diligence
- Identify the legal entity, trading names, domains, sending infrastructure, list owner, broker, and actual sender/ESP.
- Obtain the exact audience description: geography, B2C/B2B, sole traders, age/sector restrictions, source URLs/forms, collection dates, and last-activity date.
- Require a sample of the actual signup form and privacy notice in force when each cohort was collected.
- Reject “scraped,” harvested, guessed, publicly available, purchased, co-registration, or “partner” data unless counsel has specifically validated the use and the relevant consent/notice chain.
- Ask for cohort-level consent evidence: date/time, form version, wording, checkbox state, source URL, IP/device or equivalent audit data, and confirmation/double-opt-in event where used.
- Confirm whether consent names the buyer/advertiser, a defined category of partners, or only the seller. Generic “third parties” language is not a safe basis for a list rental.
- Verify promised frequency, subject matter, and channel match the proposed offer; a weekly editorial opt-in is not automatically consent for a daily affiliate offer.
- Request recent delivery, hard/soft bounce, complaint, unsubscribe, and engagement statistics by mailbox provider and by source cohort; investigate unexplained spikes and suppress risky cohorts.

### 2. Legal and role allocation
- Map each party: advertiser/product owner, list owner, sender/initiator, ESP, affiliate, broker, and any data processor/service provider.
- Decide which law applies by recipient location before launch. U.S. CAN-SPAM is baseline but does not replace state, sector, or foreign rules. UK PECR and EU ePrivacy/GDPR rules can require consent and are often stricter.
- For EU/UK audiences, document the lawful basis and the direct-marketing channel rule separately. Do not treat a privacy-policy mention or pre-ticked box as affirmative consent.
- For California residents, map whether the transaction is a sale/share of personal information and how opt-out/GPC requests flow through the list owner, buyer, and sender.
- Screen the offer itself: health, finance, credit, employment, crypto, gambling, supplements, and money-making claims may create additional advertising, platform, or sector restrictions.

### 3. Suppression and unsubscribe controls
- Require a shared, near-real-time suppression process covering: global unsubscribe, campaign/brand unsubscribe, hard bounce, complaint, legal objection, do-not-contact, and invalid address.
- Put suppression ownership and SLA in writing. A buyer must be able to stop a recipient from every future send by the buyer, seller, affiliate, and downstream sender, not only from one campaign.
- Process one-click List-Unsubscribe headers and body links; do not require login, survey completion, or extra personal data.
- Confirm suppression lists are protected, deduplicated, versioned, and checked immediately before every deployment.
- Retain evidence: request timestamp, source, recipient identifier/hash, propagation log, and confirmation of removal.
- Maintain a small “suppression-only” record where necessary to prevent re-mailing; do not delete suppression data in a way that causes re-addition.

### 4. Campaign and tracking controls
- Use accurate From/Reply-To identity, truthful subject line, advertiser identity, physical postal address, and clear ad/affiliate disclosure where required.
- Keep tracking parameters limited to what is necessary; document pixels, click IDs, device identifiers, and sharing with affiliates/analytics vendors in the privacy notice and data map.
- Do not use deceptive display names, fake replies/forwards, hidden links, or misleading landing-page redirects.
- Use authenticated sending domains (SPF, DKIM, DMARC); segregate promotional traffic from transactional mail where possible.
- Record the exact creative, landing page, offer terms, disclosure, sender, list/cohort, send time, suppression snapshot, and tracking configuration for each drop.

### 5. Launch and stop rules
- Run a seed test and small cohort first; compare complaint, hard-bounce, soft-bounce, deferral, unsubscribe, and conversion quality against the seller's historical baseline.
- Pause the campaign and investigate on material deviation, especially complaints, authentication failures, sudden invalids, or evidence that consent does not cover the offer.
- Treat platform figures as deliverability gates, not legal safe harbors: Google says keep Postmaster spam rate below 0.10% and avoid 0.30% or higher; Yahoo requires bulk senders to keep spam below 0.3% and honor unsubscribes within 2 days.
- There is no universal legal “acceptable bounce rate.” Contract a hard-bounce ceiling and remediation/pause rule based on the mailbox mix and verified baseline; require prompt removal of invalid recipients. Do not use a vendor's open-rate claim as proof of permission or deliverability.
- Monitor complaint/bounce rates by source cohort and affiliate, not only in aggregate; one bad source can be hidden by a large clean list.

## Minimum contract clauses

1. **Definitions and roles:** identify advertiser, initiator/sender, list owner, affiliate, ESP, processor, and jurisdictions.
2. **Permission representation:** seller represents that every address was lawfully collected for the stated channel and purpose; no harvesting, scraping, purchased/rented third-party upload, deceptive co-registration, or pre-checked consent unless expressly approved in writing.
3. **Consent specificity:** seller warrants that consent covers the buyer/advertiser or an adequately specific partner category, the email channel, the expected frequency, and the relevant offer category; attach the form, notice, and version history.
4. **Evidence and audit:** seller must retain and produce cohort-level consent, source, timestamp, form text, IP/equivalent, confirmation, transfer disclosures, and suppression records; buyer may audit or request regulator/platform response materials.
5. **Data-use limits:** no reuse, resale, enrichment, onward transfer, cross-campaign use, or retargeting beyond the agreed purpose; define controller/processor or independent-controller responsibilities and deletion/return mechanics.
6. **Compliance warranty:** comply with CAN-SPAM, applicable state law including California privacy rights, UK PECR/UK GDPR, EU GDPR/ePrivacy rules, advertising/affiliate disclosures, and applicable sector rules; flow obligations to subcontractors and affiliates.
7. **Sender/creative approval:** buyer approves From identity, subject, body, landing page, claims, disclosures, tracking, and frequency before launch; no substitutions without written approval.
8. **Unsubscribe and suppression SLA:** immediate intake; operational propagation within a defined short SLA; at minimum meet applicable law/platform requirements; global buyer suppression must override seller campaign lists.
9. **Metrics and access:** timely delivery and provider-level reporting for sent, delivered, hard/soft bounce, complaint, unsubscribe, deferral, authentication, and source cohort; permit raw event exports where needed.
10. **Stop/kill rights:** buyer may pause immediately for complaints, bounces, spam-folder/reputation damage, legal concern, missing evidence, or platform warning; seller must stop the affected source and preserve evidence.
11. **Incident notice and cooperation:** prompt notice of complaints, regulator inquiries, data incidents, suppression failures, ESP suspension, or provider blocklisting; cooperation with investigations and remediation.
12. **Indemnity and remedies:** indemnity for seller/affiliate breach, invalid consent, unlawful data transfer, suppression failure, deceptive claims, and third-party/platform penalties to the extent legally permitted; refund/credit and termination rights.
13. **No guarantee / allocation:** performance, delivery, and conversions are not permission evidence; seller must not represent that a platform or regulator has “approved” the list.

## Source-backed requirements and guidance

- **FTC CAN-SPAM guide:** commercial email includes email promoting commercial products/services; no B2B exception; truthful headers/subjects, ad identification, postal address, clear opt-out, honor opt-outs within 10 business days, and do not sell/transfer opted-out addresses except for compliance support. Both promoted business and sending company may be liable; hiring a sender does not contract away responsibility. The guide also says paid referral/forwarding arrangements can create compliance obligations.  
  https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- **ICO PECR electronic/telephone marketing:** electronic marketing generally requires clear, specific, affirmative consent where consent is required; pre-ticked boxes are invalid; keep records; indirect consent must specifically identify the organization; withdrawal must be easy; both the instigator and contractor can be responsible, and the ICO recommends a written contract plus checks.  
  https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/
- **EU GDPR Regulation (official EUR-Lex):** Article 7 requires demonstrable consent, distinguishable/plain-language requests, and withdrawal as easy as giving consent; Article 21 gives an unconditional objection right for direct marketing and requires stopping that processing; Article 13 requires notice of controller, purposes/legal basis, recipients, retention, and related information.  
  https://eur-lex.europa.eu/eli/reg/2016/679/oj
- **California Attorney General CCPA FAQ:** California consumers can opt out of sale/sharing; email address is personal information; businesses/data brokers have notice and response duties; the AG FAQ states opt-out requests must be handled as soon as feasible, up to 15 business days, and cannot require account creation.  
  https://oag.ca.gov/privacy/ccpa
- **Google Gmail sender guidelines:** require authentication (SPF/DKIM; bulk senders SPF, DKIM, DMARC), easy unsubscribe, and one-click unsubscribe for marketing/subscribed messages over 5,000/day; advise against purchased addresses and mailing people who did not sign up; recommend removing repeated bounces; affiliate spam can damage the brand; keep Postmaster spam rate below 0.10% and avoid 0.30% or higher.  
  https://support.google.com/mail/answer/81126
- **Yahoo Sender Best Practices:** all senders must authenticate and keep spam below 0.3%; bulk senders must use SPF/DKIM/DMARC, functioning one-click unsubscribe, visible body unsubscribe, and honor unsubscribes within 2 days; Yahoo says do not purchase lists, monitor hard/soft bounces, remove invalid recipients promptly, use complaint feedback loops, and monitor affiliates.  
  https://senders.yahooinc.com/best-practices/
- **Mailchimp Acceptable Use Policy (reputable ESP policy):** requires evidence of opt-in/consent, prohibits external unsubscribe processes, prohibits purchased/rented/third-party/co-reg/public/partner lists, and lists affiliate marketing and list brokers/rental as disallowed or restricted categories. This is a provider policy, not a statement of law, but it is a useful buyer screening signal.  
  https://mailchimp.com/legal/acceptable_use/
- **FTC Endorsements/Influencers hub:** use for affiliate/endorser disclosure and material-connection review; disclosure obligations are separate from email permission and CAN-SPAM.  
  https://www.ftc.gov/business-guidance/advertising-marketing/endorsements-influencers-reviews

## Jurisdiction notes

- CAN-SPAM is an important U.S. federal baseline, but state privacy/consumer-protection laws and sector rules may add duties. It generally does not require prior opt-in, but platforms and many non-U.S. laws do.
- EU/UK analysis is not interchangeable: GDPR governs personal-data processing and objection/notice; PECR/ePrivacy governs electronic marketing mechanics. UK and EU member-state rules can differ and may be stricter for B2B or specific channels.
- CCPA/CPRA sale/share opt-outs concern personal-information transfers and are distinct from email unsubscribe. A recipient can require both: stop marketing and stop sale/share/use of their data.
- Platform policies (Google, Yahoo, Mailchimp) can block or throttle mail even when a sender believes it is legally compliant; contract for platform-safe practices and evidence, not merely statutory compliance.

#!/usr/bin/env python3
"""Build the single-page Overdeliver research explorer from the verified corpus."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def lane_for(category: str) -> str:
    value = category.strip().lower()
    rules = (
        ("Solo ads & dedicated sends", ("solo-ad", "solo ad", "traffic broker", "managed traffic", "lead distribution")),
        ("Affiliate & performance", ("affiliate", "performance", "partnership", "partner ecosystem", "partner marketing", "creator partnership", "influencer")),
        ("Discovery, associations & events", ("association", "conference", "event", "community", "directory", "discovery", "trade association")),
        ("Postal, brokers & direct mail", ("list brokerage", "list management", "list compiler", "mailing list", "direct mail", "postal", "list supplier", "media planning", "managed media/acquisition")),
        ("Data, modeling & hygiene", ("data", "identity", "audience", "model", "property", "hygiene", "prospect list")),
        ("Publisher & newsletter media", ("publisher", "newsletter", "sponsorship", "email advertising", "email monetization", "media/marketing")),
        ("Infrastructure & controls", ("tracking", "compliance", "referral platform", "software", "infrastructure")),
    )
    for lane, terms in rules:
        if any(term in value for term in terms):
            return lane
    raise ValueError(f"Unclassified vendor category: {category}")


def compact_json(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


vendors = read_csv("VENDOR_DIRECTORY.csv")
sources = read_csv("SOURCE_LEDGER.csv")
for vendor in vendors:
    vendor["lane"] = lane_for(vendor["category"])

validation = json.loads((ROOT / "FINAL_VALIDATION.json").read_text(encoding="utf-8"))["summary"]

html = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Overdeliver is an evidence-backed directory, source ledger, and operating system for buying audience access without buying blind.">
<title>Overdeliver — Audience Access Research</title>
<style>
:root{--ink:#191714;--muted:#6d675e;--paper:#f5f1e9;--surface:#fffdf8;--surface-2:#ebe5da;--line:#d8d0c3;--amber:#c87908;--amber-dark:#855006;--green:#25634b;--red:#9d3e35;--dark:#211e19;--shadow:0 14px 40px rgba(42,35,24,.08);--radius:14px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.55 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}button,input,select{font:inherit}button,a{transition:color .16s ease,background .16s ease,border-color .16s ease,transform .16s ease}a{color:var(--amber-dark)}a:hover{color:#5e3600}.shell{max-width:1440px;margin:auto;padding:0 28px}.masthead{position:sticky;top:0;z-index:20;background:rgba(245,241,233,.96);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}.masthead-inner{min-height:70px;display:flex;align-items:center;justify-content:space-between;gap:24px}.brand{display:flex;align-items:baseline;gap:11px;text-decoration:none;color:var(--ink)}.brand strong{font:800 25px/1 Georgia,serif;letter-spacing:-.025em}.brand span{font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--muted);font-weight:800}.nav{display:flex;gap:4px;overflow-x:auto;padding:8px 0}.nav a{white-space:nowrap;text-decoration:none;color:var(--muted);font-weight:750;font-size:13px;padding:9px 12px;border-radius:8px}.nav a:hover,.nav a[aria-current="page"]{background:var(--dark);color:#fffaf1}.hero{background:var(--dark);color:#fff9ef;margin:28px auto 0;border-radius:18px;padding:34px 38px;display:grid;grid-template-columns:minmax(0,1.4fr) minmax(260px,.6fr);gap:40px;align-items:end}.eyebrow{color:#f2a936;text-transform:uppercase;letter-spacing:.16em;font-size:11px;font-weight:900}.hero h1{font:800 clamp(43px,7vw,86px)/.92 Georgia,serif;letter-spacing:-.05em;margin:10px 0 18px}.hero .lede{max-width:800px;color:#e6ded1;font-size:18px;margin:0}.hero-note{border-top:1px solid #514b42;padding-top:18px;color:#cfc4b4;font-size:13px}.hero-note strong{color:#fff8ec}.statline{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px auto 0}.stat{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:15px 17px}.stat strong{display:block;font:800 28px/1 Georgia,serif;color:var(--green)}.stat span{display:block;color:var(--muted);font-size:12px;margin-top:5px}.view{display:none;padding:38px 0 80px}.view.active{display:block}.section-head{display:flex;justify-content:space-between;align-items:end;gap:24px;margin-bottom:18px}.section-head h2{font:800 clamp(30px,4vw,48px)/1 Georgia,serif;letter-spacing:-.025em;margin:0}.section-head p{max-width:680px;color:var(--muted);margin:8px 0 0}.count-badge{flex:none;border:1px solid var(--line);background:var(--surface);border-radius:99px;padding:8px 12px;font-weight:800;font-size:12px}.overview-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:16px}.panel{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:24px}.panel h3{font:800 24px/1.1 Georgia,serif;margin:0 0 13px}.panel p:last-child{margin-bottom:0}.principle{background:#fff0ce;border-color:#e4c17c}.principle strong{display:block;font:800 24px/1.2 Georgia,serif;margin-bottom:8px}.lane-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}.lane{border:1px solid var(--line);border-radius:12px;padding:16px;background:var(--surface)}.lane strong{display:block}.lane small{color:var(--muted)}.process-list{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;counter-reset:stage}.stage{counter-increment:stage;position:relative;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px 18px 18px 58px}.stage:before{content:counter(stage);position:absolute;left:17px;top:17px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:var(--dark);color:white;font-weight:900}.stage h3{margin:0 0 5px;font-size:16px}.stage p{margin:0;color:var(--muted);font-size:13px}.filters{position:sticky;top:70px;z-index:10;background:var(--paper);border-block:1px solid var(--line);padding:12px 0;margin:0 0 16px}.filter-grid{display:grid;grid-template-columns:minmax(220px,1.5fr) repeat(3,minmax(150px,.55fr));gap:8px}.filter-grid.sources{grid-template-columns:minmax(220px,1.5fr) repeat(2,minmax(170px,.55fr))}.field{display:flex;flex-direction:column;gap:4px}.field label{font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);font-weight:900}.field input,.field select{width:100%;height:42px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:8px;padding:0 11px;outline:none}.field input:focus,.field select:focus{border-color:var(--amber);box-shadow:0 0 0 3px rgba(200,121,8,.12)}.data-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.record{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px;min-width:0;overflow:hidden}.record:hover{border-color:#bdb3a4;box-shadow:var(--shadow)}.record-head{display:flex;justify-content:space-between;align-items:start;gap:14px}.record-head>div:first-child{min-width:0}.record h3{font:800 21px/1.15 Georgia,serif;margin:4px 0 6px;overflow-wrap:anywhere}.kicker{font-size:10px;text-transform:uppercase;letter-spacing:.11em;color:var(--amber-dark);font-weight:900;overflow-wrap:anywhere}.record dd{overflow-wrap:anywhere}.tag-row{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}.tag{display:inline-block;border:1px solid var(--line);background:var(--paper);border-radius:99px;padding:4px 7px;font-size:10px;text-transform:uppercase;letter-spacing:.05em;font-weight:850;color:var(--muted)}.tag.high,.tag.verified_fetch,.tag.browser_verified,.tag.current,.tag.current_browser_verified{background:#e7f2ec;border-color:#b9d6c8;color:var(--green)}.tag.medium,.tag.verify-before-use,.tag.blocked_manual_recheck{background:#fff0ce;border-color:#e4c17c;color:#7d4c05}.tag.high-risk{background:#f8e4e0;border-color:#e5b7b0;color:var(--red)}.fit{margin:10px 0;color:#34302a}.record details{border-top:1px solid var(--line);margin-top:13px;padding-top:10px}.record summary{cursor:pointer;font-weight:800;color:var(--amber-dark);list-style:none}.record summary::-webkit-details-marker{display:none}.record summary:after{content:" +"}.record details[open] summary:after{content:" –"}.record dl{margin:13px 0 0}.record dt{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);font-weight:900;margin-top:12px}.record dd{margin:3px 0 0}.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:15px}.button{display:inline-flex;min-height:38px;align-items:center;border:1px solid var(--line);border-radius:8px;padding:7px 10px;text-decoration:none;font-weight:800;font-size:12px;background:var(--surface)}.button.primary{background:var(--dark);border-color:var(--dark);color:white}.button:hover{transform:translateY(-1px)}.empty{grid-column:1/-1;background:var(--surface);border:1px dashed var(--line);border-radius:12px;padding:48px;text-align:center;color:var(--muted)}.check-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.checklist{margin:0;padding-left:20px}.checklist li{margin:8px 0}.decision-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.decision{border-top:4px solid var(--line)}.decision.stop{border-color:var(--red)}.decision.refine{border-color:var(--amber)}.decision.scale{border-color:var(--green)}.resource-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.resource{display:block;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px;text-decoration:none;color:var(--ink)}.resource strong{display:block}.resource span{display:block;color:var(--muted);font-size:12px;margin-top:4px}.resource:hover{border-color:var(--amber);color:var(--ink)}.fine{font-size:12px;color:var(--muted)}.footer{border-top:1px solid var(--line);padding:22px 0 50px;color:var(--muted);font-size:12px}.footer strong{color:var(--ink)}
@media(max-width:980px){.hero{grid-template-columns:1fr}.hero-note{max-width:700px}.overview-grid{grid-template-columns:1fr}.data-list{grid-template-columns:1fr}.resource-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:720px){.shell{padding:0 14px}.masthead-inner{align-items:flex-start;flex-direction:column;gap:4px;padding:12px 0 5px}.masthead{position:static}.brand span{display:none}.nav{width:100%}.hero{margin-top:14px;padding:27px 22px;gap:24px}.statline{grid-template-columns:repeat(2,1fr)}.view{padding-top:28px}.section-head{align-items:start;flex-direction:column}.filters{position:static}.filter-grid,.filter-grid.sources{grid-template-columns:1fr}.lane-grid,.process-list,.check-grid,.decision-grid,.resource-grid{grid-template-columns:1fr}.record-head{flex-direction:column}.tag-row{justify-content:flex-start}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;transition:none!important}}
</style>
</head>
<body>
<header class="masthead">
  <div class="shell masthead-inner">
    <a class="brand" href="#overview"><strong>Overdeliver</strong><span>Audience access research</span></a>
    <nav class="nav" aria-label="Primary">
      <a href="#overview" data-route="overview">Overview</a>
      <a href="#vendors" data-route="vendors">Providers <span aria-hidden="true">(98)</span></a>
      <a href="#sources" data-route="sources">Source ledger <span aria-hidden="true">(112)</span></a>
      <a href="#process" data-route="process">Process</a>
      <a href="#diligence" data-route="diligence">Diligence</a>
      <a href="#method" data-route="method">Method & files</a>
    </nav>
  </div>
</header>
<main class="shell">
  <section class="hero" aria-labelledby="hero-title">
    <div><div class="eyebrow">Evidence before enthusiasm</div><h1 id="hero-title">Overdeliver</h1><p class="lede">A complete, searchable operating system for finding audience access, checking the evidence, running controlled tests, and turning rented reach into an owned audience.</p></div>
    <div class="hero-note"><strong>Operating standard</strong><br>Buy access, not databases. Test placements, not promises. Capture the response. Build the house file.</div>
  </section>
  <div class="statline" aria-label="Corpus summary">
    <div class="stat"><strong>__VENDOR_COUNT__</strong><span>providers rendered on this site</span></div>
    <div class="stat"><strong>__SOURCE_COUNT__</strong><span>source-ledger records rendered</span></div>
    <div class="stat"><strong>__HTTP_COUNT__</strong><span>official URLs returned HTTP 200</span></div>
    <div class="stat"><strong>10</strong><span>gated operating stages</span></div>
  </div>

  <section class="view" id="overview" data-view="overview">
    <div class="section-head"><div><h2>The complete research, in one place</h2><p>The original publication hid the evidence behind CSV downloads. Overdeliver renders every provider and every source directly on the site, while preserving the raw files for audit.</p></div><span class="count-badge">No samples · no truncation</span></div>
    <div class="overview-grid">
      <article class="panel principle"><strong>The acquisition model</strong><p>Controlled access to relevant audiences, measured response, first-party capture, and disciplined compounding—not buying a database and blasting it.</p></article>
      <article class="panel"><h3>What is actually here</h3><p><strong>98 provider records</strong> covering publishers, brokers, marketplaces, performance channels, data vendors, associations, and infrastructure.</p><p><strong>112 evidence records</strong> linking the claims to official pages, regulator guidance, terms, pricing, and retained captures.</p></article>
    </div>
    <div class="section-head" style="margin-top:34px"><div><h2>Six operating lanes</h2><p>The raw categories remain intact. These lanes make the market navigable without pretending the products are interchangeable.</p></div></div>
    <div class="lane-grid" id="lane-summary"></div>
  </section>

  <section class="view" id="vendors" data-view="vendors">
    <div class="section-head"><div><h2>All 98 providers</h2><p>Search the full directory. Open any record to see the official evidence, what remains unproven, fit, status, and source notes.</p></div><span class="count-badge" id="vendor-count">98 of 98 shown</span></div>
    <div class="filters"><div class="filter-grid">
      <div class="field"><label for="vendor-search">Search</label><input id="vendor-search" type="search" placeholder="Name, category, evidence, fit…"></div>
      <div class="field"><label for="vendor-lane">Operating lane</label><select id="vendor-lane"><option value="">All lanes</option></select></div>
      <div class="field"><label for="vendor-confidence">Confidence</label><select id="vendor-confidence"><option value="">All confidence levels</option></select></div>
      <div class="field"><label for="vendor-status">Status</label><select id="vendor-status"><option value="">All statuses</option></select></div>
    </div></div>
    <div class="data-list" id="vendor-list" aria-live="polite"></div>
  </section>

  <section class="view" id="sources" data-view="sources">
    <div class="section-head"><div><h2>All 112 source-ledger records</h2><p>Every evidence URL, observation, verification state, note, and retained local capture is available here.</p></div><span class="count-badge" id="source-count">112 of 112 shown</span></div>
    <div class="filters"><div class="filter-grid sources">
      <div class="field"><label for="source-search">Search</label><input id="source-search" type="search" placeholder="ID, URL, evidence, notes…"></div>
      <div class="field"><label for="source-type">Source type</label><select id="source-type"><option value="">All source types</option></select></div>
      <div class="field"><label for="source-status">Verification</label><select id="source-status"><option value="">All verification states</option></select></div>
    </div></div>
    <div class="data-list" id="source-list" aria-live="polite"></div>
  </section>

  <section class="view" id="process" data-view="process">
    <div class="section-head"><div><h2>The ten-gate process</h2><p>No stage gets skipped because a seller is familiar, a platform is large, or a page says “opt-in.”</p></div></div>
    <div class="process-list">
      <article class="stage"><h3>Strategy brief</h3><p>Define product, audience, margin, geography, success event, budget, and first-party capture.</p></article>
      <article class="stage"><h3>Category selection</h3><p>Choose the access lane that sells the product the campaign actually needs.</p></article>
      <article class="stage"><h3>Source universe</h3><p>Assemble candidates with official URLs and source-level provenance.</p></article>
      <article class="stage"><h3>Vendor qualification</h3><p>Score audience truth, congruence, permission clarity, testability, reporting, and operating fit.</p></article>
      <article class="stage"><h3>Compliance clearance</h3><p>Document consent or lawful basis, roles, sender, suppression, data use, and jurisdiction.</p></article>
      <article class="stage"><h3>Test design</h3><p>Fix budget, volume, creative, landing page, source ID, attribution, and stop thresholds.</p></article>
      <article class="stage"><h3>Launch control</h3><p>Run seed and QA checks, preserve suppression state, and monitor delivery and reputation.</p></article>
      <article class="stage"><h3>Measurement</h3><p>Reconcile delivery, complaints, leads, sales, refunds, quality, and contribution.</p></article>
      <article class="stage"><h3>Scale or stop</h3><p>Use source and cohort evidence—not platform size or seller confidence.</p></article>
      <article class="stage"><h3>Owned-audience compounding</h3><p>Route lawful leads, customers, segments, and source learning into the house-file system.</p></article>
    </div>
    <div class="actions"><a class="button primary" href="BUSINESS_PROCESS.md">Read the complete operating packet</a><a class="button" href="FINAL_REPORT.md">Read the narrative report</a></div>
  </section>

  <section class="view" id="diligence" data-view="diligence">
    <div class="section-head"><div><h2>Minimum diligence before paying</h2><p>A provider’s ability to send, track, or supply a record does not prove that the audience can receive a particular offer.</p></div></div>
    <div class="check-grid">
      <article class="panel"><h3>Identify the product</h3><ul class="checklist"><li>Name the owner, broker, sender, ESP, advertiser, affiliate, and processor.</li><li>Classify what is sold: placement, dedicated send, postal access, data file, lead generation, or partner traffic.</li><li>Classify the audience: buyer, paid subscriber, free registrant, lead, clicker, modeled record, or unknown.</li><li>Separate media access from record transfer and from tracking infrastructure.</li></ul></article>
      <article class="panel"><h3>Demand the evidence</h3><ul class="checklist"><li>Collection source, signup form, privacy notice, exact wording, dates, channel, geography, and named sender or category.</li><li>Suppression intake, propagation, logs, and a permanent do-not-contact record.</li><li>Recent delivery, bounce, complaint, unsubscribe, conversion, refund, and invalid-lead reporting.</li><li>Written offer, creative, From identity, subject, disclosure, landing-page, and frequency approval.</li></ul></article>
    </div>
    <div class="decision-grid" style="margin-top:14px">
      <article class="panel decision stop"><h3>Stop</h3><p>Missing provenance, unclear roles, suppression failure, material complaint or fraud deviation, unapproved creative, or missing reporting.</p></article>
      <article class="panel decision refine"><h3>Refine</h3><p>The source is congruent but the offer, creative, landing page, follow-up, or segment is weak.</p></article>
      <article class="panel decision scale"><h3>Scale</h3><p>A repeatable test meets contribution and quality thresholds, controls stay intact, and the next increment has a learning objective.</p></article>
    </div>
    <div class="actions"><a class="button primary" href="BUYER_DUE_DILIGENCE.md">Open the complete checklist</a><a class="button" href="PROVIDER_SCORING_RUBRIC.md">Provider scoring rubric</a></div>
  </section>

  <section class="view" id="method" data-view="method">
    <div class="section-head"><div><h2>Method, limits, and files</h2><p>The polished site does not replace the evidence. It makes the evidence usable while keeping every source and artifact auditable.</p></div></div>
    <div class="overview-grid">
      <article class="panel"><h3>Verification state</h3><p><strong>92 official URLs</strong> returned HTTP 200. Six Industry Dive advertising pages returned HTTP 403 and remain marked for manual or media-kit recheck. No other URL failures, duplicate provider names, duplicate provider URLs, malformed CSV rows, or missing evidence artifacts were found.</p></article>
      <article class="panel"><h3>Scope boundary</h3><p>This is an evidence-backed operating guide, not legal advice or a guarantee of current pricing, inventory, permission, or performance. Recheck the current source before deployment.</p></article>
    </div>
    <div class="section-head" style="margin-top:34px"><div><h2>Full corpus</h2><p>Everything remains inside this same published site.</p></div></div>
    <div class="resource-grid">
      <a class="resource" href="FINAL_REPORT.md"><strong>Final report</strong><span>Executive conclusion and recommendations</span></a>
      <a class="resource" href="BUSINESS_PROCESS.md"><strong>Business process</strong><span>Stages, scorecards, test cards, and cadence</span></a>
      <a class="resource" href="ULTIMATE_GUIDE.md"><strong>Ultimate guide</strong><span>Full market map and operating guide</span></a>
      <a class="resource" href="VENDOR_DIRECTORY.csv"><strong>Provider CSV</strong><span>Raw 98-row directory</span></a>
      <a class="resource" href="SOURCE_LEDGER.csv"><strong>Source ledger CSV</strong><span>Raw 112-row evidence ledger</span></a>
      <a class="resource" href="BUYER_DUE_DILIGENCE.md"><strong>Due-diligence checklist</strong><span>Pre-purchase and contract controls</span></a>
      <a class="resource" href="FINAL_VALIDATION.json"><strong>Validation record</strong><span>Counts, integrity, and secret scan</span></a>
      <a class="resource" href="URL_VERIFICATION.json"><strong>URL verification</strong><span>URL-level response results</span></a>
      <a class="resource" href="REPOSITORY_MANIFEST.json"><strong>Repository manifest</strong><span>Tracked-file hashes</span></a>
    </div>
  </section>
</main>
<footer class="footer"><div class="shell"><strong>Overdeliver.</strong> Evidence-backed audience access research. Confirm current terms, consent, sender responsibility, suppression, offer clearance, and applicable law before deployment.</div></footer>

<script type="application/json" id="vendor-data">__VENDORS__</script>
<script type="application/json" id="source-data">__SOURCES__</script>
<script>
const vendors=JSON.parse(document.getElementById('vendor-data').textContent);
const sources=JSON.parse(document.getElementById('source-data').textContent);
const $=s=>document.querySelector(s);
const $$=s=>[...document.querySelectorAll(s)];
const esc=value=>String(value??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
const slug=value=>String(value??'').toLowerCase().replace(/[^a-z0-9_-]+/g,'-');
const unique=(rows,key)=>[...new Set(rows.map(row=>row[key]).filter(Boolean))].sort((a,b)=>a.localeCompare(b));
const text=row=>Object.values(row).join(' ').toLowerCase();
const option=(value,label=value)=>`<option value="${esc(value)}">${esc(label)}</option>`;

function route(){
  const id=(location.hash||'#overview').slice(1);
  const target=$(`[data-view="${CSS.escape(id)}"]`)||$('[data-view="overview"]');
  $$('.view').forEach(view=>view.classList.toggle('active',view===target));
  $$('.nav a').forEach(link=>link.setAttribute('aria-current',link.dataset.route===target.dataset.view?'page':'false'));
  document.title=`${target.dataset.view==='overview'?'Overdeliver':target.querySelector('h2')?.textContent+' — Overdeliver'}`;
  if(target.dataset.view==='vendors') renderVendors();
  if(target.dataset.view==='sources') renderSources();
  window.scrollTo({top:0,behavior:'instant'});
}

function linkForNote(note){
  const value=String(note||'').trim();
  return /^(RAW_OFFICIAL_FETCHES|AGENT_RESEARCH)\/.+\.(html|md|txt)$/i.test(value)?`<a class="button" href="${esc(value)}">Stored evidence</a>`:'';
}

function renderVendors(){
  const query=$('#vendor-search').value.trim().toLowerCase();
  const lane=$('#vendor-lane').value,confidence=$('#vendor-confidence').value,status=$('#vendor-status').value;
  const rows=vendors.filter(row=>(!query||text(row).includes(query))&&(!lane||row.lane===lane)&&(!confidence||row.confidence===confidence)&&(!status||row.status===status));
  $('#vendor-count').textContent=`${rows.length} of ${vendors.length} shown`;
  $('#vendor-list').innerHTML=rows.length?rows.map(row=>`<article class="record">
    <div class="record-head"><div><div class="kicker">${esc(row.lane)} · ${esc(row.category)}</div><h3>${esc(row.name)}</h3></div><div class="tag-row"><span class="tag ${slug(row.confidence)}">${esc(row.confidence)} confidence</span><span class="tag ${slug(row.status)}">${esc(row.status)}</span></div></div>
    <p class="fit">${esc(row.fit)}</p>
    <details><summary>Evidence and caveats</summary><dl><dt>Official evidence</dt><dd>${esc(row.official_evidence)}</dd><dt>Not proven</dt><dd>${esc(row.not_proven)}</dd><dt>Repository note</dt><dd>${esc(row.notes)}</dd></dl><div class="actions"><a class="button primary" href="${esc(row.official_url)}" target="_blank" rel="noopener">Official source ↗</a>${linkForNote(row.notes)}</div></details>
  </article>`).join(''):'<div class="empty">No providers match those filters.</div>';
}

function renderSources(){
  const query=$('#source-search').value.trim().toLowerCase();
  const type=$('#source-type').value,status=$('#source-status').value;
  const rows=sources.filter(row=>(!query||text(row).includes(query))&&(!type||row.source_type===type)&&(!status||row.verification_status===status));
  $('#source-count').textContent=`${rows.length} of ${sources.length} shown`;
  $('#source-list').innerHTML=rows.length?rows.map(row=>`<article class="record">
    <div class="record-head"><div><div class="kicker">${esc(row.source_id)} · ${esc(row.source_type)}</div><h3>${esc(new URL(row.url).hostname.replace(/^www\./,''))}</h3></div><div class="tag-row"><span class="tag ${slug(row.verification_status)}">${esc(row.verification_status.replaceAll('_',' '))}</span>${row.official_or_regulator==='yes'?'<span class="tag">official / regulator</span>':''}</div></div>
    <p class="fit">${esc(row.evidence_observed)}</p>
    <details><summary>Source details</summary><dl><dt>URL</dt><dd>${esc(row.url)}</dd><dt>Notes</dt><dd>${esc(row.notes)}</dd><dt>Stored artifact</dt><dd>${esc(row.local_artifact)}</dd></dl><div class="actions"><a class="button primary" href="${esc(row.url)}" target="_blank" rel="noopener">Live source ↗</a><a class="button" href="${esc(row.local_artifact)}">Stored capture</a></div></details>
  </article>`).join(''):'<div class="empty">No sources match those filters.</div>';
}

function fillSelect(selector,values){const select=$(selector);values.forEach(value=>select.insertAdjacentHTML('beforeend',option(value)));}
fillSelect('#vendor-lane',unique(vendors,'lane'));
fillSelect('#vendor-confidence',unique(vendors,'confidence'));
fillSelect('#vendor-status',unique(vendors,'status'));
fillSelect('#source-type',unique(sources,'source_type'));
fillSelect('#source-status',unique(sources,'verification_status'));
['#vendor-search','#vendor-lane','#vendor-confidence','#vendor-status'].forEach(selector=>$(selector).addEventListener('input',renderVendors));
['#source-search','#source-type','#source-status'].forEach(selector=>$(selector).addEventListener('input',renderSources));
const laneCounts=vendors.reduce((acc,row)=>(acc[row.lane]=(acc[row.lane]||0)+1,acc),{});
$('#lane-summary').innerHTML=Object.entries(laneCounts).sort((a,b)=>b[1]-a[1]).map(([lane,count])=>`<button class="lane" type="button" data-lane="${esc(lane)}"><strong>${esc(lane)}</strong><small>${count} provider${count===1?'':'s'} — open directory</small></button>`).join('');
$('#lane-summary').addEventListener('click',event=>{const button=event.target.closest('[data-lane]');if(!button)return;$('#vendor-lane').value=button.dataset.lane;location.hash='vendors';renderVendors();});
window.addEventListener('hashchange',route);
route();
</script>
</body>
</html>
'''

html = (html.replace("__VENDOR_COUNT__", str(len(vendors)))
            .replace("__SOURCE_COUNT__", str(len(sources)))
            .replace("__HTTP_COUNT__", str(validation["http_200"]))
            .replace("__VENDORS__", compact_json(vendors))
            .replace("__SOURCES__", compact_json(sources)))

(ROOT / "index.html").write_text(html, encoding="utf-8")
print(json.dumps({
    "site": str(ROOT / "index.html"),
    "bytes": len(html.encode("utf-8")),
    "vendors": len(vendors),
    "sources": len(sources),
    "lanes": sorted({row["lane"] for row in vendors}),
}, indent=2))

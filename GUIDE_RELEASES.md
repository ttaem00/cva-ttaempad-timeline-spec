# Guide release maintenance

## Issue77 deployed-version catalog / 2026-10-24

The public catalog contains actual product versions delivered to users, not
documentation-only version identifiers. A captured document, archive status or
published guide is not evidence that its product version was deployed. Review
the whole catalog against this rule when correcting an entry. Public Store
publication and an actual development installation are distinct evidence.

| Version | Product delivery evidence |
|---|---|
| 0.4.0 | Actual Normal/Pro package installation and Chrome adoption: product `docs/release-0.4.0.md`, R51/R55 verification. Store review remains separate. |
| 0.3.39 | R53 dashboard observation below: Normal published at 0.3.39; product `docs/issue-125-validation.md` records installed worker/parser adoption. |
| 0.3.37 | Product `docs/project-qa.md` and `docs/store-readiness.md`: actual public Store version observed on 2026-10-09. |
| 0.3.32 | [Public v0.3.32 release](https://github.com/ttaem00/CVA-TTaempad/releases/tag/v0.3.32), 2026-10-05, non-draft/non-prerelease with Store ZIP. |
| 0.3.31 | Product `docs/cafe-introduction.md`: actual Chrome installation used for the 2026-10-05 capture. This is not a Store-publication claim. |
| 0.3.23 | This repository's validation record: same Chrome extension updated/reloaded to 0.3.23 and active version verified. Store submission was not performed. |

The manager also removed the development preview from the maintained internal
snapshot and editable draft. Its dedicated release/validation entries and README
link are removed; older task audit statements below describe past observations,
not current preservation instructions. Git history is not rewritten. Neutral old
HTML routes use current page keys independently of snapshot lifetime. Retained
internal histories still pass the same inventory/hash checks. Public previews
are rejected by catalog validation. No current article or image pixels change.

Same-task Harness diagnosis and the W3C/Jekyll redirect research recorded below
remain applicable; the change is removal of snapshot coupling, not a new browser
mechanism. Harness status remains enabled/integrity PASS with no active run.

## Issue77 public current-guide navigation / 2026-10-24

The public version selector helps readers choose usable product guidance. Internal
draft provenance belongs in maintenance history, without a public explanation of
an authoring mistake. This follow-up supersedes the public label approach below:
the draft is absent from the public catalog, history page and search. Stable and
authoringVersion remain 0.4.0; current article content is unchanged.

Preservation and publication now have separate inputs. Every internal numeric
history directory still passes its original inventory/hash checks. Retired HTML
entry points are routing data outside the public version catalog. Their exact
generated subtree is reconciled before rebuilding neutral current-guide links;
old Markdown, examples and search payloads are no longer published. Page keys
route to the corresponding current page, with query/fragment preservation and a
visible current-guide fallback. Frozen history, draft sources and image bytes
are not edited. Repeated builds must not republish old payloads.

Primary references: [W3C H76](https://www.w3.org/WAI/WCAG22/Techniques/html/H76)
and [jekyll-redirect-from's template](https://github.com/jekyll/jekyll-redirect-from/blob/master/lib/jekyll-redirect-from/redirect.html)
support a neutral immediate redirect with a plain fallback link. The existing
static builder implements that small pattern, preserving the fragment in script;
no redirect dependency is added. [Read the Docs hidden versions](https://docs.readthedocs.com/platform/latest/guides/hiding-a-version.html)
separates selector visibility from storage, but hiding alone leaves old content
accessible and does not satisfy this request. The modern-web-guidance lookup had
no matching entry; these primary sources supply the applicable design evidence.

## Issue77 current 0.4.0 comment compatibility / 2026-10-24

The manager authorized applying and publishing the current 0.4.0 guide correction
in [Issue77](https://github.com/ttaem00/cva-ttaempad-timeline-spec/issues/77).
Current comment pages and the current SPEC/SUPPORT references describe copied
Markdown escapes and hardbreaks, trailing bracket clocks and a short standalone
title's local increasing peer list. The title borrows its first child's actual
clock; explicit roles/ranges, raw text and ambiguous Point anchors remain authoritative.
Product main is `8f9c1937c1d7aa3ed29532f867b3abc6330bfa23`; the explicitly supplied
parser SHA256 is `7649a97f5fa19fca63e7750ee7a846250eba5121cf4fe1975ebc7954c50fb300`.
Stable/authoring stay 0.4.0. Frozen histories, draft sources and all image pixels
remain preserved. The incorrectly named preview entry is reclassified below.
Source validation and actual Pages publication
are separate evidence; publication is not established by a local build.

The original source-workspace failure used the stale active-main-runtime issuer
at `31b3504d`, which required a guard inside the target repository. Canonical
runtime PR2691 (merge `120aef77`) had already added the trusted issuer guard for
an absent target guard while retaining precedence for an existing target guard
and its failures. The current canonical issuer is adopted; no duplicate guard
repair is needed. `Resolve-CodexRuntimeScript` accepts an explicit `-RepoRoot`
for the verified current canonical checkout, then prefers its current Git/self
path before environment fallback. This selection does not detect a stale script
version or change global environment variables. These are authoring-tool facts,
not additional product input requirements.

## Issue77 version-label correction / 2026-10-24

PR76 split support already implemented in product 0.4.0 into a separately named
0.4.1 documentation preview. Its capture metadata explicitly says productVersion
0.4.0; no manager request for a product or documentation 0.4.1 was verified.
The manager reaffirmed that both products and this repair belong to 0.4.0.
Current supported-input explanations therefore belong in the editable 0.4.0
guide, without inventing a future release number for a documentation correction.

The old route remains available as an archived draft labeled
"0.4.0 초안 · 0.4.1 오표기", rather than an upcoming release. Its source, capture
integrity and image bytes remain unchanged. Generated version menus and archived
page headers use that same configured label, so a storage identifier cannot
independently imply a product release. Stable and authoringVersion stay 0.4.0.
Selecting the stable version opens the current editable guide; the exact
original stable snapshot remains linked from the history page as a preserved
baseline. Readers need not distinguish two identically named stable menus to
reach the corrected current guidance.
Future product-version or preview decisions require an actual manager selection;
ordinary edits to the current guide do not create a new version.

Reference: [Docusaurus versioning](https://docusaurus.io/docs/versioning) also
separates route identifiers from labels shown in version menus and banners.
This guide reuses its existing label field for that distinction; no external
documentation engine or new redirect mechanism is introduced.

## Historical draft recorded as 0.4.1 / 2026-10-24

This was a documentation preview of the shared mixed-outline comment support,
incorrectly assigned a future-looking version as explained above.
The current installed Normal and CVA-TTaempad pro product versions remain 0.4.0;
stable and authoringVersion remain 0.4.0. No product 0.4.1 release, default-guide
promotion, Store publication or installed-browser acceptance follows from this
preview.

The draft with 15 pages was captured once from exact guide source
`93de16647c65895ad525e937f254620eee9ded1c` using
`guide-drafts/0.4.1/source`. Four pages explain unclocked explicit parents,
local peer tree/round relationships, preserved explicit roles and boundaries.
All pre-existing histories and image pixels remain preserved.

Two new synthetic PNGs use the existing actual-product-module renderer, product
version 0.4.0 and parser SHA256
`a645771086974d3b473780e1fddd60a3218a95990fd453729c798a9503a83bc0`.
The 19 previous cases are retained and two fictional cases are appended. The 21
renderer cases passed, the two new PNGs were visually checked, existing guide
conformance passed 15 parser cases and 6 people/portable cases, and 15 draft article
bodies passed 175 local links/fragments. These are renderer and local document
checks, separate from actual guide navigation or product/browser/output QA.
Publish only the PNGs; private capture adapters and modules are not site assets.


## Current 0.4.0 browser H.264 automatic encoding guidance / 2026-10-22

Issue58 describes the web Pro Export / Quick Export automatic encoding default
in the current cuts guide. Source preservation remains the first choice; processed
H.264 keeps the selected dimensions, cadence, profile (High by default) and target
bitrate. Automatic VBR peak behaviour and file size may differ from compatibility
encoding. Explicit Off / maximum-bitrate choices and unsupported browser settings
retain the compatibility path. Studio remains the default YouTube method.
Stable and authoringVersion stay 0.4.0. Frozen histories, drafts and image pixels
remain unchanged. This guidance is not a measured speed / GPU guarantee or the
completion of the six R56 long-output acceptance cells; publication and product
verification remain separate evidence.

## Current 0.4.0 Studio default correction / 2026-10-22

Issue58 updates the two current cuts-guide paragraphs to match the temporary
Studio-tab YouTube default for Normal and Pro Export / Quick Export while the
Google-account method is being stabilized. Google transfer remains an explicit
choice, and Pro preserves an explicitly saved Google or Studio method. The
current source explains the default marker without changing private-video
defaults or claiming upload, performance, Store or Google approval evidence.
Stable and authoringVersion stay 0.4.0; drafts, frozen histories and image pixels
remain unchanged. Merge and publication require the product owner's review.

## R53 explicit 0.4.0 public guide promotion / 2026-10-21

The manager explicitly selected the actual public guide and repository README to
describe current Normal and Pro 0.4.0, with their differences, separate Chrome
installation steps and two existing Store item links. This authorization supersedes
the earlier unpublished-only continuation boundary below for this release.

`guide-drafts/0.4.0/source/` reused the latest 15 editable pages from the former
1.0.0 authoring directory. The new 0.4.0 snapshot was captured exactly once from
committed authoring source `4f267724f95ba246a7ebb656ba792d7e3bf12afb`:

```text
python scripts/capture_guide_release.py --version 0.4.0 --ref 4f267724f95ba246a7ebb656ba792d7e3bf12afb --source-path guide-drafts/0.4.0/source
```

The captured source is now adopted into `docs/source`; stable and authoringVersion
are both 0.4.0. The former 0.3.39 stable and 1.0.0 development preview are archives.
The current first-page and README title spells the product `CVA-TTaempad pro`
exactly; that editorial title correction is distinct from the exact captured
source. The former authoring directory and every earlier history file and image
remain preserved. No old snapshot was renamed or recaptured. The selected guide
baseline does not claim product 1.0.0 release or Store approval.

The 0.4.0 snapshot, current sources, version pointers and generated reading site
are now reconciled locally. One existing `scripts/Test-PrValidationGate.ps1` run
passed the committed-input image/link inventory (428 assets), the generated site
(15 stable pages and 7 preserved versions), 15 static synthetic cases, all 8 guide
version tests, all 4 published-site tests and the whitespace check. The prepared
0.4.0 directory inventory then passed with 467 assets. All 317 prior history and
asset files remain byte exact apart from the generated current search index,
which intentionally follows the new source. The initial committed inventory
check refers to authoring HEAD; root must verify the final committed publication
inventory before merge. External guide publication is not performed
by this work. The prior exact-module
PNG pixels and public JSON URLs are retained. Current dashboard observations show
Normal published at 0.3.39 and Pro under its old name as a 1.0.0 draft. Neither
0.4.0 Store submission nor publication is claimed here. Existing output timings
retain their measured scope; the R53 Studio transfer implementation and its
product validation remain root-owned and are not converted into an unmeasured
speed guarantee in this guide.

## R52 0.4.0 final QA reconciliation / 2026-10-21

The current installed development version is 0.4.0. Correct only existing unpublished draft text for R51 acceptance and the observed Google data-access review. R52 repaired the observed initial-preferences/control ordering defect and verified the same installed Chrome short-link activation, separate shared-copy save and original VOD reentry. Full release remains NOT_READY; these text updates do not establish Whale or unexecuted release journeys. Existing stable0.3.39, published preview/history, images and version pointers remain unchanged.

## R51 unpublished development continuation / 2026-10-21

Issue58 continues only `guide-drafts/1.0.0/source`: Pro native-project sharing,
its existing short-link and JSON size boundaries, the default-on periodic autosave
control, and separate rendering / MP4 finalization / YouTube processing evidence.
The R51 source candidate batches metadata without changing the tested output bytes;
bounded synthetic timing is not a long-output speed guarantee. Candidate installation,
browser behavior and whole-product acceptance remain separate evidence. Stable0.3.39,
the published preview, frozen histories, image pixels and version pointers are unchanged.

The default site describes the explicitly selected stable app version, not the latest product main. `docs/guide-versions.json` is the single version pointer. The manager selected 0.3.39 on 2026-10-10. Product source: 396429e484d41a0478488fd35238c3a187ed0e5b. The guide stable designation is separate from Chrome Web Store publication. Previous 0.3.32, 0.3.31 and 0.3.23 snapshots remain immutable.

## Current authoring version correction / 2026-10-20

Normal and **CVA-TTaempad pro** remain in **0.n development**, and both current development package versions are **0.4.0**. Development packages are installed; follow-up repairs and real-use acceptance remain in progress. The existing `guide-drafts/1.0.0/` path, goal filenames and preserved `1.0.0` preview labels are historical documentation identifiers, not a released product version. Product 1.0.0 release and whole-product acceptance remain **NOT_DONE**.

Continue authoring in the existing unpublished draft paths. This text correction does not rename or recapture frozen snapshots, edit published/generated pages or assets, change version manifests or stable/authoring pointers, or authorize a separate current-development public route. The existing explicit, history-preserving publication boundary still applies. Historical records below keep their original labels and evidence scope; a published documentation preview is not a product 1.0.0 release.

| Module | Responsibility |
|---|---|
| `docs/source/*.md` | Editable current stable guide |
| `docs/guide-versions.json` | Stable baseline, authoring version and version-menu labels |
| `guide-history/<version>/` | Frozen text, examples, source revision and SHA-256 inventory |
| `docs/assets/versioned/` | Deduplicated immutable image pixels, named by SHA-256 |
| `scripts/capture_guide_release.py` | Capture an exact committed guide once; reject recaptures |
| `scripts/build_site.py` | Verify snapshots, build stable and version routes, validate all local links |
| `docs/assets/site.js` | Existing search/navigation and one delegated native image dialog |
| `scripts/test_guide_versions.py` | Reject silent promotion, changed history and unsafe resource links |
| `scripts/check_published_site.py` | Validate exact Git-tree or prepared-output image/link inventory before rebuilding |
| `scripts/test_published_site.py` | Reject omitted/changed images and broken generated links |
| `scripts/Test-PrValidationGate.ps1` | Aggregate site, fixtures, version and whitespace checks |

## Keep a new version

For a historical revision whose build manifest already records its version:

```text
python scripts/capture_guide_release.py --version 0.3.33 --ref <exact-commit>
```

For a new preview, prepare `guide-drafts/0.3.33/source/*.md` and `guide-drafts/0.3.33/version.json` containing `{"version":"0.3.33"}`. Commit them with the matching public images and examples, then capture that exact revision:

```text
python scripts/capture_guide_release.py --version 0.3.33 --ref <exact-commit> --source-path guide-drafts/0.3.33/source
```

Add its version entry with status `preview` to `docs/guide-versions.json`. Keep `stable` and `authoringVersion` unchanged. A rebuild will include the preview without changing the default guide. Never regenerate previous-version images through current product modules: snapshots use preserved pixels.

## Advance stable deliberately

Only after confirming the app's chosen stable release, copy that version's preserved source into `docs/source`, update both `stable` and `authoringVersion`, mark its entry `stable`, and change the prior entry to `archive`. Retain every history directory. The old guide's frozen revision remains readable; later editorial corrections are also retained in Git. Add any current-only notices needed for pages absent from an old version.

Run:

```text
python scripts/build_site.py
python scripts/test_guide_versions.py
python scripts/test_published_site.py
node scripts/validate.cjs
python -m http.server 8771 --bind 127.0.0.1 --directory docs
```

Verify actual version navigation, modal close/focus/scroll restoration, external tabs and a narrow viewport before merging. The generated stable and archived pages share this site's reading controls; their article text, examples and image pixels remain version-specific. Product parser, player, renderer, CSS and extension JavaScript are not deployed by this builder. Existing public JSON URLs remain available for previously sent links.

## Current images within a stable version

Run `python scripts/check_published_site.py --directory .` on prepared output. Include every generated file, including new `docs/assets/versioned/*.png` files, in the owned commit. Then run `python scripts/check_published_site.py --ref HEAD` to validate the exact committed inventory. The PR gate checks that inventory before rebuilding: a build must not hide an omitted asset by recreating it only on the local machine. Validate the remote merge ref with the same command before merging.

`build_site.current_assets` pins the current PNG pixels by hash for the default guide. Archived routes use only their preserved `assets.json`. Updating a current example does not reuse the old stable image map or overwrite historical pixels. The product-owned `design/timeline-guide-examples/capture.cjs` generates the synthetic examples in its cases.json from actual shipped modules; publish only its PNG output. Capture proof, the private module bundle and installed-browser QA remain separate local release artifacts.

## 0.3.37 preview / 2026-10-09

User-requested package guide, preserved from exact guide source e13cb32c1108e404d1099f7d53f0e0783de73cdf. Product source 83fab17976b33dbd74868462e063218b1e2e457a. The remote issue48 branch is the authoring authority; local source archives are validation artifacts. At initial preview publication, stable and authoringVersion remained 0.3.32; the subsequent explicit promotion is recorded below. New synthetic PNGs use assets/preview/0.3.37; older pixels and frozen histories remain unchanged. Packaging and guide publication do not establish Chrome Web Store submission or Whale runtime QA.

## 0.3.37 stable promotion / 2026-10-09

The manager explicitly selected 0.3.37 as the default stable guide. The issue50 remote branch is the authoring authority. Copy the preserved 0.3.37 source to docs/source, set stable and authoringVersion to 0.3.37, and mark 0.3.32 archive. The same approved image bytes and every frozen history are retained. This guide designation does not submit a Chrome Web Store release or establish Whale runtime readiness.

## 0.3.39 semantic comment preview / 2026-10-10

The manager requested this public guide update and a product roster-chip correction.
The issue52 remote branch is the authoring authority; local source archives are
validation artifacts. Stable/authoringVersion stay0.3.37 and all earlier frozen
source/image snapshots remain unchanged. Product source396429e (full revision
recorded in VALIDATION.md) keeps inherited rosters as lookup context and presents
only each scene's own roster chips.

New draft pages describe marker-free heading/roster plus rounds, provisional
D1/D2/Point structure, before/after rosters, contextual VS and comparisons,
duplicate clocks, round overrides and safe termination/uncertain boundaries.
The current product-owned renderer generated19 offline synthetic PNGs with actual
DOM checks for inherited-chip suppression and preserved detail context. Only
PNG output is published; private bundles/proof and installed Chrome evidence
remain separate. Nine public semantic fixtures match the explicit local parser.

The0.3.39 snapshot comes from exact committed source
3b90a6cc4e7c957f8f30a71dbbae25d0b0865631. Global history article links work
from every version route, including fragments; this builder repair does not
rewrite historical Markdown or pixels.

Before first publication, review found two legacy people-page paragraphs that
still described inherited roster chips. The task-owned, unpublished0.3.39
capture from3b90a6c is retained in Git and the private recovery artifact.
Its corrected draft will be captured from a new exact source revision before
this preview's first public deployment. Previously published histories and
pixels remain byte-identical; no recapture guard is disabled.

Final first-publication0.3.39 snapshot source57087b6e8b6bfd71038486491033a1b2f2f2768f.
Only this task-owned new preview replaces its unpublished capture; previously
published history/source/pixels remain unchanged.

## 0.3.39 stable promotion / 2026-10-10

The manager explicitly selected the published0.3.39 guide as default stable. Issue54 remote branch is the authoring authority; task-owned archives are validation artifacts. Preserved0.3.39 source from57087b6e8b6bfd71038486491033a1b2f2f2768f is copied to docs/source, with current-only preview wording changed to stable. Stable/authoringVersion become0.3.39;0.3.37 becomes archive. Every frozen history file and image pixel remains unchanged. This guide promotion does not submit the Store package or verify installed Chrome adoption.


## Ordinary copy-option text draft / 2026-10-17

Issue58 prepares the ordinary development candidate's original-video preference
in `guide-drafts/1.0.0/source/cuts.md` and `limits.md`. New ordinary work defaults
to original video where supported; changing compression quality disables that
preference, while saved output settings retain their prior intent. The draft
also separates Studio receiver binding, delivery-time empty-input checks and
same-channel connection recovery from upload completion and retry safety.
The partial CHZZK candidate has passed a bounded installed 1080p60 file inspection
for video content, timing and regenerated audio structure. A normal ordinary
YouTube-button action has also delivered a supported-range result without manual
file selection and completed private Studio upload and processing. Broader input
coverage remains unverified; the previously delivered private video's watch-page
quality menu now lists 1080p60 HD and 720p60. This is an unshipped
text draft, not a new capture or a change to the published1.0.0 preview.
Stable/authoring stay0.3.39;
every frozen history, public route and image stays unchanged.

The current release contract accepts numeric app versions and preserves each
version exactly once. It defines no separate documentation revision suffix or
second capture for an already published version. Keep this draft unpublished
until the product owner selects an explicit, history-preserving publication
route. Do not invent an app version or bypass the recapture guard to publish it.

The whole/end-of-source and partition follow-up remains an unpublished text draft.
It describes conditional copying from source zero while preserving the original
video/audio start difference, separate later-keyframe-to-end checks,
compatible whole-source joins, and original-audio plus regenerated-AAC end checks.
Automatic part boundaries may use verified keyframes without changing saved cuts;
retry keeps established ranges and delivery history, and required repartitioning
affects only output that has not been delivered. Unsupported boundaries retain the
existing precise generation path. The reopened Issue58 continuation also describes
ordinary whole/end buttons that resolve the selected VOD at 1080 and read Input
duration up front, without output inspection, frame decoding or an FPS probe.
Optional numeric draft/cut coordinates preserve that duration through persistence,
forward wall-consistency validation and retime/split. Manual commit replaces the
selected numeric endpoint even when its displayed string is unchanged; Esc and a
canceled source transition preserve the previous draft. No near-EOF snap or deferred
EOF flag is introduced. A conditional unchanged single-whole HLS AAC path copies
eligible encoded audio, and requires both video/audio completion receipts before
the file can close successfully; other audio keeps precise trim/AAC regeneration.
Installed ordinary Main Chrome now has bounded normal-entry evidence for whole-button
collection, native-range work JSON saving and Undo, plus end-button precise draft JSON.
This confirms selection/persistence only, not a long whole-CHZZK output or whole AAC copy.
A subsequent multi-source output first required the explicit memory choice, then
stopped at a strict output-time-grid check with no completed file. The repair uses
integer tick accumulation for copied packets, fragment joins and required native PCM
lengths, preserving original coordinates and SDK tolerance. After installation, the
ordinary MP4 button produced a retained file in the original cut order. Independent
inspection passes its 1080p60 structure and full video decode. A fresh reordered
normal-button output is also retained physically. Both cut orders match all7506
source video access units, presentation times and decoded YUV frames. A continuous
AAC decoder repair reduces repeated one-second audio-boundary damage in a newer
retained reordered output; its video remains source-identical. That earlier file
still has448 zero startup frames despite active source audio and decoded AAC tail
padding. Its failure record is preserved. A later development-installation file
has source-correlated startup and join samples; the same Main Chrome WebAudio
decoder returns exactly its requested audio length. The separate decoder's tail
padding observation is retained. Neither numeric result establishes full audible
playback, perceptual sync or complete audiovisual acceptance.
The rendered baseline stopped at the actual memory cap, so no completed speed
comparison is established. Native endpoint cuts also expose an unresolved preview
clock/duration difference after final-fragment/EOS observation; stored cuts and
export coordinates are preserved. Long whole-CHZZK output, whole AAC copy and new
Studio delivery remain unverified. Earlier observations below
retain their original scope.

Earlier bounded Main Chrome checks cover actual
controller output from short local synthetic inputs: one whole 1080p60 source,
two whole-source occurrences joined at 1080p60, and a separate small 6fps input
split into two time-limited parts with retained-file retry. Independent inspection
passes video payload, decoded frames, timing and full-file decoding. The ordinary
installed entry and its original-first/Studio choices were checked separately;
these controller cases use a synthetic receiver and add no Studio upload.
Regenerated AAC startup/tail and source-reference limits remain explicit, without
audio byte-identity or perceptual-sync acceptance. Earlier bounded file and private
YouTube quality-menu observations retain their original scope. No actual 17-hour,
quota-exhaustion, Whale-runtime, publication, capture, stable-promotion, route or
preserved-history result is added.

## Ordinary development control guidance / 2026-10-18

The editable cuts and limits draft names the shorter **선택 장면으로** control,
explains **영상 생성 준비 중** before a part has progress values, and describes
returning to TTaempad to explicitly check a Studio tab opened later. Listing or
binding a receiver is kept separate from file generation, delivery and upload.
Preparation, cancellation and failure guidance continues to preserve existing
drafts and cuts. This text update adds no professional-editor behavior or new
Studio upload success claim.

The size notice now distinguishes estimated bytes from completed bytes and says
when the existing continue-download choice becomes available. Its actual 128 MiB
cap, incomplete-output handling and direct-save alternative remain unchanged.
The audio-limit text also separates the preserved earlier startup failure from
the later same-file startup/join and Chrome audio-decode observations. Full
audible playback and perceptual sync remain unverified.
These instructions describe an ordinary development installation; they do not
announce a new Store version or a full 1.0 release.

Only this editable text and maintenance record change. Stable/authoring remain
0.3.39; the published 1.0.0 preview, frozen histories, generated pages, images and
version pointers are preserved. The existing no-recapture publication boundary
still applies; no capture, publication or professional guide is added.

## Professional original-audio source candidate / 2026-10-19

At the initial source-only review, the editable 1.0.0 cuts and limits draft
distinguished the professional source candidate from the then-current
development installation and the ordinary whole-HLS AAC candidate. Its first
audio-copy cohort is a regular finite clear
MP4 AAC-LC stereo track used over its complete presented range, with a supported
original edit and complete known original roll context. Unsupported inputs keep
the existing native AAC processing path.

Processed-video Studio delivery must preserve the same completed native File
only after exact packet coverage, the selected presentation edit, complete AAC
termination and physical output close are proved together. This is an integration
requirement, not an actual-file or Studio acceptance claim. Real decoding,
listening, audiovisual sync and Studio delivery remain unverified for this source
candidate. A source-aac completion claim with missing or mismatched proof must
stop delivery and preserve existing edits instead of using an additional remux.
The existing non-source-aac finalization behavior is retained.

Only editable draft text and its maintenance/validation records are affected.
Stable/authoring remain 0.3.39. The published 1.0.0 preview, preserved history,
generated pages, version pointers, images and deployment remain unchanged.
No capture or publication route is selected.

## Professional full-track AAC development installation / 2026-10-19

The later professional source f361196906deb830548debbacee5824e21cde9ef is
installed and reloaded in the owned Main Chrome session. The editable cuts and
limits draft now describes this installed path rather than a source-only future
candidate. Its finite clear full-track AAC-LC stereo restrictions and existing
native AAC behavior for unsupported input remain unchanged. Missing or
mismatched source-audio completion proof stops delivery and preserves edits.

The bounded evidence covers 129 selected native tests, 167 JavaScript tests,
all 12 project QA steps, matching installed asset hashes, the actual installed
JavaScript rejection guard and saved-project preservation with eight original
attachments. These results do not establish a positive AAC output, independent
AAC decoding, listening, audiovisual sync or Studio delivery.

A separate reviewed ASC source correction passes 10 selected native tests and
retains the complete original configuration bytes. Its matching build,
installation and actual consumer evidence remain separate; this record does
not claim that the additional configuration support is installed. Earlier
source-only review results and failures retain their original scope.

Only these four editable draft/maintenance paths change. Stable/authoring stay
0.3.39; the published 1.0.0 preview, histories, generated pages, version pointers,
assets, images and deployment remain unchanged. Overall acceptance is NOT_DONE
and NO_SHIP; no new product output or Studio submission is added.


### 2026-10-19 — unpublished AAC actual-file checkpoint

The existing Issue58/PR60 draft remains unpublished. A wholly synthetic Pro native output preserved94 original AAC packets, complete original configuration/edit/roll metadata and1.98s movie presentation; the captured same File passed independent packet binding and same-decoder source comparison. This does not establish hearing/sync, other platforms, Studio or whole release acceptance. Production generic inspection still reports2s: the same1.61.0 edit-end omission is reported in [Mediabunny447](https://github.com/Vanilagy/mediabunny/issues/447). The source repair is under verification; no adoption/reload claim is made here.

A59-frame partial-audio control was actually re-encoded and captured after a QA route-label repair. Its native intermediate has padded AAC/1000Hz header rounding before the existing final remux, so exact final timing remains unverified. The incorrect QA assertion, initial discarded output, subsequent actual output and current finalizer gap are preserved separately. Stable/default0.3.39, published1.0 preview/history/version pointers/generated images/deployment are unchanged.


### 2026-10-19 — current unpublished native presentation boundary

The shared inspector source repair now passes paired project QA and reproducible SDK/source-offer builds. Retained physical-file public metadata queries read the1.98s declaration; legacy packet duration APIs are unchanged. The exact3-file runtime delta is installed in both fixed product folders with backups and full135/104 package equality. Same-Chrome reload was NOT_ATTEMPTED: an instrumented supported tool reconnect reached Chrome attach and timed out. Byte installation, reload request and actual behavior remain distinct.

Independent observation of the actual111349B ordinary finalized control preserved all59 AVC/94 AAC payloads/config, but default FFprobe reads every video timestamp+1/30 and end2s instead of59/30. FFmpeg decodes95232frames as in the raw native control,832 beyond selected94400; audible or browser playback is unverified. The raw native-processing file is also the direct Export/Quick local-save artifact, so its1000Hz edit rounding/AAC padding declaration is a separate user-visible gap, not solely an intermediate test seam. Native exact-close and distinct same-File completion proof source repair is ACTIVE; no new native output acceptance is claimed. Earlier successful source-AAC1.98 proof stays scoped and unchanged. Studio0, old failures and historical budgets preserved. Only the same four draft/maintenance paths change; protected stable/default0.3.39, published preview/history/generated/pointers/assets/deployment remain unchanged. Whole NOT_DONE/NO_SHIP.


### 2026-10-19 — source-native exact-end and same-file decoder comparison

The existing Pro source now carries the matching native exact-presentation patch and distinct post-Close same-File proof;129 preceding sourceAAC scope remains historical. Current selected native25/JS203/build-boundary8 and full project QA12steps (2491PASS/4skip) pass. A source-bound real software H264/AAC CPU synthetic output has59frames/end59/30 and explicit94400-sample audio presentation; actual positioned writes sync/close before completion. This is a CPU component, not installed Chrome or the original imported MP4. Native new assets are not installed or reloaded at this checkpoint.

The unchanged physical CPU file was observed by default FFmpeg8.1.1 and a checksum-pinned portable9.0.2 QA oracle. The old consumer emits832 extra AAC padding samples; the new consumer emits exactly94400/final192 and59video frames/end59/30. Official FFmpeg [8.1.1 FATE](https://github.com/FFmpeg/FFmpeg/blob/n8.1.1/tests/ref/fate/gaplessenc-pcm-to-mov-aac) versus [9.0 FATE](https://github.com/FFmpeg/FFmpeg/blob/n9.0/tests/ref/fate/gaplessenc-pcm-to-mov-aac) independently reproduces this partial-tail demux/decoder change. Old failure logs remain; no file trim/re-encode/remux or requested-duration override was used. Native generated AAC roll metadata completeness is a separate source compatibility check under Apple's explicit-delay guidance. Same-Chrome reload/private same-File finalizer, actual local picker, hearing/sync/other players/whole output and Studio remain UNVERIFIED. Whole NOT_DONE/NO_SHIP; no stable/default0.3.39, published preview/history/generated/version pointers/assets/deployment changes.


### 2026-10-19 — generated AAC roll, physical pair and installed bytes

The existing writer now maps the concrete builtin AAC decoder's one-access-unit dependency over the actual final AAC sample count, independently of encoder priming. Original source-AAC metadata stays preserved and custom/unknown encoders stay unspecified. Preferred fef4d5e1 source /11131fa5 patch has60 selected source tests PASS; matching pinned WASM build, physical CPU output and independent source review pass. The new84252B synthetic file9095e6db contains actual94 AAC roll(-1),59video/94400logical presentation. Physical sync/handle-drop precedes three held Pending polls with no proof until Close ACK, then public Done.

Independent new-file default9.0.2 observation ran three commands once, all exit0/empty stderr. Removing only the54 generated roll bytes and correcting their five enclosing lengths in memory reconstructs the entire preceding d7163247 file. All153 physical AV payload/config/timing/flags/side-data rows and decoded row hashes are identical. Default PCM94400/final frame192 and video59 both end59/30. Old8.1.1 tail832 remains preserved; final frame192 is not an extra tail. Separately, the original1.98s source-AAC file and copied counterpart both decode95040 under9.0.2 with identical rows; their old8.1.1 extra192 observation remains historical. [Official8.1.1 FATE](https://github.com/FFmpeg/FFmpeg/blob/n8.1.1/tests/ref/fate/gaplessenc-pcm-to-mov-aac) and [9.0 FATE](https://github.com/FFmpeg/FFmpeg/blob/n9.0/tests/ref/fate/gaplessenc-pcm-to-mov-aac) provide the version-specific partial-tail precedent, not a browser guarantee.

Current Pro full project QA12steps PASS/2491extension PASS4skip, build-boundary8PASS and editor135-file audit pass. The existing installer backed up the prior135 files, applied exactly five native runtime files and verified all135 incoming hashes. Reload was NOT_ATTEMPTED because the existing MainChrome initial attach remains quarantined; installed bytes and actual runtime are distinct. Normal's added U0 in-memory regressions pass fullQA2231/5skip and retain the actual regular-MP4 late header rewrite negative; no new upload/server ACK follows. Actual Chrome/private same-File consumer/local picker/Apple/hearing/sync/wholeHLS/long resources/Studio remain unverified. Whole NOT_DONE/NO_SHIP, old failures/budgets/Studio0 preserved. These four existing draft/maintenance paths do not publish or promote stable0.3.39, published preview/history/generated/version pointers/assets.


### 2026-10-19 — exact fractional video end and current installed bytes

The existing unpublished four-path draft now records the separate source-AAC and native-AAC CPU cases at selected99/50s: independent default FFmpeg9 observes60 video frames and95040 logical48kHz samples in each physical file. The last picture at59/30s and the60-frame grid extent2s remain distinct from the selected1.98s presentation end. SourceAAC preserves original94 AAC payload/config/edit/roll; nativeAAC has its separate post-Close nativePresentation proof. The earlier59-frame failure, pre-Exporter runner identity failures and older decoder-tail observations remain retained with their original scope. This is actual raw mux ledger plus direct encoder clock/origin snapshots and default decoding, not an encoder raw-packet probe or Main Chrome result.

Preferred source bda850537c226d5650b26fe95912faa2c252cf3851fac80124537fe1b088e36a /patch766d6e9e5a77a8a7e93b133360f9e57b28f9c30dd7b1994a047fb6aef87e2dab includes exact video mux clock scaling and the previously isolated bounded ready-AAC drain;87 selected source tests and current12-step project QA pass. No throughput improvement is established. Matching WASMd69b0f51a8a44f9474feb0e144d08ba27b6a6d171a608cb8f7929ad1fe4a5639 is installed through the existing135-file backup/verification path; only WASM/upstream changed and Normal104 files remain unchanged. Same-Chrome reload is NOT_ATTEMPTED because the existing initial attach remains quarantined. Actual Chrome output, HLS, local picker, Apple/other players, hearing/sync, long-resource and Studio acceptance stay UNVERIFIED. Only the existing four editable maintenance/draft paths change: stable/authoring0.3.39, published preview, histories, generated pages, version pointers, assets and deployment stay unchanged. Whole NOT_DONE/NO_SHIP; old budgets and Studio0 are preserved.

### 2026-10-20 - unpublished professional current-stage progress

The existing editable1.0.0 cuts/limits draft describes professional Export and Quick Export preparation, render, finalization, transfer and private-confirmation stages. Percentages and bytes require current-stage observations; unknown progress remains indeterminate. Transfer100 and legacy handoff do not establish private completion. Failed/cancelled/uncertain states retain their last actual measurement. Source tests, matching builds and installed browser observations remain separate; current integration is under verification and whole NOT_DONE/NO_SHIP remains. No private channel, uploaded filename or video link is included. R30 extends this same draft to shared General/Quick start and destination/settings disabling, a distinct local generation/write gauge, unknown cumulative-byte totals, physical saved completion and popup-close versus output-cancel semantics. Completed-file upload candidates also require a currently available matching file; direct local and disposed temporary artifacts are excluded. New-run preparation replaces prior destination status. Output locks use actual export ownership, leaving unrelated analysis/proxy/preview work and safe queue draft management available. A stopped queue may accept frozen Ready work; a running queue cannot start new work behind another busy output. An already-open preset manager preserves browsing/closing while applying settings stays locked. Current source/native/build/install checks remain separate and actual R30 Chrome behavior is not yet verified. Only these four draft/maintenance paths change; stable/default0.3.39, published1.0.0 preview, histories, generated pages, pointers, images and deployment remain unchanged.

### 2026-10-20 — unpublished R35 delivery choices and truthful connection stages

Issue58/PR60 retains the existing four editable maintenance/draft paths. The Normal draft now describes destination first, the relevant file or YouTube method next, and one visible primary action. Existing file preference is preserved; initial YouTube and missing legacy method remain Studio. Pro General/Quick retain adjacent file/YouTube actions with one YouTube method selection. Studio-only tab tools, Google human account/channel consent, private defaults and adjacent information readable during output remain explicit. Both existing sequence-settings context entrances and effective export target/format are described as candidate behavior; installed current-screen acceptance is pending.

Source connection events distinguish account authorization from channel checking without a fabricated percentage. A110-second authentication deadline and safe pre-begin noMedia errors explicitly state that generation and transmission have not started; later uncertain receipt and retained-file retry are separate. Normal518/520 failed before media and its initial auth subphase remains UNKNOWN. The new correction's installed runtime behavior is UNVERIFIED.

The actual Pro60-second broadcast cohort has first Google ACK during generation, the same execution's Studio private record and independently decoded same-file1080p60/3600video/2880000stereo samples/exact60s. It was processed/native-aac in692.537s, not a source-copy or speed comparison. The Studio1:01 display difference, exact source-window correspondence, hearing/sync and long-work acceptance remain unverified. The original app uncertain observation is preserved and app-final-settlement correction remains unverified. Separate legacy Studio496/497 completed private upload. The privacy website's PR4934 is merged; this does not complete OAuth/user rollout or product acceptance. No private channel, filename, video link or authentication value is included here.

This is unpublished text only. Stable/authoring0.3.39, the already published1.0.0 preview, frozen histories, generated pages, version pointers, image pixels and deployment remain unchanged. New actual UI screenshots and current installed output acceptance remain pending. Whole NOT_DONE/NO_SHIP remains.

### 2026-10-20 — unpublished R36 export choices and actual-output limits

The same four editable paths now describe the installed Normal destination/method layout: file or YouTube first; ordinary memory download versus an OS file picker before generation; Google streaming during generation versus completed-file Studio handoff. The advanced video settings stay in the native disclosure. Normal's adjacent information control and automatic/manual same-channel Studio selection are observed UI/connection evidence; selection and binding did not start another upload. All video defaults remain private, and overlapping generation/transfer can reduce waiting without a speed guarantee.

Pro General/Quick use a basename field and adjacent file/YouTube/information actions. Single H.264 MP4 without a sidecar uses the actual OS picker; other formats follow browser download settings. Shared output ownership disables new starts and relevant settings, while actual supported cancellation and reading the information remain available. Generation/write overlap, unknown byte totals, physical Close and private confirmation stay distinct; no intermediate100% is final acceptance. The old shared LocalCuts output panel is hidden in the Pro product and is not a second visible export UI.

The current site ownership check and production homepage deployment8c5699ae have HTTP200 evidence, with the common privacy body preserved. Google app verification remains incomplete and the full OAuth verification application has not been submitted. Neither website publication nor the retained private Pro60-second case establishes general Google authorization, Store publication or whole-product readiness.

Normal's actual360-second selected range completed in103.543s as rendered video plus regenerated AAC after an exact-end copy fallback. The22,202,994-byte file decodes without errors to21,598 video frames and17,280,000 stereo PCM frames. ISO video begins at42.673611ms and ends at360s; audio is0..360s, while ffprobe reports format duration360.042674s. Source correspondence/hearing/sync remain unverified. It is not a source-copy, filled0..360 frame-grid or whole six-minute A/V acceptance. Decoder-reuse follow-up is still under verification, with no accepted speed improvement or multiplier. Existing Pro60-second same-file/private scope and earlier failures remain intact. This follow-up writes no generated page, stable/default pointer, preview snapshot, history, image or deployment. Whole NOT_DONE/NO_SHIP remains.

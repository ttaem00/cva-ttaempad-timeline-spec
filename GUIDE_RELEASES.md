# Guide release maintenance

The default site describes the explicitly selected stable app version, not the latest product main. `docs/guide-versions.json` is the single version pointer. The manager selected 0.3.39 on 2026-10-10. Product source: 396429e484d41a0478488fd35238c3a187ed0e5b. The guide stable designation is separate from Chrome Web Store publication. Previous 0.3.32, 0.3.31 and 0.3.23 snapshots remain immutable.

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


##1.0.0 development preview /2026-10-17

The manager requested split-VOD cut insertion and direct sequential Studio delivery.
Issue56 adds a clearly labeled development preview with ordinary development-build
availability and separate professional verification status. Stable and authoring remain
0.3.39. Existing frozen histories and preserved images remain byte-exact. This preview
is documentation, not a Store/product release or a claim of full1.0 readiness.

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
retained reordered output; its video remains source-identical. The first448 audio
frames are still zero despite active source audio, and decoded AAC tail padding
remains. These are unresolved audio limits, not complete audiovisual acceptance.
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

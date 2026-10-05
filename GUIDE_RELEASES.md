# Guide release maintenance

The default site describes the explicitly selected stable app version, not the latest product main. `docs/guide-versions.json` is the single version pointer. The manager selected 0.3.32 on 2026-10-05. Source main: d880756f895e5ead61e8a424c88cbf302c69d835. The guide stable designation is separate from Chrome Web Store publication. Previous 0.3.31 and 0.3.23 snapshots remain immutable.

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
node scripts/validate.cjs
python -m http.server 8771 --bind 127.0.0.1 --directory docs
```

Verify actual version navigation, modal close/focus/scroll restoration, external tabs and a narrow viewport before merging. The generated stable and archived pages share this site's reading controls; their article text, examples and image pixels remain version-specific. Product parser, player, renderer, CSS and extension JavaScript are not deployed by this builder. Existing public JSON URLs remain available for previously sent links.

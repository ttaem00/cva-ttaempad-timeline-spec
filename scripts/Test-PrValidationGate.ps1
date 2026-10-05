#requires -Version 7.0
param([string]$Root, [int]$MaxTotalSeconds = 600, [int]$ChildTimeoutSeconds = 90, [int]$MainSyncTrackingIssue, [switch]$RemoteMergeRefValidation, [string]$RemoteMergeRefExpectedHead, [string]$RemoteMergeRefBaselineRoot, [string]$RemoteMergeRefBaselineHead)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
if ($Root) { $repoRoot = (Resolve-Path -LiteralPath $Root).Path }; Push-Location $repoRoot
try {
    & python scripts/check_published_site.py --ref HEAD
    if ($LASTEXITCODE -ne 0) { throw 'Committed publication inventory failed; rebuild and include every generated asset before committing' }
    & python scripts/build_site.py
    if ($LASTEXITCODE -ne 0) { throw 'Site build or generated links failed' }
    & node scripts/validate.cjs
    if ($LASTEXITCODE -ne 0) { throw 'Documentation checks failed' }
    & python scripts/test_guide_versions.py
    if ($LASTEXITCODE -ne 0) { throw 'Guide version boundaries failed' }
    & python scripts/test_published_site.py
    if ($LASTEXITCODE -ne 0) { throw 'Published asset regression checks failed' }
    & git diff --check
    if ($LASTEXITCODE -ne 0) { throw 'Diff whitespace check failed' }
    Write-Output 'RESULT: PASS'
} finally { Pop-Location }

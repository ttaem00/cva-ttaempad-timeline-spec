# 현재 문서 검증

2026-10-10에 사용자가 기본 안내를 **0.3.39 stable**로 선택했습니다. 새 댓글 형태와 합방·12명씩 더보기는 [현재 안내](docs/source/index.md)와 [지원 범위](docs/source/formats.md)에서 확인합니다. 이번 안내 승격은 기존 사이트·정확한 게시 자산·문서 conformance·버전 회귀 검사와 게시 후 화면 확인으로 검증합니다. 과거 실행 결과의 버전을 소급 변경하지 않습니다.

## 2026-10-05 당시 검증

2026-10-05 · 기본 문서는 **CVA-탬패드 0.3.31 stable** 기준입니다. 아래의 공유 기능 검증은 **0.3.32 미리보기**에 해당합니다.

- 최신 제품 파서로 기존 15개 댓글 사례와 6개 인물·호환 파일 사례를 대조합니다.
- 정적 사이트의 로컬 링크·목차·검색을 빌드 검사합니다. 문의·제보는 이메일로 연결됩니다.
- 예제 PNG는 제품 모듈을 사용하는 생성 템플릿에서 만들며, 합성 예제임을 표시합니다.
- 자동 인물 검색·겹치는 다시보기 불러오기·제목 옆 별/인물 칩을 현재 사용법으로 설명합니다.
- 공유 예제는 실제 설치된 메인 Chrome에서 링크 진입, 9개 장면·집계·컷 복원, 00:03:20 이동과 정지, 링크 복사, JSON 다운로드·파일 선택·복원, 별도 저장·다시 열기를 확인했습니다. JPEG는 해당 화면의 실제 캡처입니다. 가상 시간표·이름·집계이며 실제 영상 내용과는 무관합니다.

```text
python scripts/build_site.py
node scripts/validate.cjs --parser <제품의 content/comment_format.js>
```

## 이전 검증 기록

아래 날짜·버전은 당시의 기록이며 현재 지원 버전을 뜻하지 않습니다.

# 검증 기록

## 2026-10-03 문서 탐색과 시간축 화면 안내

문서 사이트의 목차 그룹·현재 위치 표시를 개선하고 Chrome 스토어 미리보기 링크를 상단 CTA로 추가했습니다. 실제 사용자가 제공한 편집 화면 캡처를 PNG 이미지로 안내하며, 제품의 CSS·JS나 해석기를 배포하지 않습니다. 이미지의 대체 텍스트·실제 치수·원본 보기 링크를 포함합니다. Markdown 원문과 생성 페이지에서 모두 이미지 경로를 확인합니다.

8개 페이지 재생성·로컬 링크 검사와 15개 합성 문서 사례 검사를 통과했습니다. 실제 브라우저에서 1280px·810px·390px 화면의 상단과 목차 배치, 모바일 목차의 키보드 펼치기, 이미지 원본 열기, 검색·Esc 닫기와 포커스 복귀를 확인했습니다. 이 검증은 문서 사이트의 사용 흐름에 해당하며, 확장 설치·편집 데이터 변경·스토어 출시 완료를 의미하지 않습니다.

## 0.4 소비자 후보와 읽기 사이트

2026-10-03, 공개 편집 초안 0.4는 CVA-탬패드 0.3.23 후보를 대상으로 명확한 상대 들여쓰기·단독 구분자·정상 이웃 보존·괄호 시각 확인 안내를 설명합니다. 기존 14개 시각·계층 예제와 6개 인물/파일 예제는 유지하며 혼합 형상의 합성 예제 1개를 추가했습니다. 실제 사용자 댓글·계정 자료는 포함하지 않습니다.

새 혼합 fixture는 시작·끝·역할·깊이·부모·진단을 함께 확인합니다. 2026-10-03에 현재 소비자 main commit `07ab0fb99ea4b5f80855c56db430c42ffe6a2b1d`와 대조해 시각·계층 15건, 인물/교환 파일 6건, 참가자 규격을 모두 통과했습니다. 검사한 `comment_format.js`의 Windows checkout SHA-256은 `8fba4e8c39be2c372ced824e9601bf6208112eafbdf672b773ce6179a64d2104`입니다. 소비자 별도 회귀 검사 382건과 로컬 병합 검증·Chrome/Whale 패키지 검사를 통과했습니다.

실제 브라우저에서 현재 소비자 parser와 댓글 미리보기 모듈을 합성 입력으로 실행했습니다. 13개 이동 시각, 부모 아래 D2, 구분자 뒤 4개 독립 순간, 마지막 주제의 미확정 끝, 괄호 시각 안내를 확인했고 부분 입력에서 자동 끝이 미확정으로 유지됐습니다. 이 검증은 실제 설치본의 댓글 채택·영상 재생·저장까지 검증했다는 뜻이 아닙니다. 기존 메인 Chrome 확장은 사용자 승인으로 같은 ID·권한을 유지해 0.3.23 코드 갱신·재로드했고 활성 버전을 확인했습니다. 저장된 댓글·컷·초안은 변경하지 않았습니다. 확장 스토어 제출은 수행하지 않았습니다.

읽기 사이트는 Python 표준 라이브러리만으로 8개 페이지를 생성합니다. 본문·문서 목차·현재 문서 목차·이전/다음·예제·원본 링크는 HTML에 있고, 로컬 검색과 작은 화면의 목차 접기는 보조 JavaScript입니다. builder가 로컬 링크·fragment·중복 ID를 검사합니다. 정적 검사만으로 실제 브라우저의 가독성·검색·키보드·반응형 통과를 주장하지 않습니다. 사이트에는 제품 parser·온라인 댓글 입력·인증·자동 게시가 없습니다.

```text
python scripts/build_site.py
node scripts/validate.cjs
node scripts/validate.cjs --parser /absolute/path/to/comment_format.js --roster-parser /absolute/path/to/people_input.js
python -m http.server 8768 --directory docs
```

사이트 출력의 상대 경로와 SHA-256은 `docs/build-manifest.json`에 기록합니다. 재현 명령에는 비공개 저장소·계정·브라우저 자료가 필요하지 않습니다. 공개 소스는 이 저장소의 문서·합성 예제·site asset뿐이며 제품 설치 사본·배포 ZIP과 별도입니다.

## 이전 검증 기록

2026-10-01 공개 편집 초안 0.2. 기존 합성 fixture 8건과 자연 목차 5건을 현재 제품의 `comment_preview.v2` parser와 대조합니다. 검사 항목은 시작/끝, 진단, 미해석 원문이며 자연 목차는 역할·깊이·부모 연결도 확인합니다. D1–D6와 반복/복수 시각을 포함하고, 기존 제품의 별도 회귀 검사에는 부모 명단 상속, 강조, 부분 본문, 범위 오류, 답글 관계, 분할 뒤 부모 맥락과 종료 보존도 포함됩니다.

```text
node scripts/validate.cjs
node scripts/validate.cjs --parser /absolute/path/to/comment_format.js
```

첫 명령은 이 저장소의 JSON 형태, 문서 링크, 코드 블록을 확인합니다. 두 번째는 사용자가 이미 가진 호환 parser 모듈을 명시했을 때만 동작합니다. 모듈은 `parseCompatibleComments(documents, options)`를 제공해야 합니다. 이 저장소는 해당 parser를 다운로드하거나 배포하지 않습니다.

실행 결과, parser SHA-256과 확인한 문서 commit은 PR 검증 기록에 고정합니다. 다른 구현 간 호환성이나 플랫폼 댓글 게시 성공은 이 fixture 대조만으로 증명되지 않습니다. 제품 실사용 검증과 이 저장소의 문서 검증은 각자 범위를 표시합니다. C08 전체 변환 기본값은 이 공개 초안으로 승인되지 않습니다.

## 0.2 구현 대조 기준

자연 구조 지원을 확인한 소비자 main commit은 `1b57b43ab3e45e2b132abe72e625b7da57ba39b0`이며,
대조한 `comment_format.js` SHA-256은 `37e11b7916c64ef74dfc32c0953db83c5961919c609745680a235241bd6681e8`입니다.
이 저장소는 구현 파일을 배포하지 않으며, 사용자는 자신이 가진 parser를 명시해 같은 합성 예제를 검사합니다.

대조 결과: 기존 8건 + 자연 구조·부분 본문·붙여넣기 변형 5건, 총 13건 PASS.
소비자 별도 검증은 66개 회귀 테스트, Chrome·Whale 패키지 검사와 실제 main Chrome의
미리보기→한 번 채택→취소 복원→확장/탭 재로드 후 부분 상태·미확정 끝 보존을 포함합니다.
원본 영상의 정지 시각과 기존 저장 자료도 유지됐습니다. Whale 패키지 검사는 Whale 실사용 증거가 아닙니다.

## 0.3 소비자 후보 대조

2026-10-02, 소비자 구현 후보 commit `ba7dbf8232c35440966618ddeff61897f552f510`과 대조했습니다. main 채택 상태와는 별개입니다. 검사에 사용한 Windows 작업 사본 및 Chrome 후보 패키지의 `comment_format.js` SHA-256은 `f5046682770475a2abb36708298edc881632fe4184b6717667b74a93099bbbc8`입니다.

동일 commit의 LF 정규화 Git blob SHA-256은 `c2318de0321e16c4da9d590c306f53ad4ff64d405612bb8f2f5ceb13728dbe7d`입니다. 운영체제 checkout의 줄바꿈 때문에 바이트 해시가 달라질 수 있으므로 구현 commit과 검사한 파일의 해시를 함께 기록합니다.

기존 13건과 `(w. …)`/with 변형, 원문별 별칭, 충돌, 선언 원문의 상속 별칭, 구조 JSON 등 추가 6건의 합성 예제를 대조해 PASS했습니다. 소비자의 별도 회귀 검사 195건과 Chrome·Whale 패키지 검사도 PASS했습니다. 호환 JSON은 `readTimelineFile(text, name, videoNo)`로 먼저 읽고 `parseCompatibleComments`로 미리보기합니다. 역할·시각 투영이 달라지는 입력은 거부하므로 단순 JSON 문법 성공을 의미 보존 성공으로 해석하지 않습니다.

현재 main Chrome의 공식 확장 입구에서 구조 JSON 선택 후 기존 자료 유지 → 미리보기 → 명시 채택 흐름을 확인했습니다. 실제 댓글 원문이나 비공개 브라우저 자료는 이 저장소의 예제에 포함하지 않았습니다. 실제 이름의 정확한 신원·참여 여부·사건 정렬·게시 성공, 타 소비자 구현 호환성과 Whale 실행은 별도 확인 대상입니다.

## 0.3 CVA-TTaempad 0.3.3 후속 후보

2026-10-02, 같은 소비자 PR #26의 `ttaempad.v19` 후속 후보에서 14개 시각·계층 fixture, 6개 인물·구조 JSON fixture와 참가자 규격을 대조해 PASS했습니다. 강조 기호가 감싼 시각, 자유 제목과 중첩 목록, 별표 강조, 역순 시각과 미확정 끝을 포함합니다. 소비자 회귀 검사는 212건 PASS입니다. 참가자 입력은 비교 검색 범위를 지정하며 참여 사실·채널 신원·같은 사건을 확정하지 않습니다.

검사한 `comment_format.js` SHA-256: `2fd0ba6d708e28295b1532cafcbbfbb07c706b465150b61e6c6ba8dd8f61e8d2`.
검사한 `people_input.js` SHA-256: `fbb3b4d2e42035b032bf3bd6406570c4813714a4d7201d27717fe51271e932d6`.
대조한 소비자 구현 commit은 `61d6bf9df9d35a6e6584f5854a1e938c3c8ad220`입니다. 당시 소비자 검증 기록은 212건, Chrome 38개 파일과 Whale 37개 파일 패키지 검사 PASS입니다. 이전 후보 검증은 위 기록의 해당 commit에만 적용됩니다.

```text
node scripts/validate.cjs --parser /absolute/path/to/comment_format.js --roster-parser /absolute/path/to/people_input.js
```

후속 후보의 실제 HLS/교차 컷 출력은 메모리 저장소를 쓰는 main Chrome 검증 화면에서 확인했습니다. 설치된 확장, 치지직 원본 플레이어, CSP/권한 동작이나 공개 게시 성공을 이 증거로 대신하지 않습니다. Chrome 확장 관리 화면의 자동 제어가 제한되어 사용자의 후보 패키지 수동 로드 후 공식 입구를 확인해야 합니다. 공개 main 채택은 아직 별개입니다.

## 0.3.39 guide follow-up

Product source396429e includes UI-only direct roster chips; shared parser SHA256
d5a1a26b6a181ed19c5998c0736dc59cfaa73439e5b09893a00e721b23702b45
is unchanged. Nine new semantic comment fixtures pass explicit local-parser
conformance. The existing time and roster fixtures are checked after generation.
Nineteen synthetic PNGs come from the actual current product modules; capture
checks DOM roster-chip inheritance and detail context alongside stars/alignment.
Product auto QA passes921 extension cases and32 short-link cases; source/package
checks do not establish installed Chrome or Whale behavior.

Guide stable/authoringVersion remain0.3.37; preview0.3.39 is separate. Exact
committed inventory, generated-site regression and published navigation evidence
are recorded with this release. No product JS/CSS/private capture bundle is
published. Main Chrome list_extensions returned Transport closed, so current
product runtime adoption is UNVERIFIED.

Prepared0.3.39 output passes the existing site/link builder and exact image/link
manifest checker(389 assets),15 existing parser time fixtures,6 roster/file
fixtures,9 semantic fixtures,8 version checks and4 missing-asset/link regression
checks. An actual IAB local page opened the new synthetic image dialog, closed
it and returned focus to the same image link. At390px the document width375px
and article327px stay within the viewport. The people page shows the direct
roster-chip policy. Images below the viewport use existing lazy loading; this
is not installed Chrome evidence.

The new version's history.md article link exposed a builder omission: historical
versions do not render their own history page. rewrite_link now routes this
shared document to the global history page with its fragment intact. A regression
check covers root stable and preview contexts. Frozen source text/pixels remain
unchanged. Exact guide source snapshot3b90a6cc4e7c957f8f30a71dbbae25d0b0865631;
full product396429e484d41a0478488fd35238c3a187ed0e5b.

Pre-publication review rejected two stale people-page chip explanations. The
corrected draft describes direct Point candidates and inherited roster details
consistently with the current19 PNGs. The unpublished initial capture is retained
as recovery/Git evidence; this task's new preview snapshot is regenerated from
the corrected exact commit before first publication. Existing published0.3.37
and earlier histories are untouched.

Final first-publication0.3.39 snapshot source57087b6e8b6bfd71038486491033a1b2f2f2768f.
Only this task-owned new preview replaces its unpublished capture; previously
published history/source/pixels remain unchanged.

## 0.3.39 stable promotion / 2026-10-10

User-selected default0.3.39 uses the published source and actual-module images. Both stable pointers and menu labels change together; the old0.3.37 is archived. All frozen history/source/image bytes remain unchanged. Existing site, documentation, version and publication-asset checks and exact remote tree/merge inventory must pass before publication. Live default/version navigation, current policy, image dialog/focus and narrow layout are verified separately after Pages builds. Product package and installed-browser checks remain separate evidence.


## Issue56:1.0.0 development preview

The ordinary development guide documents deliberate front/before insertion, source
clock preservation, supported1080p60, automatic actual-duration/byte/storage parts,
sequential private upload completion, retry and direct Studio interaction pauses.
Professional native verification and full1.0 release remain separate. No private QA
channel/video IDs, local paths, product runtime code or new screenshots are published.
Stable/authoring0.3.39 and all pre-existing frozen histories/image pixels are preserved.
The1.0.0 draft is frozen from de8eba81ba32452e8282d9c72c2b6550463a4eee.
An initial unpublished generated capture had a mixed-case fragment; it was retained
outside the source tree as rejected task evidence before the corrected first history
was prepared. No pre-existing committed history was edited or recaptured.

Prepared inventory428assets and all local links PASS before commit; product source
PR133 and receiver compatibility follow-up are separate from this public guide tree.
Actual multipart upload/private-save proof, exact committed tree checks and public-site
navigation readback are recorded independently before final completion.

## Issue58: ordinary original-video-copy option draft

The editable1.0.0 cuts/limits draft describes the ordinary original-video
preference for new work, explicit compression changes disabling that preference,
preservation of saved output intent, supported local H.264 MP4 and partial CHZZK
candidate ranges, precise audio trimming/AAC regeneration, exact-cut fallback and
the absence of a speed/file-size promise. Studio guidance distinguishes receiver
binding from empty-input checks at delivery and preserves existing tabs during
same-channel connection recovery without uncertain automatic retransmission.
No new image, product runtime code, internal benchmark result, private channel or
local path is published.

The ordinary HLS original-video candidate passed bounded real-file inspection
through the installed ordinary build's normal MP4 save button. One two-second
H.264 High 1920x1080/60 output contains 466973 bytes, SHA-256
`c26163cdeb27e7b24b97c3f87fc4270f71f0705620fc06e926c970cba4eadd16`.
All 120 source/output VCL NAL byte sequences and independently decoded YUV frame
hashes match, as do every rebased video PTS/duration and the dimensions. The first
video PTS is 0; output metadata records 60 fps and limited-range BT.709.
Regenerated 48 kHz stereo AAC passes structural/decode checks, with 256 final decoded
padding samples remaining beyond the selected two seconds. Original audio sample
identity, perceptual A/V sync and source DTS identity are not established.
Whole-VOD/end-of-source cuts, long processing and Studio upload of this copied
output were not verified by this observation. This evidence is not release readiness
or publication.

Validation on this draft: the existing build/link checks pass with15 stable pages
and6 preserved versions; prepared publication inventory passes428 assets;
the version suite passes8 tests, publication regression passes4 tests, and static
documentation validation passes15 synthetic cases. The existing guide renderer
also renders all14 draft pages in an external local-only preview and validates
their links/fragments, including the new cuts/limits links. Whitespace checks pass.

The original-preference and Studio wording follow-up repeats these checks with
unchanged validation scripts in an external local-only copy. All14 updated draft
pages render with valid links and fragments. The bounded real-file result above
is separate product evidence; these documentation checks do not broaden its scope.

The Studio retention follow-up explains that an existing delivery record keeps
its target and retry context across connection checks or changed output settings.
Explicit output cleanup retains existing Studio files and starts any next delivery
as a new transfer from the beginning. The same local documentation checks pass.

The reading-path follow-up distinguishes possible prefix reads for local recordings
from CHZZK manifest, initial video configuration and required-range reads. CHZZK
preparation checks boundaries, then validates selected packets in one output pass.
An incompatibility discovered during copying cancels unfinished generation, preserves
the cuts and does not silently retry through rendering. After reloading only the
ordinary extension in main Chrome, one normal MP4-save action on this reading-path
revision produced a two-second 1920x1080/60 file of 466973 bytes. All 120 source/output
VCL NAL sequences, decoded YUV frame hashes and rebased PTS/duration mappings match;
regenerated AAC passes structural checks. This bounded installed-file result applies
to that reading-path revision. The private Studio upload previously verified used render
fallback; copied-video Studio upload remained unverified at that revision. Broader output quality,
whole-VOD/end-of-source and long processing remain unverified. The same local
documentation checks pass.

The AAC presentation-end follow-up is grounded in product source
`4b1581c9ad5157fc7807986fb1a45efc2e64becc`, with 1614 project QA cases passing.
After reloading only the ordinary extension in main Chrome, one normal MP4-save
action produced a two-second 1920x1080/60 file of 466973 bytes, SHA-256
`766567cb4999a40c780c5a7d3c64b6263b72b233e73050db0104fa9e7aa60c88`.
All 120 VCL NAL sequences, independently decoded YUV frame hashes and rebased
PTS/duration mappings match; regenerated AAC passes structural checks. The first-mux
presentation cap and conditional omission of a second remux are supported by source
and synthetic consumer checks. This installed run did not count remux calls or
measure phase-specific timing, so it adds no direct remux-count or performance claim.
Copied-video Studio upload was not verified at this revision; the prior private upload
used render fallback. Other input quality, general cut boundaries, whole-VOD/end-of-source
and actual 17-hour processing remain unverified. This observation adds no support
for the separate temporary whole-source/EOF candidates.

The subsequent bounded ordinary-build check uses product source
`42ba4e98727e58b470057ccb805e3a7a6bfee4f1`, with 1674 project QA cases passing.
The same five runtime files were installed while 99 other installed files were
preserved. After reloading only the ordinary extension in main Chrome, one normal
MP4-save action produced a two-second 1920x1080/60 file of 466973 bytes, SHA-256
`90737a42112031daa845a1ed46e1c662430730dac0dce71df864fcaae09acd2c`.
All 120 VCL NAL sequences, independently decoded YUV frame hashes and rebased
PTS/duration mappings match; regenerated AAC passes structural checks. One normal
ordinary YouTube-button action also delivered an approximately 0.45 MiB result
without manual file selection. The same Studio video showed private save, upload,
processing and copyright checks completing without a reported problem. The assigned
file was cleaned up, so its separate SHA-256 and decoded content were not inspected.
The YouTube 1080p60 rendition list was not checked during that run; the server
preview at 360p and the local preview at 1080p did not establish that rendition.
This run did not measure phase timing, codec work or fetch counters. Source and
synthetic strict-source-first
end-of-source checks do not establish actual whole-source/EOF output, general cut
boundaries, other input quality or actual 17-hour processing. The bounded local-file
inspection and normal private Studio delivery do not broaden those support claims.
The same local documentation checks pass.

The output-explanation follow-up is grounded in product source
`3ce65336a719bcfdd2fc504ed73bb8bb33d6cc96`. Its source/package QA passes 12 steps
and 1683 cases. The draft now explains regeneration for exact cut boundaries,
selected size/direction or differing original video settings. It explicitly
distinguishes copied video from AAC audio regenerated for the cuts; audio-free
input receives no audio-regeneration phrase. Controller and mounted-UI regressions
use mocked media and Studio boundaries. After reloading only the ordinary extension
and its QA tab in main Chrome, one normal MP4-save action verified the copy/AAC
explanation on the installed revision. The controller reported 120 copied video
packets, no rendered video samples and 95 audio sample adds covering 96000 PCM
frames; these are controller observations, not internal codec-operation counts.
The resulting two-second 1920x1080/60 file contains 466973 bytes, SHA-256
`981efdd5c848e505519af3e37b4a30a86ce7e8239719ea2e0817a09758a030fd`.
The frozen independent validator passes all 120 VCL NAL sequences, decoded YUV
frame hashes and rebased PTS/duration mappings, with AAC structural checks. Other
fallback-reason labels retain controller/mounted-UI regression evidence. No new
Studio upload was performed on this explanation revision.

The earlier `42ba4e9` private Studio video was subsequently inspected on its normal
YouTube watch page: its quality menu lists 1080p60 HD and 720p60. This establishes
those menu choices for that video; no quality selection or publication setting was
changed. The assigned file's separate SHA-256 and decoded content remain unverified.
Neither observation adds whole-source or actual 17-hour evidence. Static
documentation and draft render/link checks pass; unchanged version/publication
checks retain the prior
results above.

Stable/authoring remain0.3.39. No `docs/` or `guide-history/` file changes are part
of this draft. Browser navigation, installed product behavior and deployment are
not established by these checks. This is an intentionally unpublished development draft. Publication requires
an explicit history-preserving route; this change does not recapture1.0.0 or
establish a new guide revision schema.

### Whole-source, end-range, join and automatic-part text follow-up

The new draft describes conditional source-zero copying with the original
video/audio start difference preserved, separate confirmation of source ends for
full reads and later-keyframe reads, compatible whole-source joins, and completion
checks for original audio and regenerated AAC when audio outlasts video. It also
distinguishes automatic internal part boundaries from saved cut coordinates and
preserves established retry ranges and prior delivery records. These conditions
do not promise copied output for general non-keyframe cuts; the existing precise
generation path remains available.

The product-owner's source record reports 1763 QA cases and Chrome/Whale package
checks passing, two fresh builds, public-helper synthetic checks and independent
decoded-frame comparisons. These are source/package and bounded synthetic evidence.
Subsequent actual Main Chrome controller checks and independent inspection of four
downloaded files pass within the following scope:

| Case | Input and actual file evidence |
|---|---|
| Whole source | Short 1920x1080 High/B 60fps synthetic source,120 video packets/decoded frames. First video PTS3840/90000, video end183840/90000; audio/movie end103424/48000. Original video payload, decoded frames and PTS/durations match |
| Two whole-source occurrences joined | The same retained synthetic source presented as two source occurrences,240 video packets/decoded frames at1920x1080/60. Original phase and the13920/90000 internal video gap are preserved. Video end377760/90000 differs from audio/movie end206848/48000; no video frame is extended |
| Time-based automatic parts and retained retry | Separate32x24 High/B 6fps synthetic source, split at91920/90000 into two files with6 frames each. Both retain expected source payload, decoded frames and rebased timing. Retrying the second part reuses its retained file with no re-encode; the receiver is synthetic |

All four files pass public and independent packet/configuration checks plus full
audio/video decoding. The actual controller record uses the frozen LocalCuts
implementation and public media constructors on an owned local test page. It is
separate from the installed ordinary entry check: after reloading only its QA tab,
the ordinary source identity, retained two cuts, original-first checkbox and Studio
choice were confirmed. These new controller cases do not establish a new normal
Studio upload. Time-based splitting is covered; forcing quota exhaustion or a
256GB output is not. Released test resources report no active inputs, outputs,
iterators, samples or retained files.

AAC is regenerated, with no compressed-audio or PCM byte-identity acceptance.
The whole and joined outputs decode to103424 and206848 frames respectively, equal
to their requested counts. The6fps part files decode to49152/48128 frames versus
49024/48000 requested:128 extra decoded samples per part,256 total. The first sample
above the fixed1e-5 amplitude threshold is at frame448 in both parts. This observation
is not a measured universal audio delay or a correction. Independently decoded
source audio lacks the final768 reference frames of the second part's requested
window; its container end does not prove original PCM coverage there. The almost
silent whole/join inputs and periodic6fps test tone do not establish perceptual
audio fidelity or lip sync. No matching old-renderer audio control was supplied for
these exact selections.

No actual17-hour processing, new Studio upload, Whale-runtime or live-publication
verification is established. The earlier bounded installed1080p60 file, controller
counts and private YouTube video's1080p60/720p60 menu observations above retain their
original revision and input scope; they are not repeated or broadened here.

This four-file draft has separate text/render/link validation. Those checks do not
run the product, broaden the actual controller/file results or publish a guide revision.
Stable 0.3.39, the already published 1.0.0 preview, every preserved history, image and
public route remain unchanged.

Root product review accepted these four editable paths after the bounded actual
results above. Post-integration source `faa838f46467c2c88135b722954324d6b12b629e`
passes all 12 project QA steps and 1779 extension cases with no skips, including
Chrome/Whale package audits. This is automated integration evidence, separate from
the actual Main Chrome controller, installed UI and file observations. Merging
this editable draft preserves the existing published site and every immutable
version; it does not select a new stable version or recapture published 1.0.0.

### Professional full-track AAC source candidate / 2026-10-19

The initial source-only draft review covered the professional candidate separately from
ordinary whole-HLS AAC. Admission requires a regular finite clear MP4 AAC-LC
stereo track, the full presented audio range, supported source-declared exact
clocks/edit and the complete known original sgpd/sbgp roll pair. Missing or
unsupported evidence does not authorize compressed-audio reuse.

The processed-video integration must prove actual written packet timing and
presentation coverage, an exact native video edit, original AAC End/count/coded
duration, the same source binding and the physical output Close acknowledgement.
Only that completed native result may retain the same File through Studio
finalization. A rendered-frame count alone is insufficient. An off-grid start
that cannot preserve the exact presentation remains on the existing native AAC
path before output claim; no timestamp rounding or post-claim encode fallback
is authorized.

For a source-aac claim, missing or mismatched completion evidence must stop
delivery and preserve existing edits. A sanitized proof does not authorize the
legacy remux if File ownership, revision, duration or exact tick checks fail.
Those failures must be terminal for source-aac; the existing non-source-aac
finalization behavior is retained. This is an accepted consumer-boundary repair
requirement at that review, not a claim that the successor source or actual
Studio flow had passed. Subsequent integration evidence is recorded below.

The preceding frozen full-track source unit reports 120 selected native tests
passing with zero ignored cases. The root matching build reproduces its frozen
source tree f1871873624f8549cd26b9572bad75e03138797fa590da189c045a8eaff95fe6
and completed in 167.843 seconds. The separately prepared root JavaScript seam
suite reports 158 passing tests. These are separate source, build and JavaScript
evidence scopes; at that point they did not establish canonical source adoption,
installation, an actual output file or processed-video Studio acceptance. The
processed-video integration requirement remained pending at that review.

Source and automated checks are separate from independent AAC decoding,
listening, audiovisual sync and actual Studio delivery. No new actual-file or
Studio acceptance is added by this documentation note. Prior failures and
existing bounded observations retain their original input and revision scope.

The FFmpeg edit-list implementation and its duration correction are relevant
design references, not acceptance evidence for this product:
[FFmpeg n8.0 movenc edit handling](https://github.com/FFmpeg/FFmpeg/blob/n8.0/libavformat/movenc.c#L3739-L3835)
and [the post-edit duration correction](https://ffmpeg.org/pipermail/ffmpeg-cvslog/2021-January/125662.html).

Issue58 remains open. Its earlier PR59 was merged at
b39d266571b5f1bd27cba6454e2522a722cccf9b; the current branch
codex/issue-58-normal-native-end-preview is tracked by open draft PR60. The
current draft does not reopen or rewrite that historical merge.

Stable/authoring 0.3.39, the published 1.0.0 preview, all frozen histories,
generated pages, version pointers and images remain unchanged.

### Professional AAC installed boundary and ASC source successor / 2026-10-19

The subsequent professional checkpoint f361196906deb830548debbacee5824e21cde9ef
adopts the processed-video exact-edit/packet/Close integration and terminal
source-aac proof failures, including a completion-owner mismatch before the
source claim could be lost. The existing non-source-aac finalization behavior
is retained. The root adjudication records 129 selected native tests, 167
JavaScript tests and eight build-boundary tests passing with zero ignored or
skipped cases. All 12 integrated project QA steps pass; their real-use status
remains UNVERIFIED and release status remains NOT_READY.

The matching development package was installed with an exact 135-file audit
and a five-file delta, then the extension and only the owned QA page were
reloaded. Served JavaScript, glue and WASM hashes match the installed candidate.
The actual installed JavaScript guard rejected a missing source-aac completion
proof, disposed/cancelled that owned test output and retained no part. It invoked
no actual native export and created no media file. This is an installed negative
boundary observation, not a positive native AAC consumer result or independently
observed WASM resource-use proof.

The original project was checked before, after and after normal save/re-entry:
eight attachments, durable saved bytes, snapshot/history/jobs and UI state were
preserved, with only the explicitly excluded runtime FPS changing. The saved
14,232-byte document SHA-256 is
cf3d3460c024d08349bfab563a1d5b391214d2a6cc60e9932166809a4fc88579.
The earlier wrong-canvas setup stop, first re-entry path mismatch and immediate
close observer are preserved in the raw records; their corrected checks do not
erase those failures or relax the original comparison.

A separate one-file ASC source successor has a reproduced actual-parsed
five-byte RED followed by 10 selected native tests passing, including raw
malformed/extension/configuration rejection before packet reads. Independent
review confirms that the prior 24 test bodies and unrelated source bytes remain
unchanged. Compact two-byte configuration leaves SBR unspecified; the admitted
five-byte form explicitly declares it absent. Both retain every original byte;
no truncation, normalization or roll manufacture is introduced. Its matching
build and installation are separate pending evidence at this documentation
checkpoint. This source result does not demonstrate real AAC payload decoding.

The local final adjudication receipt SHA-256 is
42ff92fa25c58743c9a49ca8e22b66be7f8795272eab2886b4a289e64c8f7daa;
the integrated QA report is
ec23fa00096577ab6cc8ae229b3638c2d3e6a93c6cbf8717958eea5a02d0cb31;
the installed-module observation is
5d1d2d02167972ce0117eb18f228c92477bb75754f56c8a11baa6a31f39d2852.
The ASC review uses mp4.rs SHA-256
b0177ecd5a24f823e3d3f81e0fd9dc2d713253d63bdc5364004d4229bc91d72d.
These receipts retain the exact source/build/install and raw evidence links.

Actual positive AAC output, independent decoding, listening, audiovisual sync
and this path's Studio delivery remain UNVERIFIED. Original product movies
2/2 remain CLOSED and extra Studio submissions remain 0. Overall NOT_DONE and
NO_SHIP are unchanged. This text update adds no media, capture, publication or
stable promotion; stable/authoring 0.3.39, the published 1.0.0 preview and all
protected histories, generated output, pointers and assets remain byte-exact.


### 2026-10-19 unpublished draft — actual original AAC and remaining inspection/finalizer boundaries

Only the existing four Issue58/PR60 maintenance paths changed. Pro captured processed-video/source-AAC output62687B preserved94 AU/config/edit/roll and exact1.98s movie declarations. Native Close proof and real same-File consumer/capture/disposal passed with one producer and zero second remux; the destination was simulated, Studio0. Default FFmpeg source/output PCM-s32 hashes matched93rows/95232samples, including192 samples beyond the95040-sample presentation declaration. These observations are scoped and do not establish audible trim/sync or general device support.

The generic production inspector's2vs1.98 duration mismatch is reproduced and matches the upstream1.61.0 [edit-end case447](https://github.com/Vanilagy/mediabunny/issues/447). New source queries/inspector tests and final source adoption are separate ongoing evidence. A captured111125B59-frame re-encoded control uses the expected existing native-processing route; its direct native intermediate is not the final Studio remuxed file and fails exact selected presentation. That failure remains recorded. No broad acceptance, public publication, stable promotion or actual Studio claim follows from these checks. All protected stable/history/generated assets remain exact.


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


### 2026-10-19 — unpublished exact fractional-clock CPU pair

The current source-AAC physical output63277B/SHA2561d2be0caa930d0b46bdaff388b6961e3c72ebb2fc9582ef7dc053b16ad65f8d7 and native-AAC output84289B/SHA25637e9dcc89096d7507b1be0e415d4b5d49caa8dd11bdcb5deba0006790be47204 each pass the independent default FFmpeg9 video60/PCM95040 observation at selected1.98s. SourceAAC keeps original94 AAC/config/roll and encoded AV payload/rational timing; the old final video discard flag1 becomes0. NativeAAC has its own exact post-Close proof and generated roll. Movie clocks90000/178200 and1000/1980 are exact equivalent selected ranges, not a forced common timescale. Video lastPTS59/30 and full60-frame grid extent2s are distinguished from presentation end1.98s. Positioned writes physically sync/close before held Pending polls and completion ACK. Earlier59-frame failure, two pre-Exporter serialization failures and old decoder-tail results remain preserved; no timing clamp, extra mux, new input or threshold correction is used in the observations.

Current source bda850537c226d5650b26fe95912faa2c252cf3851fac80124537fe1b088e36a /patch766d6e9e5a77a8a7e93b133360f9e57b28f9c30dd7b1994a047fb6aef87e2dab has87 selected source PASS and12-step full project QA PASS. The current QA report SHA256 is e3484fe7cfa14b58bfe6203db18ffcf2477d3324799745c090830ca2ab15cc04; runtime fingerprint5c2346c1d18726cd53dba617984a1c5882c59c47cf643198e049b9be625dde86. The135-file editor package passes audit; the existing installer backs up135 files and changes only WASMd69b0f51a8a44f9474feb0e144d08ba27b6a6d171a608cb8f7929ad1fe4a5639/upstream, then verifies all135 hashes. Normal104 is unchanged. These source/build/package/installed-byte results do not establish runtime reload: the initial Main Chrome attach remains quarantined and reload is NOT_ATTEMPTED. Same Chrome output/HLS/local picker/Apple/hearing/sync/long resources/Studio and whole acceptance remain UNVERIFIED or NOT_DONE. No speed comparison or public publication claim is made. This four-path text follow-up preserves stable0.3.39, published preview/history/generated pages/version pointers/assets/deployment and Studio0.

### 2026-10-20 - unpublished professional current-stage progress

The existing editable1.0.0 cuts/limits draft describes professional Export and Quick Export preparation, render, finalization, transfer and private-confirmation stages. Percentages and bytes require current-stage observations; unknown progress remains indeterminate. Transfer100 and legacy handoff do not establish private completion. Failed/cancelled/uncertain states retain their last actual measurement. Source tests, matching builds and installed browser observations remain separate; current integration is under verification and whole NOT_DONE/NO_SHIP remains. No private channel, uploaded filename or video link is included. R30 extends this same draft to shared General/Quick start and destination/settings disabling, a distinct local generation/write gauge, unknown cumulative-byte totals, physical saved completion and popup-close versus output-cancel semantics. Completed-file upload candidates also require a currently available matching file; direct local and disposed temporary artifacts are excluded. New-run preparation replaces prior destination status. Current source/native/build/install checks remain separate and actual R30 Chrome behavior is not yet verified. Only these four draft/maintenance paths change; stable/default0.3.39, published1.0.0 preview, histories, generated pages, pointers, images and deployment remain unchanged.

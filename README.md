# CVA-탬패드 · CVA-TTaempad pro 0.4.0 사용 안내

다시보기에서 장면을 찾고, 다른 시점과 비교하고, 필요한 구간을 편집해 저장하는 **CVA-탬패드 일반판과 CVA-TTaempad pro 0.4.0**의 사용 안내입니다. 댓글의 시각·목차·장면·관련 인물을 읽는 방법부터 컷 저장, YouTube 전송과 Pro 편집 공유까지 설명합니다.

```text
00:00 방송 시작
02:35 오늘 할 게임 이야기
08:12 다시 보고 싶은 순간
```

한 줄은 하나의 이동 지점입니다. 시간은 영상 경과시간이며 날짜·벽시계 시각이 아닙니다. Markdown은 선택사항입니다.

## 읽기 사이트

[웹 문서](https://ttaem00.github.io/cva-ttaempad-timeline-spec/)는 왼쪽 목차, 현재 문서 목차, 검색, 짧은 예제로 안내합니다. [사이트 출력](docs/index.html)과 [Markdown 원본](docs/source/index.md)도 저장소에 보존합니다. JavaScript가 없어도 본문과 문서 링크를 읽을 수 있습니다.

| 문서 | 내용 |
|---|---|
| [빠른 시작·제품 선택·Chrome 설치](docs/source/index.md) | 일반판과 Pro의 차이, 각각의 Store 주소와 설치 순서 |
| [지원 형태 한눈에](docs/source/formats.md) | 모든 현재 지원 형태를 예제와 의미로 비교 |
| [시간축 용어](docs/source/timeline.md) | 독립 목차에서 CVA의 d1·d2·dn·point·예상구간과 자동 끝 확인 |
| [자료 공유하기](docs/source/sharing.md) | 시간표·합방·집계·컷을 링크나 파일로 전달 |
| [요약과 JSON 가져오기](docs/source/summary.md) | 공개 요약 자동 연결과 게시 없는 로컬 호환 파일, 가상 요약 시간표 예제 |
| [기존 댓글 읽기](docs/source/existing.md) | 자연 목차, 상대 들여쓰기, 독립 목록, 괄호 시각 |
| [구간과 강조](docs/source/ranges.md) | 순간·범위·주제·강조·보조 설명 |
| [인물과 합방](PEOPLE.md) | 관련 인물, 명시 참여자, 원문별 별칭 |
| [파일 가져오기](IMPORT.md) | TXT와 시간축 JSON |
| [참가자 자료](ROSTER.md) | 한 줄 명단·참가자 JSON·기존 합방 자료 |
| [한계와 문제 해결](docs/source/limits.md) | 확인 안내, 오류 복구, 보장하지 않는 표현 |
| [의미 계약](SPEC.md) · [지원 범위](SUPPORT.md) · [검증 기록](VALIDATION.md) | 구현자용 조건과 검증 근거 |

## 현재 기준

현재 제품과 문서 작성 기준은 **0.4.0**입니다. 일반판은 다시보기 탐색·합방 비교·컷 수집과 순서 편집을, **CVA-TTaempad pro**는 시퀀스·트랙·효과를 사용하는 정밀 편집을 제공합니다. 2026-10-21 관리자가 0.4.0을 기본 안내로 선택했습니다. 정확한 작성 커밋을 캡처해 현재 문서와 버전 포인터를 0.4.0으로 맞췄으며, 생성·검증과 외부 게시 확인은 [유지보수 기록](GUIDE_RELEASES.md)에 구분합니다.

| 제품 | Chrome Web Store | 안내 |
|---|---|---|
| 일반판 · CVA-탬패드 | [일반판 Store 페이지](https://chromewebstore.google.com/detail/cva-%ED%83%AC%ED%8C%A8%EB%93%9C/ajokeikoipagcdnpdkkbamidkjgeghon?hl=ko) | [일반판 사용·설치](docs/source/index.md#일반판-chrome-설치) |
| Pro · CVA-TTaempad pro | [Pro Store 페이지](https://chromewebstore.google.com/detail/emkepdnkieiaadkciifenmhlkpiamhmm?hl=ko) | [Pro 사용·설치](docs/source/index.md#pro-chrome-설치) |

두 Store의 0.4.0 심사·공개 완료는 이 문서 작성만으로 확인되지 않습니다. Store에서 실제 제품명·버전을 확인하세요. 공개 전에는 기존 버전이 보이거나 Pro 페이지가 열리지 않을 수 있습니다. 개발 설치와 Store 설치도 구분합니다.

공개 버전 메뉴와 [버전 기록](docs/source/history.md)에는 실제 배포한 버전의 안내만 표시합니다. 댓글·시간표의 기존 기능과 `[M]`·`[메모]` 표기는 이어서 사용할 수 있습니다.

[자료 공유하기](docs/source/sharing.md)와 [컷 작업과 MP4 저장](docs/source/cuts.md)에서 0.4.0 기능을 확인하세요. 문서 버전 관리와 모듈 경로는 [유지보수 안내](GUIDE_RELEASES.md)에 있습니다.

화면 예제는 현재 제품 모듈로 만든 가상 입력의 PNG이며, 실제 사용 화면은 별도로 표시합니다. [현재 지원 범위](SUPPORT.md)와 [검증 기록](VALIDATION.md)을 함께 확인할 수 있습니다.

[문의·오류 제보](docs/source/contact.md) · [이용 정책](docs/source/policy.md)

## 재현

추가 라이브러리·인증 없이 Python 표준 라이브러리로 사이트를 만듭니다.

```text
python scripts/build_site.py
node scripts/validate.cjs
python -m http.server 8768 --directory docs
```

로컬 미리보기는 `http://127.0.0.1:8768/`에서 확인합니다. 이미 보유한 호환 parser를 선택적으로 대조하는 명령은 [검증 기록](VALIDATION.md)에 있습니다. builder는 parser를 다운로드하거나 공개하지 않습니다.

문서·예제·사이트의 현재 이용 조건은 [라이선스](LICENSE)와 [이용 정책](docs/source/policy.md)에 있습니다. 이전 MIT 버전의 유효한 허락은 유지됩니다. 문의는 [ttaem00@naver.com](mailto:ttaem00@naver.com)으로 보내 주세요.

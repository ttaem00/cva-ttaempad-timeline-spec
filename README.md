# CVA-탬패드 댓글 시간축 안내

다시보기 댓글의 **시각·목차·장면·관련 인물**을 읽고 확인하는 공개 문서입니다. 새 댓글은 간단한 시각 목록으로 시작할 수 있고, 기존 댓글은 원문을 보존하며 가져옵니다.

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
| [빠른 시작](docs/source/index.md) | 선택 → 미리보기 → 시간축에 불러오기 |
| [지원 형태 한눈에](docs/source/formats.md) | 모든 현재 지원 형태를 예제와 의미로 비교 |
| [시간축 용어](docs/source/timeline.md) | 독립 목차에서 CVA의 D1·D2·Dn·Point·예상 구간과 자동 끝 확인 |
| [링크로 공유하기](docs/source/sharing.md) | 댓글이 없는 영상에 시간표·인물·집계·컷 작업 전달 |
| [요약과 JSON 가져오기](docs/source/summary.md) | 공개 요약 자동 연결과 게시 없는 로컬 호환 파일, 가상 요약 시간표 예제 |
| [기존 댓글 읽기](docs/source/existing.md) | 자연 목차, 상대 들여쓰기, 독립 목록, 괄호 시각 |
| [구간과 강조](docs/source/ranges.md) | 순간·범위·주제·강조·보조 설명 |
| [인물과 합방](PEOPLE.md) | 관련 인물, 명시 참여자, 원문별 별칭 |
| [파일 가져오기](IMPORT.md) | TXT와 시간축 JSON |
| [참가자 자료](ROSTER.md) | 한 줄 명단·참가자 JSON·기존 합방 자료 |
| [한계와 문제 해결](docs/source/limits.md) | 확인 안내, 오류 복구, 보장하지 않는 표현 |
| [의미 계약](SPEC.md) · [지원 범위](SUPPORT.md) · [검증 기록](VALIDATION.md) | 구현자용 조건과 검증 근거 |

## 현재 기준

**CVA-탬패드 0.3.32**을 기준으로 설명합니다. 시각·구간·목차·별 표시와 제목 옆 인물 칩, 인물 자동 검색과 겹치는 다시보기 불러오기를 안내합니다. `[M]`과 `[메모]`는 같은 메모 표기입니다.

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

# Hyperframe Reference Studio

참고 영상의 구도와 움직임을 분석하고, **Codex + 로컬 HyperFrames**로 모션 그래픽을 만들고 검수하는 독립 스킬입니다.

[English](README.md) · [6초 예제 영상](docs/media/studio-demo.mp4) · [검증 기록](docs/VERIFICATION.md)

## 설치

```sh
npx skills add dearyour/hyperframe-reference-studio --skill hyperframe-reference-studio --agent codex --global --copy --yes
```

설치 후 Codex를 다시 시작하거나 새 세션을 여세요. `--global`을 빼면 현재 프로젝트에만 설치합니다. 기존에 이름이 `hyperframe`인 스킬과는 별도로 설치됩니다.

이렇게 요청하세요.

> $hyperframe-reference-studio 첨부한 참고 영상의 카드 배치와 등장 모션을 분석해서 내 문구로 재현해 줘. 1080×1920으로 만들고, SRT가 있으면 문장과 시간을 그대로 유지해. 렌더한 MP4의 길이와 실제 프레임까지 확인해 줘.

## 준비물

- Codex 등 스킬을 읽고 명령을 실행할 수 있는 AI 코딩 도구
- Node.js 22 이상, Python 3.10 이상, FFmpeg와 ffprobe
- 참고 영상 또는 이미지, 넣을 문구, 필요하면 SRT 파일
- 최초 패키지·브라우저 설치를 위한 인터넷과 저장 공간

**Manus 로그인이나 Manus 크레딧은 필요하지 않습니다.** Codex가 HTML과 모션을 작성하고 HyperFrames가 로컬에서 MP4를 렌더합니다. AI 도구 자체의 요금·사용량 제한은 별개입니다. 스킬 설치 명령만으로 위 실행 도구가 전부 설치되는 것은 아닙니다.

## 포함된 것

참고 장면 분석, 정확한 SRT 처리 규칙, 렌더 결과 검수 절차, 새 프로젝트 생성 스크립트, 영상 프레임 추출 스크립트, 한글 글꼴과 6초 예제를 포함합니다. 다른 사람의 다운로드 폴더나 개인 프로젝트 파일에 의존하지 않습니다. 사용자가 재현하고 싶은 별도의 참고 영상은 직접 제공해야 합니다.

공식 Keyframes·Registry·Seam Craft 등의 역할과 사용 시점을 안내합니다. 해당 공식 스킬 파일을 복사해 모두 내장하거나 자동 설치하는 패키지는 아닙니다. 공개 공식 문서를 필요한 작업에 맞춰 참고합니다.

예제는 공개 배포를 위해 새로 만든 디자인입니다. 어떤 영상이든 픽셀 단위로 동일하게 재현한다는 보장은 하지 않습니다. 코덱스가 문서를 읽고 실행하는 제작 절차이며, 실제 품질은 참고 자료와 구현·검수에 달려 있습니다.

## 바로 렌더해 보기

```sh
python3 ~/.codex/skills/hyperframe-reference-studio/scripts/new_project.py ./my-video
cd my-video
npm ci
npm run setup
npm run lint
npm run check
npm run render
ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp4
```

`out.mp4`가 생성되고 길이는 `6.000000`이어야 합니다. 기존 폴더에는 덮어쓰지 않습니다. 스킬 설치 위치를 변경했다면 첫 번째 명령의 경로를 바꾸세요. 오류가 나면 성공으로 간주하지 말고 실패한 명령부터 확인합니다.

원본 스킬·스크립트·예제 구성은 Apache-2.0, 포함된 Noto Sans KR 글꼴은 SIL OFL입니다. npm으로 설치하는 GSAP에는 별도 라이선스가 적용됩니다. [출처와 라이선스](skills/hyperframe-reference-studio/THIRD_PARTY_NOTICES.md)를 확인하세요. HeyGen·Manus·OpenAI의 공식 제품이나 독점 Manus 스킬의 추출본이 아닙니다.

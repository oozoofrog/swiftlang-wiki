---
type: entity
category: documentation
tags: [tips, development, productivity]
aliases: [개발 팁, Development Tips]
sources: [development-tips.md]
---

# 컴파일러 개발 팁

Swift 컴파일러 개발 생산성을 높이는 팁 모음.

## 빌드 속도

- **Ninja 직접 사용**: `ninja bin/swift-frontend`로 프론트엔드만 빌드
- **sccache**: C/C++ 빌드 캐싱 (캐시 50GB 권장)
- **hosttools 모드**: `--bootstrapping=hosttools`로 부트스트래핑 생략
- **타겟 선별**: `ninja -t targets | grep <keyword>`

## 듀얼 빌드 전략

Release로 표준 라이브러리, Debug로 swift-frontend만 빌드 후 Release 산출물 복사로 시간 단축.

## 기타

- `ninja -nv <target>`: dry-run으로 실제 명령 확인
- `-suppress-warnings`: 경고 숨기고 에러만 확인

관련 페이지: [[debugging-the-compiler]], [[getting-started]]

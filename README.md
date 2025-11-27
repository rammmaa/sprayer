# 후원 요청 메일 자동 발송 시스템

Gmail API를 사용하여 여러 회사에 후원 요청 메일을 자동으로 발송하는 Python 스크립트입니다. 각 회사별로 맞춤화된 LaTeX 후원기획서 PDF를 생성하고, HTML 메일 템플릿을 사용하여 개인화된 메일을 발송합니다.

## 주요 기능

- 📧 Gmail API를 통한 대량 메일 자동 발송
- 📄 LaTeX를 사용한 회사별 맞춤 후원기획서 PDF 생성
- 🎨 HTML 템플릿을 사용한 개인화된 메일 본문
- 📎 첨부 파일 자동 첨부 (PDF, 이미지 등)

## 설정 가이드

이 문서는 프로젝트 실행에 필요한 각 파일의 설정 방법을 설명합니다.

## 1. credentials.json (필수)

**위치**: 프로젝트 루트 디렉토리

**설정 방법**:
1. [Google Cloud Console](https://console.cloud.google.com/)에 접속
2. 새 프로젝트 생성 또는 기존 프로젝트 선택
3. "API 및 서비스" > "사용자 인증 정보"로 이동
4. "사용자 인증 정보 만들기" > "OAuth 클라이언트 ID" 선택
5. 애플리케이션 유형: "데스크톱 앱" 선택
6. 이름 입력 후 생성
7. 다운로드한 JSON 파일을 `credentials.json`으로 이름 변경하여 프로젝트 루트에 저장

**예시 파일**: `credentials.json.example` 참고

**중요**: 이 파일은 실제 Google Cloud Console에서 받은 파일로 교체해야 합니다.

---

## 2. token.json (자동 생성)

**위치**: 프로젝트 루트 디렉토리

**설정 방법**:
1. `credentials.json` 파일이 준비되면 다음 명령어 실행:
   ```bash
   python quickstart.py
   ```
2. 브라우저가 열리면 Google 계정으로 로그인 및 권한 승인
3. 자동으로 `token.json` 파일이 생성됩니다

**참고**: `token.json`은 한 번 생성하면 재사용 가능합니다. 만료되면 자동으로 갱신됩니다.

---

## 3. companies 파일 (필수)

**위치**: 프로젝트 루트 디렉토리 (이름 자유)

**형식**: 각 줄에 `회사이름,회사메일주소` 형식으로 작성

**규칙**:
- 회사 이름에 띄어쓰기는 없어야 함
- 띄어쓰기가 필요할 경우 `-`로 대체
- `-`가 필요할 경우 `\-`로 대체

**예시**:
```
네이버,naver@example.com
카카오,kakao@example.com
라인,line@example.com
당근마켓,daangn@example.com
```

**예시 파일**: `companies.example` 참고

---

## 4. sponsorship-proposal-documents/mail/mail.html (필수)

**위치**: `sponsorship-proposal-documents/mail/mail.html`

**설명**: 메일 본문 HTML 템플릿

**특수 변수**:
- `@회사@`: 회사 이름으로 자동 치환됩니다

**예시 파일**: `sponsorship-proposal-documents/mail/mail.html.example` 참고

**사용 방법**: 예시 파일을 복사하여 `mail.html`로 이름 변경 후 내용 수정

---

## 5. sponsorship-proposal-documents/paper/main.tex (필수)

**위치**: `sponsorship-proposal-documents/paper/main.tex`

**설명**: LaTeX로 작성된 후원기획서 템플릿

**특수 변수**:
- `@회사@`: 회사 이름으로 자동 치환됩니다

**예시 파일**: `sponsorship-proposal-documents/paper/main.tex.example` 참고

**사용 방법**: 예시 파일을 복사하여 `main.tex`로 이름 변경 후 내용 수정

**주의**: LaTeX 컴파일을 위해 `pdflatex`가 설치되어 있어야 합니다.

---

## 6. sponsorship-proposal-documents/res/pt-final.pdf (필수)

**위치**: `sponsorship-proposal-documents/res/pt-final.pdf`

**설명**: 홍보 자료 PDF 파일

**설정 방법**: 실제 홍보 자료 PDF 파일을 이 경로에 저장

**참고**: `install.sh` 실행 시 이 파일이 `attachments/` 디렉토리로 복사됩니다.

---

## 7. attachments/SUAPC포스터초안.png (선택)

**위치**: `attachments/SUAPC포스터초안.png`

**설명**: 메일 첨부용 포스터 이미지

**설정 방법**: 포스터 이미지 파일을 `attachments/` 디렉토리에 저장

---

## 전체 설정 순서

1. **credentials.json** 준비 (Google Cloud Console에서 다운로드)
2. **token.json** 생성 (`python quickstart.py` 실행)
3. **companies** 파일 생성 (회사 목록 작성)
4. **mail.html** 준비 (`mail.html.example` 복사 후 수정)
5. **main.tex** 준비 (`main.tex.example` 복사 후 수정)
6. **pt-final.pdf** 준비 (`sponsorship-proposal-documents/res/`에 저장)
7. **포스터 이미지** 준비 (`attachments/`에 저장, 선택사항)
8. **install.sh** 실행 (`./install.sh`)
9. **메일 발송** 실행 (`python run-for-companies.py companies`)

---

## 문제 해결

### LaTeX 컴파일 오류
- `pdflatex`가 설치되어 있는지 확인: `which pdflatex`
- macOS: `brew install basictex` 또는 `brew install mactex`
- Linux: `sudo apt-get install texlive-latex-base` (Ubuntu/Debian)

### Gmail API 오류
- `credentials.json`이 올바른지 확인
- `token.json`이 존재하는지 확인
- Google Cloud Console에서 Gmail API가 활성화되어 있는지 확인

### 파일 경로 오류
- 모든 파일이 올바른 경로에 있는지 확인
- `install.sh`를 실행했는지 확인

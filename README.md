# 후원 요청 메일 자동 발송 시스템

Gmail API를 사용하여 여러 회사에 후원 요청 메일을 자동으로 발송하는 Python 스크립트입니다. 각 회사별로 맞춤화된 LaTeX 후원기획서 PDF를 생성하고, HTML 메일 템플릿을 사용하여 개인화된 메일을 발송합니다.

## 빠른 시작

### 1. 환경 설정

```bash
# 의존성 설치
pip install -r requirements.txt

# 초기 설정 (첨부 파일 준비)
./install.sh
```

### 2. Gmail API 인증

```bash
# credentials.json을 프로젝트 루트에 저장한 후
python quickstart.py
```

브라우저가 열리면 Google 계정으로 로그인 및 권한 승인하면 `token.json`이 자동 생성됩니다.

### 3. 회사 목록 준비

`companies.txt` 파일을 생성하고 다음 형식으로 작성:

```
회사명, 이메일주소
네이버, naver@example.com
카카오, kakao@example.com
```

### 4. 메일 발송

```bash
python run-for-companies.py companies.txt
```

완료! 각 회사별로 맞춤 PDF와 메일이 자동으로 발송됩니다.

---

## 상세 설정 가이드

### 필요한 파일들

#### 1. `credentials.json` (필수)

**설정 방법**:
1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 새 프로젝트 생성 또는 기존 프로젝트 선택
3. "API 및 서비스" > "사용자 인증 정보"로 이동
4. "사용자 인증 정보 만들기" > "OAuth 클라이언트 ID" 선택
5. 애플리케이션 유형: "데스크톱 앱" 선택
6. 생성된 JSON 파일을 `credentials.json`으로 이름 변경하여 프로젝트 루트에 저장

**참고**: `credentials.json.example` 파일을 참고하세요. 실제 사용을 위해서는 Google Cloud Console에서 받은 파일로 교체해야 합니다.

#### 2. `token.json` (자동 생성)

`python quickstart.py` 실행 시 자동으로 생성됩니다. 한 번 생성하면 재사용 가능하며, 만료 시 자동으로 갱신됩니다.

#### 3. `companies.txt` (필수)

**형식**: 각 줄에 `회사명, 이메일주소` 형식으로 작성

**예시**:
```
네이버, naver@example.com
카카오, kakao@example.com
라인, line@example.com
```

**주의사항**:
- 회사명에 띄어쓰기가 있으면 자동으로 공백으로 변환됩니다
- 쉼표(`,`) 뒤 공백은 자동으로 제거됩니다

#### 4. `sponsorship-proposal-documents/mail.html` (필수)

메일 본문 HTML 템플릿 파일입니다.

**특수 변수**:
- `@회사@`: 회사 이름으로 자동 치환됩니다

**예시**:
```html
<p>안녕하세요, @회사@ 담당자님께</p>
<p>후원 요청 내용...</p>
```

#### 5. `sponsorship-proposal-documents/paper/main.tex` (필수)

LaTeX로 작성된 후원기획서 템플릿입니다.

**특수 변수**:
- `@회사@`: 회사 이름으로 자동 치환됩니다

**주의**: LaTeX 컴파일을 위해 `pdflatex`가 설치되어 있어야 합니다.

#### 6. 첨부 파일 (선택)

메일에 첨부할 파일들을 `attachments/` 디렉토리에 저장하세요:

- `SUAPC포스터초안.png` (이미지)
- `2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 홍보 자료 PPT.pdf` (PDF)
- `2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 후원기획서.pdf` (자동 생성)

첨부 파일은 `send_mail.py`의 `attachments` 리스트에서 관리됩니다.

---

## 전체 설정 순서

1. ✅ **의존성 설치**: `pip install -r requirements.txt`
2. ✅ **Gmail API 인증 설정**: `credentials.json` 준비 → `python quickstart.py` 실행
3. ✅ **템플릿 파일 준비**: `mail.html`, `main.tex` 작성
4. ✅ **회사 목록 준비**: `companies.txt` 작성
5. ✅ **첨부 파일 준비**: `attachments/` 디렉토리에 파일 저장 (선택)
6. ✅ **초기화**: `./install.sh` 실행
7. ✅ **메일 발송**: `python run-for-companies.py companies.txt`

---

## 주요 기능

- 📧 **Gmail API를 통한 대량 메일 자동 발송**
- 📄 **LaTeX를 사용한 회사별 맞춤 후원기획서 PDF 생성**
- 🎨 **HTML 템플릿을 사용한 개인화된 메일 본문**
- 📎 **첨부 파일 자동 첨부** (PDF, 이미지 등)

---

## 문제 해결

### LaTeX 컴파일 오류

**증상**: `pdflatex: command not found` 또는 컴파일 실패

**해결 방법**:
- macOS: `brew install basictex` 또는 `brew install mactex`
- Linux (Ubuntu/Debian): `sudo apt-get install texlive-latex-base`
- 설치 확인: `which pdflatex`

### Gmail API 오류

**증상**: 인증 실패 또는 권한 오류

**해결 방법**:
1. `credentials.json`이 올바른지 확인
2. `token.json`이 존재하는지 확인
3. [Google Cloud Console](https://console.cloud.google.com/)에서 Gmail API가 활성화되어 있는지 확인

### 파일 경로 오류

**증상**: `FileNotFoundError` 발생

**해결 방법**:
- 모든 필수 파일이 올바른 경로에 있는지 확인
- `sponsorship-proposal-documents/mail.html` 경로 확인 (⚠️ `mail/mail.html` 아님)
- `install.sh`를 실행했는지 확인

### 회사명 파싱 오류

**증상**: 회사명이나 이메일이 잘못 파싱됨

**해결 방법**:
- `companies.txt` 파일 형식 확인: `회사명, 이메일주소` (쉼표로 구분)
- 각 줄 끝의 공백이나 개행 문자는 자동으로 처리됩니다

---

## 파일 구조

```
sprayer/
├── attachments/                    # 첨부 파일 디렉토리
├── sponsorship-proposal-documents/
│   ├── mail.html                   # 메일 HTML 템플릿
│   └── paper/
│       └── main.tex                # LaTeX 템플릿
├── companies.txt                   # 회사 목록
├── credentials.json                # Gmail API 인증 정보
├── token.json                      # Gmail API 토큰 (자동 생성)
├── quickstart.py                   # Gmail API 인증 초기화
├── run-for-companies.py            # 메인 실행 스크립트
├── send_mail.py                    # 메일 발송 함수
├── build_tex.py                    # LaTeX PDF 생성 함수
└── utils.py                        # 유틸리티 함수
```

---

## 라이선스

MIT License

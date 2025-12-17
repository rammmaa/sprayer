# 후원 요청 메일 자동 발송 시스템

Gmail API를 사용하여 여러 회사에 후원 요청 메일을 자동으로 발송하는 Python 스크립트입니다.  
공통 후원기획서 PDF와 홍보 PPT를 첨부하고, HTML 메일 템플릿을 사용하여 회사명/담당자/이메일이 자동으로 치환된 메일을 발송합니다.

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

### 3. 회사 목록 CSV 준비

`companies.csv` 파일을 생성하고 **헤더를 포함한 CSV 형식**으로 작성합니다.

가능한 컬럼 이름(대소문자 무시, 일부 예시):
- **회사 이름**: `company`, `회사`, `기업명`
- **받는 이메일(회사 측)**: `to`, `to_email`, `company_email`, `회사이메일`, `기업이메일`, `email`, `메일`, `이메일`  
  (여러 개일 경우 쉼표(,)로 구분하면, 모든 주소로 메일이 발송됩니다.)
- **우리 쪽 담당자 이름**: `person`, `담당자`, `담당자이름`, `담당자명`
- **우리 쪽 담당자 이메일**: `person_email`, `담당자이메일`, `담당자메일`

**예시 (`companies.csv`)**:

```csv
company,to,person,person_email
네이버,naver@example.com,홍길동,hong@our-org.com
카카오,kakao@example.com,김영희,kim@our-org.com
```

### 4. 메일 발송

```bash
python run-for-companies.py companies.csv
```

완료! 각 회사별로 **공통 후원기획서 PDF + 홍보 PPT**가 첨부되고,  
회사명/담당자/이메일이 치환된 메일이 자동으로 발송됩니다.

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

#### 3. `companies.csv` (필수)

**형식**: 헤더 포함 CSV 파일

예를 들어:

```csv
company,to,person,person_email
네이버,naver@example.com,홍길동,hong@our-org.com
카카오,kakao@example.com,김영희,kim@our-org.com
라인,line@example.com,이철수,lee@our-org.com
```

#### 4. `sponsorship-proposal-documents/mail.html` (필수)

메일 본문 HTML 템플릿 파일입니다.

**특수 변수 (자동 치환)**:
- `@회사@`   → 회사 이름
- `@담당자@` → 담당자 이름
- `@이메일@` → 담당자 이메일

**예시**:
```html
<p>안녕하세요, @회사@ @담당자@님께</p>
<p>후원 관련하여 메일드립니다. 회신은 @이메일@ 로 부탁드립니다.</p>
```

#### 5. 첨부 파일

메일에 첨부할 파일들을 `attachments/` 디렉토리에 저장하세요:

- `2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 홍보 자료 PPT.pdf` (PDF, 공통 첨부)
- `ICPC Sinchon 후원 기획서.pdf` (공통 후원기획서, 담당자 미지정일 때 사용)
- `ICPC Sinchon 후원 기획서_홍길동.pdf`, `ICPC Sinchon 후원 기획서_김영희.pdf` 처럼  
  `ICPC Sinchon 후원 기획서_담당자이름.pdf` 형식으로 우리 쪽 담당자별 후원기획서를 둘 수 있습니다.

**주의 (메일에 보이는 파일 이름)**  
- 실제 파일 이름이 `ICPC Sinchon 후원 기획서_홍길동.pdf` 여도,  
  메일에 첨부될 때 보이는 이름은 자동으로 **`ICPC Sinchon 후원 기획서.pdf`** 로 바뀝니다.  
  (언더바 `_` 뒤의 담당자 이름은 표시용 파일명에서 제거됩니다.)

---

## 전체 설정 순서

1. ✅ **의존성 설치**: `pip install -r requirements.txt`
2. ✅ **Gmail API 인증 설정**: `credentials.json` 준비 → `python quickstart.py` 실행
3. ✅ **템플릿 파일 준비**: `mail.html` 작성 (`@회사@`, `@담당자@`, `@이메일@` 사용)
4. ✅ **회사 목록 준비**: `companies.csv` 작성
5. ✅ **첨부 파일 준비**: `attachments/` 디렉토리에 홍보 PPT 저장, 프로젝트 루트에 공통 후원기획서 PDF 저장
6. ✅ **초기화**: `./install.sh` 실행
7. ✅ **메일 발송**: `python run-for-companies.py companies.csv`

---

## 주요 기능

- 📧 **Gmail API를 통한 대량 메일 자동 발송**
- 🎨 **HTML 템플릿을 사용한 개인화된 메일 본문 (회사/담당자/이메일 자동 치환)**
- 📎 **공통 후원기획서 PDF 및 홍보 PPT 자동 첨부**

---

## 문제 해결

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

### 회사 정보 파싱 오류

**증상**: 회사명/담당자/이메일이 잘못 파싱됨

**해결 방법**:
- `companies.csv` 파일 형식 확인: 헤더 포함 CSV인지, 회사/담당자/이메일 컬럼 이름이 올바른지 확인
- 각 셀 앞뒤의 공백은 자동으로 제거됩니다

---

## 파일 구조

```
sprayer/
├── attachments/                    # 첨부 파일 디렉토리
├── sponsorship-proposal-documents/
│   └── mail.html                   # 메일 HTML 템플릿
├── companies.csv                   # 회사 목록 (CSV)
├── credentials.json                # Gmail API 인증 정보
├── token.json                      # Gmail API 토큰 (자동 생성)
├── quickstart.py                   # Gmail API 인증 초기화
├── run-for-companies.py            # 메인 실행 스크립트
├── send_mail.py                    # 메일 발송 함수
├── build_tex.py                    # (선택) LaTeX PDF 생성 함수
└── utils.py                        # 유틸리티 함수
```

---

## 라이선스

MIT License

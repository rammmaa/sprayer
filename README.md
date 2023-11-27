# How to Use
1. [Gmail Python Quickstart guide](https://developers.google.com/gmail/api/quickstart/python)를 따라하고, 마지막 `quickstart.py`에서 `SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]`로 변경하여 `token.json`을 만들고 이 README가 있는 디렉토리에 둡니다.
2. 각 줄이 `회사이름,회사메일주소`로 구성된 파일 companies(이름 자유)를 만듭니다. 회사 이름에 띄어쓰기는 없어야 하며, 띄어쓰기가 필요할 경우 '-'로 대체합니다. '-'가 필요할 경우, '\-'로 대체합니다.
3. `./install.sh`
4. `python run-for-companies.py companies`

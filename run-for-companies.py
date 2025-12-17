#!/usr/bin/python

import sys
import csv

import send_mail


# 모든 회사에 공통으로 기본 첨부할 후원기획서 PDF 경로
PROPOSAL_PDF_PATH = "attachments/ICPC Sinchon 후원 기획서.pdf"

# 우리 쪽 담당자별 후원기획서 파일 이름 포맷
# 실제 파일명 예시:
# - attachments/ICPC Sinchon 후원 기획서_홍길동.pdf
# - attachments/ICPC Sinchon 후원 기획서_김영희.pdf
PERSON_PROPOSAL_TEMPLATE = "attachments/ICPC Sinchon 후원 기획서_{person}.pdf"


def extract_field(row, *keys):
    """row(dict)에서 주어진 키들 중 처음으로 발견되는 값을 반환합니다."""
    for k in keys:
        if k in row and row[k]:
            return row[k].strip()
    return ""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} COMPANIES_CSV_FILE")
        sys.exit(1)

    csv_path = sys.argv[1]

    with open(csv_path, "r", encoding="utf8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 회사명
            company = extract_field(row, "company", "회사", "기업명")

            # 받는 사람(회사 측 이메일, 여러 개면 쉼표로 구분)
            to_email_raw = extract_field(
                row,
                "to",
                "to_email",
                "company_email",
                "회사이메일",
                "기업이메일",
                "email",
                "메일",
                "이메일",
            )

            # 우리 쪽 홍보 담당자 이름 / 이메일
            our_person = extract_field(row, "person", "담당자", "담당자이름", "담당자명")
            our_person_email = extract_field(
                row,
                "person_email",
                "담당자이메일",
                "담당자메일",
                "담당자 email",
            )

            if not company or not to_email_raw:
                print("경고: company 또는 받는 이메일(to_email) 정보가 없어 건너뜁니다. row =", row)
                continue

            # 이메일 여러 개일 경우 쉼표(,)로 구분해서 모두 발송
            to_emails = [e.strip() for e in to_email_raw.split(",") if e.strip()]

            # 담당자 이름에 따라 다른 후원기획서 PDF 경로를 포맷으로 생성
            if our_person:
                proposal_pdf_path = PERSON_PROPOSAL_TEMPLATE.format(person=our_person)
            else:
                proposal_pdf_path = PROPOSAL_PDF_PATH

            for to_email in to_emails:
                print(
                    f"Processing company={company}, "
                    f"to_email={to_email}, our_person={our_person}, our_person_email={our_person_email}, "
                    f"proposal_pdf={proposal_pdf_path}"
                )

                send_mail.run(
                    to_email,
                    company,
                    our_person,
                    our_person_email,
                    proposal_pdf_path,
                )


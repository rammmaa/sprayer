#!/usr/bin/python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase

import base64

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import typing

import sys

from utils import change_name
import os.path

import socket

socket.setdefaulttimeout(4000)  # without this, we can't send big attachments.

SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]


def send_mail(
    to: str,
    cc: typing.Optional[str],
    content: str,
    attachments_names: typing.List[typing.Tuple[str, str, str]],
) -> None:
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("gmail", "v1", credentials=creds)

    msg = MIMEMultipart("Mixed")
    msg["subject"] = "[후원 문의] 신촌지역 대학교 프로그래밍 동아리 연합 대회 후원 요청서"
    msg["From"] = "icpc.sinchon@gmail.com"
    msg["To"] = to
    if cc:
        msg["Cc"] = cc
    part = MIMEText(content, 'html')
    msg.attach(part)

    for file, maintype, subtype in attachments_names:
        if not os.path.exists(file):
            print(f"Warning: Attachment file not found: {file}, skipping...")
            continue
        part = MIMEBase(maintype, subtype)
        with open(file, "rb") as f:
            part = MIMEApplication(f.read(), _subtype=subtype)

        # 첨부파일 실제 이름은 디스크상 파일명을 따르되,
        # 메일에 표시되는 이름에서는 "_담당자" 부분을 잘라냅니다.
        # 예) "ICPC Sinchon 후원 기획서_홍길동.pdf" → "ICPC Sinchon 후원 기획서.pdf"
        basename = os.path.basename(file)
        root, ext = os.path.splitext(basename)
        if "_" in root:
            root = root.split("_")[0]
        display_name = root + ext

        part.add_header(
            'Content-Disposition',
            'attachment',
            filename=display_name,
        )
        msg.attach(part)

    encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf8')
    create_message = {"raw": encoded_message}
    print("message generated")
    service.users().messages().send(userId="me", body=create_message).execute()
    print("sended")


def run(
    to: str,
    company: str,
    our_person: str,
    our_person_email: str,
    proposal_pdf_path: str,
):
    """
    메일 템플릿에 회사명/담당자 이름/이메일을 치환하고,
    포스터 없이 홍보 PPT와 회사별 후원기획서 PDF만 첨부하여 발송합니다.
    """
    content = ""
    with open("sponsorship-proposal-documents/mail.html", "r", encoding="utf8") as f:
        for line in f.readlines():
            # @회사@, @담당자@, @이메일@ 플레이스홀더 치환
            # - @회사@: 메일을 받는 회사 이름
            # - @담당자@: 우리 쪽에서 홍보를 담당하는 사람 이름
            # - @이메일@: 우리 쪽 담당자 이메일 (회신 받을 주소)
            line = line.replace("@회사@", change_name(company))
            line = line.replace("@담당자@", our_person or "")
            line = line.replace("@이메일@", our_person_email or "")
            content += line

    attachments = [
        # 대회 포스터는 더 이상 첨부하지 않음
        ("attachments/2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 홍보 자료 PPT.pdf", "application", "pdf"),
        (proposal_pdf_path, "application", "pdf"),
    ]

    print(
        "Sending mail to:", to,
        "company:", company,
        "our_person:", our_person,
        "our_person_email:", our_person_email,
    )
    # 회사로는 To, 우리 담당자 이메일은 Cc 로 전송
    send_mail(to, our_person_email, content, attachments)


if __name__ == "__main__":
    # 단독 실행 시:
    # python send_mail.py 받는이메일 회사명 우리담당자이름 우리담당자이메일 후원기획서PDF경로
    to = sys.argv[1]
    company = sys.argv[2]
    our_person = sys.argv[3]
    our_person_email = sys.argv[4]
    proposal_pdf_path = sys.argv[5]
    run(to, company, our_person, our_person_email, proposal_pdf_path)

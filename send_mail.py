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
socket.setdefaulttimeout(4000) # without this, we can't send big attachments.

SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

def send_mail(to:str, content:str, attachments_names:typing.List[typing.Tuple[str, str, str]]) -> None:
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("gmail", "v1", credentials=creds)

    msg = MIMEMultipart("Mixed")
    msg["subject"] = "[후원 문의] 신촌지역 대학교 프로그래밍 동아리 연합 대회 후원 요청서"
    msg["From"] = "icpc.sinchon@gmail.com"
    msg["To"] = to
    part = MIMEText(content, 'html')
    msg.attach(part)

    for file, maintype, subtype in attachments_names:
        if not os.path.exists(file):
            print(f"Warning: Attachment file not found: {file}, skipping...")
            continue
        part = MIMEBase(maintype, subtype)
        with open(file, "rb") as f:
            part = MIMEApplication(f.read(), _subtype=subtype)
        part.add_header('Content-Disposition','attachment',filename=os.path.basename(file))
        msg.attach(part)

    encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf8')
    create_message = {"raw": encoded_message}
    print("message generated")
    service.users().messages().send(userId="me", body=create_message).execute()
    print("sended")

def run(to, company):
    content=""
    with open("sponsorship-proposal-documents/mail.html", "r", encoding="utf8") as f:
        for line in f.readlines():
            content += line.replace("@회사@", change_name(company))

    attachments = [
        ("attachments/SUAPC포스터초안.png", "image", "png"),
        ("attachments/2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 홍보 자료 PPT.pdf", "application", "pdf"),
        ("2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 후원기획서.pdf", "application", "pdf")
    ]

    print("Sending mail to:", to)
    send_mail(to, content, attachments)

if __name__ == "__main__":
    to = sys.argv[1]
    company = sys.argv[2]
    run(to, company)

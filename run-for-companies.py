#!/usr/bin/python

import sys

import build_tex
import send_mail

if __name__ == "__main__":
    with open(sys.argv[1], 'r', encoding='utf8') as f:
        for l in f.readlines():
            l = l.strip()  # 개행 문자와 공백 제거
            if not l:  # 빈 줄 건너뛰기
                continue
            com, mail = [part.strip() for part in l.split(',', 1)]  # 공백 제거 및 최대 1번만 분할
            build_tex.run("sponsorship-proposal-documents/paper/main.tex", com)
            send_mail.run(mail, com)


#!/usr/bin/python

import sys
import subprocess

import build_tex
import send_mail

if __name__ == "__main__":
    with open(sys.argv[1], 'r', encoding='utf8') as f:
        for l in f.readlines():
            com, mail = l.split(',')
            build_tex.run("sponsorship-proposal-documents/paper/main.tex", com)
            send_mail.run(mail, com)


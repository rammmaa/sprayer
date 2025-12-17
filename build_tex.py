#!/usr/bin/python
import sys
import os.path
import subprocess

from utils import change_name


def run(tex_file, company_name):
    """
    회사명에 맞춰 tex 파일을 생성하고, 해당 회사용 후원기획서 PDF를 만든 뒤
    생성된 PDF 파일 경로를 반환합니다.
    """
    tmp_tex_file = "2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 후원기획서.tex"
    with open(tex_file, 'r') as f:
        a = f.readlines()
        for i, l in enumerate(a):
            a[i] = l.replace('@회사@', change_name(company_name))

    with open(tmp_tex_file, 'w') as g:
        for i in a:
            g.write(i)

    subprocess.run(["xelatex", tmp_tex_file], stdout=subprocess.DEVNULL)
    pdf_file = os.path.splitext(tmp_tex_file)[0] + ".pdf"
    print(f"{company_name}: tex & pdf file generated -> {pdf_file}")
    return pdf_file

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} TEX_FILE COMPANY_NAME")
        sys.exit()

    tex_file = sys.argv[1]
    company_name = sys.argv[2]
    run(tex_file, company_name)

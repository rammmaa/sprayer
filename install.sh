#!/usr/bin/env sh
mkdir attachments
cp sponsorship-proposal-documents/res/pt-final.pdf "./attachments/2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 홍보 자료 PPT.pdf" 2>/dev/null || cp sponsorship-proposal-documents/ICPCSinchonPPT.pdf "./attachments/2026 겨울 신촌지역 대학교 프로그래밍 동아리 연합 홍보 자료 PPT.pdf" 2>/dev/null || echo "Warning: PDF file not found, please add it manually"

cp sponsorship-proposal-documents/paper/* .

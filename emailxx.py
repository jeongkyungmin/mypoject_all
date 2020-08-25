import smtplib
from emailxx.mime.text import MIMEText

# 메일 내용 작성
title = '[20200812_오늘의 코딩 공부].'
content = '[Python] 업무 자동화 - Naver 메일 보내기.'
msg_from = "pasco78@naver.com" # 보내는 사람 이메일 주소
msg_to = "pasco78@naver.com" # 받는 사람 이메일 주소

# 메일 객체 생성 : 메시지 내용에는 한글이 들어가기 때문에 한글을 지원하는 문자 체계인 UTF-8을 명시해줍니다.
msg = MIMEText(_text = content, _charset = "utf-8") # 메일 내용

msg['Subject'] = title  # 메일 제목
msg['From'] = msg_from   # 보내는 메일
msg['To'] = msg_to       # 받는 메일

print(msg.as_string()) # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.

SMTP_SERVER = 'smtp.naver.com'
SMTP_USER_ID = "pasco78@naver.com"  # 송신자계정
SMTP_USER_PW = "jeong14551458"  # 수신 메일
SMTP_PORT = 465

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    # 로그인
    server.login(SMTP_USER_ID, SMTP_USER_PW)

    # 로그인 된 서버에 이메일 전송
    response = server.sendmail(msg_from, msg_to, msg.as_string())

    # 이메일을 성공적으로 보내면 결과는 {}
    if not response:
        print('이메일을 성공적으로 보냈습니다.')
    else:
        print(response)

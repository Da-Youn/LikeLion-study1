import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# smtp 서버 연결하기, 서버에 이메일 로그인하게
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("###@gmail.com", "######")

# 유효성 검사하기


def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


# 함수 호출, 이메일에 내용 담기
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

# 제목, 발신자, 수신자 설정하기
message["Subject"] = "이것은 제목입니다."
message["From"] = "###@gmail.com"
message["To"] = "###@gmail.com"

# 사진 파일 읽어오기
with open("codelion.png", "rb") as image:
    image_file = image.read()

# 파일 타입 확인, 메일에 사진 담기
image_type = imghdr.what('codelion', image_file)
message.add_attachment(image_file, maintype='image', subtype=image_type)

# 메일을 보내는 sendEmail 함수를 호출해서 실행해보기
sendEmail("###gmailcom")
smtp.quit()

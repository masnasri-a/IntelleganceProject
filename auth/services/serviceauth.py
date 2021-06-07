import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class auth():
    def sendMail(mail:str,token:str):
        subject = "Test Email"
        smtp_server = "smtp.gmail.com"
        port = 25
        sender_email = "nasriblog123@gmail.com"
        pass_email = "putramunandirin"

        msg = "activate your acoount with this link "+token+" . "

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = mail
        message["Subject"] = subject
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP('localhost') as server:
                server.login(sender_email,pass_email)
                server.sendmail(sender_email,mail,msg)
        except Exception as e:
            print(e)
        finally:
            server.quit()
        return
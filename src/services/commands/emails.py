from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

def sendEmail():
    whither = input("DESTINO: ")
    title = input("TITULO: ")
    contents = input("CONTEUDO: ")
    msg = MIMEMultipart()
    msg['from'] = 'email'
    msg['to'] = whither
    msg['subject'] = title

    body = MIMEText(contents)
    msg.attach(body)

    with smtplib.SMTP(host='host', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('email', 'password')
        smtp.send_message(msg)
        print("Email enviado com sucesso!")
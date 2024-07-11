import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "lolqijezur5xrnzt@ethereal.email"
    login = "lolqijezur5xrnzt@ethereal.email"
    password = "ZXkNAyTNwRHSU3JbE6"

    msg = MIMEMultipart()
    msg["from"] = "confirmacao_viagem_nlw@email.com"
    msg["to"] = ', '.join(to_addrs)

    msg["Subject"] = "Confirmação de Viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()
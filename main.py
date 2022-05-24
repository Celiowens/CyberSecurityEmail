import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.co', 25)

server.ehlo()

server.login('cybersectest@gmail.com', 'Comptia123')

msg = MIMEMultipart()
msg['From'] = 'Christian Owens'
msg['To'] = 'malu333221@gmail.com'
msg['Subject'] = 'Just a Text'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'DogImage.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename= {filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('cybersectest@gmail.com', 'malu333221@gmail.com', text)

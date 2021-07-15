import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time

df = pd.read_csv('friends.csv')

birthdays = list(df['Birthday'])
names = list(df['Name'])
emails = list(df['Email'])
dialoges = list(df['Dialogue'])

a = 0
name_dict = {}
while a <= (len(birthdays)-1):
	name_dict[birthdays[a]] = names[a]
	a += 1

b = 0
email_dict = {}
while b <= (len(birthdays)-1):
	email_dict[birthdays[b]] = emails[b]
	b += 1

c = 0
dialogue_dict = {}
while c <= (len(birthdays)-1):
	dialogue_dict[birthdays[c]] = dialoges[c]
	c += 1

def wish(name, email, dialogue):
	try:
		content = dialogue
		subject = f"Happy Birthday {name}"
		email_user = 'prameyamohanty14@gmail.com'
		email_password = 'Prameya@1425'
		email_send = email
		msg = MIMEMultipart()
		msg['From'] = email_user
		msg['To'] = email_send
		msg['Subject'] = subject
		body = content
		msg.attach(MIMEText(body, 'plain'))
		filename = "D:\\Programming\\Automatic Birthday Wisher using Python\\attachment.png"
		attachment = open(filename, 'rb')
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(attachment.read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition',
                        "attachment; filename= " + filename)
		msg.attach(part)
		text = msg.as_string()
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(email_user, email_password)
		server.sendmail(email_user, email_send, text)
		server.quit()
		print("E-Mail has been sent successfully!")
	except Exception as e:
		print(f"An error occured which is printed below:\n{e}")

while True:
	date_today = datetime.now().strftime('%d-%b')	
	for date in birthdays:
		if date == date_today:
			name = name_dict[date]
			email = email_dict[date]
			dialogue = dialogue_dict[date]
			wish(name, email, dialogue)
			time.sleep(86400)
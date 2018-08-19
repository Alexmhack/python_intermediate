from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = "ghost@protocol.com"
password = "fallout"

from_email = username
to_list = [username]

email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()

try:
	email_conn.login(username, password)
except SMTPAuthenticationError as e:
	print('Failed to login')
	print(e)

try:
	email_conn.sendmail(from_email, to_list, "Hello there, we are from python")
except SMTPException as e:
	print('Failed to send email')
	print(e)

email_conn.quit()

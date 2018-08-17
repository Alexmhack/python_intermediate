from templates import render_html
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "78030psg@gmail.com"
password = "thisisauselessemail"

from_email = username
to_list = [username]

try:
	email_conn = SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()

	message = MIMEMultipart("alternative")
	message['Subject'] = "Hello there"
	message['From'] = 'Python Developer'
	message['To'] = to_list[0]

	html = MIMEText(render_html, 'html')
	message.attach(html)

	email_conn.login(username, password)
	email_conn.sendmail(from_email, to_list, message.as_string())
	email_conn.quit()
except SMTPException as e:
	print(e)

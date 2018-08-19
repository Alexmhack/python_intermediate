from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "ghostg@protocol.com"
password = "fallout"

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

	plain_text = "Testing plain message"
	html_text = """
	<html>
		<head></head>
		<body>
			<h2>Hello Sir</h2>
			<p>This is me, <a href="https://python.org">python!</a></p>
		</body>
	</html>
	"""

	part_1 = MIMEText(plain_text, 'plain')
	part_2 = MIMEText(html_text, 'html')

	message.attach(part_1)
	message.attach(part_2)

	email_conn.login(username, password)
	email_conn.sendmail(from_email, to_list, message.as_string())
	email_conn.quit()
except SMTPException as e:
	print(e)

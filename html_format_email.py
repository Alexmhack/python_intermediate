from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "78030psg@gmail.com"
password = "thisisauselessemail"

from_email = username
to_list = [username]

email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()

message = MIMEMultipart("alternative")
message['Subject'] = "Hello there"
message['From'] = from_email
message['To'] = to_email

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
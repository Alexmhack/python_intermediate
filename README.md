# python_intermediate
using intermediate level python for solving simple and complex tasks

# Send emails with python
Python has built-in smtplib module for sending emails using the host and port from many service 
providers out there. We have used gmail host which for smtp is

```
host = 'smtp.gmail.com'
port = 587
```

port that we use with gmail emailing service is 587 which required a gmail account.

```
username = 'any-gmail-account'
password = 'password-for-account'
from_email = username
to_email = ['example1@gmail.com', 'example2@gmail.com', 'example3@gmail.com']
```

the above are the credentials we can use for sending email, *the email we send email from should have
a gmail feature enabled, 'let third party apps use the account'* or the emails won't send

```
email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
```

For connecting to the gmail service we need to start a connection using the SMTP class and starttls 
is for securing our connection to the server. For logging into the gmail service with our username and
password we use,

```
email_conn.login(username, password)
email_conn.sendmail(from_email, to_email, 'message')
```

Sending email is as simple as using the sendmail method with three arguemnts
*Don't forget to close our connection after using the service*

```
email_conn.quit()
```

# Send HTML format email
For sending html formatted email we need to use the MIMEMultipart and MIMEText from email.mime and
create html message and attach it to the email message, then send like the usual sendmail function
but replacing the message with our email message.

```
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = MIMEMultipart("alternative")
message['Subject'] = "Hello there"
message['From'] = from_email
message['To'] = to_list[0]

part_2 = MIMEText(html_text, 'html')
message.attach(part_2)
email_conn.sendmail(from_email, to_list, message.as_string())
```

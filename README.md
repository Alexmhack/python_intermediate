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


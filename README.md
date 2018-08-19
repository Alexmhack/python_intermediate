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

We create a new file for rendering context in our template, there is a seperate function for each
process, we get the template path from templates folder that has our email template file

# Read CSV Files with Python
Python module for handling csv files and data is "csv"

```
import csv
```

To create a new csv file we can use the python in-built *with* command with *open* method

```
with open('data.csv', 'w+') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Title', 'Description'])
	writer.writerow(['New row', 'Awesome description for row'])	
```

if file data.csv does not exist then *open* creates one and with opens the file as *csvfile
*. csv has writer function which takes in a csv file object and creates a writer for 
csvfile. Now using the writerow functions we can write rows in our csv file.

**W+** in open() means we are opening this file in write mode, which means everything we do
with csv file will be written into it and existing content of the file will be erased.

**Appending CSV data**

```
import csv

with open('data.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Append row', 'append description', 'append summary'])
```

**Reading CSV data**

```
import csv

with open('data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)
```

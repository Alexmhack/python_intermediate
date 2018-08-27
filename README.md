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

# Flask
Python supports backend web development using the module Flask. There are more options like
Django but Flask lets you get started in a lot less amount of time.

We are going to use the SQL database with flask and so we will install the flask_sqlalchemy
package using pip

**command prompt**
```
pip install flask_sqlalchemy
```

We import SQLAlchemy from flask_sqlalchemy and create an instance of it

**python_flask/models.py**
```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

Next we create a model just like we do in Django using 

```
from django import models

class SampleModel(models.Model):
	...
```

We do the same thing in Flask using the instance we just created and name our model Flight
which has four fields namely id, origin, destination, duration which ofcourse matches with
the properties of a flight

```
class Flight(db.Model):
	__tablename__ = "flights"
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=False)
	destination = db.Column(db.String, nullable=False)
	duration = db.Column(db.Integer, nullable=False)
```

**Passenger model**

Every flight has to have passengers in it so we create another model or another table which
will separately be for passengers. *In databases and ORM we work on this principle that every
model has its own table*. Here we need to connect the tables passengers and flights with some
property or basis so that we can say A passenger is travelling with F flight. We connect the 
databases using foreignkey and so each passenger has an id, name, and flight id with which 
the passenger is travelling.

```
class Passenger(db.Model):
	__tablename__ = "passengers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
```

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

if file data.csv does not exist then *open* creates one and with opens the file as *csvfile*
. csv has writer function which takes in a csv file object and creates a writer for 
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

There is also *DictReader* and *DictWriter* in csv module for reading and writing dict
data, there is very less difference in csv.reader and csv.DictReader 

The output of csv.reader(csvfile) will look something like this

```
['Title', 'Description', 'Summary']
['New row', 'Awesome description for row', 'Awesome summary']
['Append row', 'append description', 'append summary']
['Row3', 'Row3', 'Row3']
```

Whereas the output of csv.DictReader is a more detailed one,

```
OrderedDict([('Title', 'New row'), ('Description', 'Awesome description for row'), ('Summary', 'Awesome summary')])
OrderedDict([('Title', 'Append row'), ('Description', 'append description'), ('Summary', 'append summary')])
OrderedDict([('Title', 'Row3'), ('Description', 'Row3'), ('Summary', 'Row3')])
```

The tuples inside the lists say > (*row heading*, *row data*)

**csv.DictWriter and csv.writer**

*csv.writer* has this simple look and feel
```
...
	writer = csv.writer(csvfile)
	writer.writerow(['Append row', 'append description', 'append summary'])
```


*csv.DictWriter* will be more detailed data filling way, which sometimes is very useful 
and powerful way of writing data with python csv module
```
...
	fieldnames = ['Title', 'Description', 'Summary']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({'Title': 'Row3', 'Description': 'Row3', 'Summary': 'Row3'})
```

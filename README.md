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

After creating the models all we need to do is import our models in another file and connect
to our postgresql database and run 

**python_flask/create.py**
```
def main():
	db.create_all()
```

# API Request
Python has built in module for url requests, responses, json data etc. Import the module 
using ```improt requests```. *requests* support many methods like GET, POST, PUT, DELETE etc.

**python_requests/fizer_api.py**
```
import requests

res = requests.get("http://api.fixer.io/latest/?base=USD&symbols=EUR")
print(res.text)
```

using .text on response from the get method to an url will print the response send by the
server on accessing the url, if the data send by server is in json format we use .json()

**python_requests/fizer_api.py**
```
data = res.json()
print(data)
```

**NOTE:** fixer api is not supporting requests through our method, read the fixer docs for more info

To get the status_code send by the server use .status_code

```
res = requests.get("http://api.fixer.io/latest/?base=USD&symbols=EUR")
print(res.status_code)
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

For writing your fieldnames at the top of csv file and giving the columns heading we can use
the csv method ```writer.writeheader()```

**Function for appending data**
We have created a file with two functions namely *get_length* for getting the total length 
of the csv file or for getting the last row of file on which data exists, and the other 
function is *append_data* that uses the same logic as we used to append data in csv file but
just takes in some parameters like the path of the file, name for the name and email for 
their columns. We give each row and id using the function *get_length*.

**There are some new features that we used here:**

1. Writing heading for columns using ```writer.writeheader()```
2. Writing the headers only when the file is empty
3. Getting the length of csv file using ```get_length(file_path)``` fucntion
4. Checking if length is one then giving an id of *1*
5. Writing rows by passing values from arguments
6. Solve the problem of new line on each append using ```newline=''``` while opening file

	**python_csv/append_function.py**
	```
	with open('data.csv', 'a', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		if next_id == 0:
			writer.writeheader()
			next_id = 1		
	```

**Editing CSV data using temporary file**

In this section we are going to create a temporary file while our code is running and 
edit our changes first in the temporary file so as to not disturb or risk our original
CSV file and then when our editing is done with the CSV data inside the temporary file
we are going to merge the temporary file with the original CSV file.

For our purpose of creating a temp file, python has built-in modules for that.

**python_csv/editing_csv_data.py**
```
import csv
import shutil
from tempfile import NamedTemporaryFile
```

the tempfile module lets us create a named temporary file with a name that shows up in 
the directory unlike the tempfile.TemporaryFile and these files are deleted if closed 
```NamedTemporaryFile(delete=True)``` which is by default, we can set delete
to False for keeping the file.

**python_csv/editing_csv_data.py**
```
temp_file = NamedTemporaryFile(delete=False)
```

We can open this file just like we open ordinary files using the ```with open()```.
For more checkout the [temfile](https://docs.python.org/3/library/tempfile.html) docs.

Then again we just create reader and writer using csv 

**python_csv/editing_csv_data.py**
```
with open(FILE_NAME, 'wb', , newline='') as csvfile, temp_file:
	reader = csv.DictReader(csvfile)
	fieldnames = ['id', 'name', 'email', 'amount', 'sent']
	writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
```

Notice that we read the original file and we write to the temporary file

**NOTE:** [tempfile](https://docs.python.org/3/library/tempfile.html) module in python creates a temporary file which gets stored in the
temp folder of windows ```C:/Windows/Temp``` The file is not deleted if delete=False
is provided. Temp file requires the data to be inserted in bytes format not string
and csv.writer or csv.DictWriter writes data in files in string format which
raises an error ```TypeError: a bytes-like object is required, not 'str'```

When you run shutil.move for the temp file that will raise another error ```Permis
sionDeniedError [error 13]``` because for accessing temp file we need admin 
access.

Run the command on a admin cmd or refer to stackoverflow for this [problem](https://stackoverflow.com/questions/44044298/permissionerror-errno-13-permission-denied-c-program-files-python35-lib)

**CORRECTIONS COMING SOON**

**Finding specific row**

So far we have been reading, writing, editing, appending data but now we will be 
writing simple ```if else``` logic for finding a specific row or we can say a specific
user in context to our data in **data.csv** file.

For that we will be simply iterating over the whole data.csv file and checking if the
row contains the data we are looking for, if yes then we fetch the whole row else
print not found error

**python_csv/read_specific_data.py**
```
import csv

def find_user(user_id=None, user_email=None):
	with open('data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			row_id = int(row.get("id"))
			unknown_id = None
			unknown_email = None
			found_email = None
```

In the above code there is nothing new, we just put all our opening iterating logic 
inside a function so using this we can call our function with id of any user and
the function will try to find it.

Notice all the None values, they are referenced before hand in every row of the file
because we will be using them for checking purposes in the end of the function

**python_csv/read_specific_data.py**
```
	.....
			if user_id is not None:
				if user_email is not None:
					if int(user_id) == row_id:
						if user_email == row.get("email"):
							return row
						else:
							unknown_email = user_email
							found_id = user_id
							break
```

We have used a very simple if else logic which says that inside our function if we have
passed in the argument user_id i.e. if user_id is been passed then check if user_email
has also been passed.

If both of them have been passed then we simply check the user_id first inside the 
data.csv file by converting the uesr_id from data.csv file into **int** because it
comes in as a **str**.

If user_id is found then check if user_email exists if yes then return the whole row
if user_email is not found then in the else clause we set **unknown_email** which
we defined as a ```None``` value at the beginning of ```for``` loop to our 
**user_email** and since we found our user_id we set ```found_id = user_id```

We added a break in else statement because we don't wanna be running the after logic 
and simply pass on to next row in file.


**python_csv/read_specific_data.py**
```
		...
			if user_id is not None:
				if user_email is not None:
					if int(user_id) == row_id:
						if user_email == row.get("email"):
							return row
						else:
							unknown_email = user_email
							found_id = user_id
							break
					else:
						unknown_id = int(user_id)
						if user_email == row.get("email"):
							found_email = user_email
						break
				else:
					if int(user_id) == row_id:
							return row
					else:
						unknown_id = int(user_id)
						break
```

In the remaining logic we check if the user_id is not equal to row_id then we step into
the else statement which simply sets the ```unknown_id = user_email``` so that we can 
use it at last and also we do a simple checking of **user_email** so that we can say
if id and email both are not found or either one of them is found

**Don't worry if you don't understand the logic now, read the code a couple of times
and everything will start relating to each other.**

**python_csv/read_specific_data.py**
```
def find_user(user_id=None, user_email=None):
	with open('data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			row_id = int(row.get("id"))
			unknown_id = None
			unknown_email = None
			found_email = None
			if user_id is not None:
				if user_email is not None:
					if int(user_id) == row_id:
						if user_email == row.get("email"):
							return row
						else:
							unknown_email = user_email
							found_id = user_id
							break
					else:
						unknown_id = int(user_id)
						if user_email == row.get("email"):
							found_email = user_email
						break
				else:
					if int(user_id) == row_id:
							return row
					else:
						unknown_id = int(user_id)
						break

		if unknown_email and found_id is not None:
			return f"USER EMAIL: {unknown_email} NOT FOUND BUT USER ID: {found_id}"
		if unknown_id is not None:
			if found_email:
				return f"USER ID: {unknown_id} NOT FOUND BUT FOUND EMAIL: {found_email}"
			return f"USER ID: {unknown_id} AND USER EMAIL: {user_email} NOT FOUND"
	return None
```

If nothing gets returned then our last two if statements run and print the not found
with details

# Command Line Integration
In this part of the python intermediate tutorial series we are going to create a command line
integrated app using our python_csv folder and all the files in it.

**NOTE:** File named as main.py are __main__.py, due to some issues with github 
README.md representation __main__.py is not showing up

We will create a folder for this purpose and another folder inside that in which all our files
will be moved that we created in CSV Tutorial, to keep simple for us to type in the command
prompt to trigger code we are gonna keep the name of the main folder simple.

Name the folder **integrate**. Your project structure should look like

```
Folder PATH listing for volume Windows
Volume serial number is ****-****
C:.
├───integrate
│   └───python_csv
├───python_csv
├───python_emailing
├───python_flask
│   └───__pycache__
├───python_requests
├───templates
└───__pycache__
```

You can look at your project tree from the cmd using, all the folders inside the current 
folder will appear in a tree format

**cmd**
```
...\python_intermediate> tree
```

Create a new file named __init__.py inside the **integrate** folder, to see how python module commands works we have to know what runs them. Now run ```python integrate``` from the parent folder where integrate folder lies.

**cmd**
```
...\python_intermediate> python integrate

... can't find '__main__' module in 'integrate'
```

Python says it cannot find a main module so create one inside integrate folder 

If you have set sublime text to open from **cmd** with subl command then enter the below
code or just create a new file in the integrate folder and name it __main__.py

**cmd**
```
...\python_intermediate> subl __main__.py
```

Now run the ```python integrate``` command again. No results because we have no code to run

You can enter simple python code like printing something on terminal from the __main__.py file

**integrate/__main__.py**
```
print("hello world")
```

**cmd**
```
.../intergrate> python integrate
hello world
```

This means for running code we have to write python code inside the **__main__.py** file

**NOTE:** There is a very detailed tutorial on creating Parser for command-line options, 
arguments and sub-commands on the [Realpython](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/). In this section
this is what we are gonna do, we are going to create a command-line app in python

For that we are going to use [Argparse](https://docs.python.org/3/library/argparse.html)
which has a lot of tools and features for creating simple to advanced command-line app

**__main__.py**
```
from argparse import ArgumentParser

from data_manager import find_user

parser = ArgumentParser(prog="integrate", usage="%(prog)s [options]",
	description="Run python codes for handling csv data using the commands and options")

parser.add_argument("--user_id", type=int, help="enter the user's id for displaying user details")

args = parser.parse_args()

print(args)
print(args.user_id)
```

We import the ArgumentParser from argparse which is used to create a parser through
which we can add arguments. At first we just add a simple argument **--user_id** 
which is of ```type=int``` and just print the args and the user_id from args

**cmd**
```
> python integrate --user_id 10
(Namespace=10)
10
```

Our args and the user_id gets printed if we don't pass in any id

**cmd**
```
> python integrate --user_id
(Namespace=None)
None
```

Now making this command functional. 

1. Create a new file **data_manager.py**
2. Copy the code from **python_csv/read_specific_data.py** into **data_manager.py**
3. Import find_user function into **__main__.py**
4. Call ```find_user(user_id=args.user_id)``` by passing args.user_id and print it
5. run ```python integrate --user_id 10```

**cmd**
```
4
USER ID: 4 NOT FOUND AND EMAIL NOT PROVIDED
```

**NOTE:** In our __main__ file we import find_user from data_manager file using
```from data_manager import find_user``` here we don't user relative import like
```from .data_mangaer import find_user``` since the file is on the same path and 
__main__ file enables that for us.

You might be wondering that we have **data.csv** file in the integrate as well as 
python_csv folder but we have used the **python_csv/data.csv** path because on
using ```with open('data.csv')``` it raises error file not found so we have to
get the whole path of the file using the **os** module

**NOTE:** In our data_mangar.py file we used os.path.join to get the path of 
**data.csv** file, if we use 

```
os.path.join(os.getcwd(), 'data.csv')
```

And then run ```python integrate --user_id 1``` it will again raise the same file not
found error which is somewhat related to the way ```os.path.getcwd()``` 

According to [documentation](https://docs.python.org/3/library/os.path.html) 

```
os.getcwd() 
	Return a string representing the current working directory.
```

This means when we run the function from the **cmd** i.e. from **python_intermediate**
folder we get the path of that folder instead of **python_intermediate/integrate**.

Now to check this you can run the data_manager.py file by adding a print statement for
the ```FILE_PATH``` variable

```
.../integrate> python data_manager.py
.../integrate/data.csv
```

So for solving this problem we just need to use instead of ```os.getcwd()```

**integrate/data_manager.py**
```
FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')
```

```os.path.dirname``` takes a filename as a string and returns the directory path 
portion

And ```__file__``` in python is a keyword which is the whole file path, just print
the __file__ and you will know what I am talking about

```
print(__file__)
```

Using ```os.path.join(os.path.dirname(__file__), 'data.csv')``` returns the 'data.csv'
path file inside **integrate** folder

Run the *integrate command* again and it works perfectly.

**Adding more arguments**

We can also add multiple arguments doing the same function 

**__main__.py**
```
parser.add_argument(
	"-id",
	"--user_id",
	type=int,
	help="enter the user's id for displaying user details"
)
```

**cmd**
```
> python integrate -id 3
```

Will work the same way

**Adding required arguments in argparse**

Till now we have been using [options] that means optional arguments which starts with
```--user_id``` and their short forms ```-id``` but we can add required arguments using

```
parser.add_argument(
	"type",
	type=str,
	choices=['view', 'message']
)
```

The ```"type"``` here is a required argument which is to be passed everytime before
passing in the optional arguments. We have added two choices for the required argument
```view``` and ```message```, for using it we can run

**cmd**
```
.../python_intermediate> python integrate view -id 2
# RESULTS SHOWN HERE

.../python_intermediate> python integrate message
Sending message
```

We accessed the argument ```type``` from the args using

```
if args.type == "view":
...
if args.type = "message":
...
```

This gives us more functionality. There is a lot more we can do with **argparse** module, be sure to checkout 

1. [documentation](https://docs.python.org/3/library/argparse.html)
2. [Real Python](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
3. [CodingForEntrepreneurs](https://www.codingforentrepreneurs.com/projects/30-days-python/)

No I am not a partener with [RealPython](https://www.realpython.com) or [
CodingForEntrepreneurs](https://www.joincfe.com) but they are best python learning 
websites.

For more tutorials like this head on to my [site](http://www.codementor.tk) and don't 
forget to checkout my [other](https://github.com/Alexmhack) tutorials on github.

If you find any mistake in my code, please do contribute.

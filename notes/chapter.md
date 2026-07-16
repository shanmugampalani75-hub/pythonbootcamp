mongoDB

username : ratanambani
password :QPe26ippqgzqq0J5
API key : mongodb+srv://ratanambani:QPe26ippqgzqq0J5@cluster0.dhcy5wr.mongodb.net/?appName=Cluster0

error handling for database

suitable using else and finally
try:

code

except FileNotFoundError (if fail - print error)

if successful
else: (can use else to print the success message)

finally (is basically used where whether there is error or a function runs successfully, finally block will run)

when accessing an object, the calling place should have a parenthesis = "()"

so everytime when we want to access the db to perform function we must use 3 things:

with sqlite3.connect(self.db_name) as conn
cursor = conn.cursor()

cursor.execute('''script query''')

when debugging

- read from bottom to top
- when fixing the code, fix from top to bottom

when importing library or file, make sure the import from file shouldnt start with number.
for example: from 15_database.py as DatabaseManager = wrong
from SQL_database.py as DatabaseManager = correct

200 - successfully created
300- successfully created to a file
400 - error
500 - server error

method to call swagger : uvicorn 17_fastsql:app

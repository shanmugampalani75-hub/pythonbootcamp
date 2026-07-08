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

import mysql.connector

print(
    """HELLO
WELCOME TO QUIZ APP\n"""
)

print("Choose option:")
print("1. Take Quiz\n")
print("2. Check Score\n")
print("3. Quit app\n")

try:
    choice = int(input("Enter choice [1,2,3]: "))
except:
    print("Please enter only numeric value as choices.")
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="quiz_comp"
)
mycursor = mydb.cursor()
mycursor.execute("select * from questions")

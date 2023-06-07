import mysql.connector
import pdb

# this is a new comment
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="quiz_comp"
)
mycursor = mydb.cursor()

mycursor.execute(
    "create table if not exists questions\
    (qno_no int(3) primary key , \
    qno_desc varchar(10000), \
    opt_a varchar(50), opt_b varchar(50), \
    opt_c varchar(50) ,opt_d varchar(50) , \
    ans varchar(5000))"
)

mycursor.execute(
    "create table if not exists participants(reg_no int(5) primary key , participant_name varchar(50))"
)
mycursor.execute(
    "create table if not exists scores(reg_no int(5) primary key ,total_correct int(50),total_wrong int(50),total_attempted int(50), scores int(50))"
)

print("QUIZ SOFTWARE")
print("1.questions")
print("2.participants")
# print("3.scores update")
# print("4.display")

choice = int(input("enter your wish:"))
if choice == 1:
    sql = int(input("enter the index_no:"))  # TODO: make this field autogen numbers
    sql1 = input("enter the ques_desc:")
    sql2 = input("enter the option a:")
    sql3 = input("enter the option b:")
    sql4 = input("enter the option c:")
    sql5 = input("enter the option d:")
    ans = input("Answer? ")

    sql_quiz = f"insert into questions1 values('{sql}', '{sql1}', '{sql2}', '{sql3}', '{sql4}', '{sql5}', '{ans}')"
    mycursor.execute(sql_quiz)
    print(
        "Your request has been processed.Thank you for making us as a part of your project"
    )
    mydb.commit()

if choice == 2:
    sql6 = int(input("enter the participant reg_no:"))
    sql7 = input("enter the participant name:")
    sql8 = int(input("enter the age group:"))
    sql9 = input("enter the city:")
    sql10 = int(input("enter the no of appearances made:"))

    # sql_int="insert into participants values("+ (sql6)+ ",'" + str(sql7) + ",'" + (sql8) + ",'" + str(sql9) +",'"+str(sql10)+")"
    sql_reg = f"insert into  participants values('{sql6}', '{sql7}', '{sql8}', '{sql9}', '{sql10}')"
    mycursor.execute(sql_reg)
    print("participants are all updated")
    mydb.commit()
# this was debugged by syan

# TODO: make related score table also with session


# if choice==3:
#     a=int(input("enter the reg_no"))
#     b=input("enter the participants name")
#     c=int(input("enter the total correct answer"))
#     d=int(input("enter the incorrect answer"))
#     e=int(input("enter the no_of_attempted_questions"))

#     sql_score = f"insert into scores values('{a}', '{b}', '{c}', '{d}', '{e}')"
#     # sql_insert="insert into scores values("+ str(a)+ ",'" + (b) + ",'" + str(c) + ",'" + (d) + ",'" + (e) +")"
#     mycursor.execute(sql_score)
#     print("scores and results updated")
#     mydb.commit()

import random
import pwinput as pp#install pwinput lib using "pip3 install pwinput" statement 
import mainmenu as m1
import mysql.connector as sqltor
import config
import acc_create

#establishing the connection
mycon = sqltor.connect(
    host = 'localhost',
    user = config.mysql_user,
    passwd = config.mysql_passwd,
    database = 'bank'
)
#Checking if connecter or not
if mycon.is_connected() == False:
   print('Could not connect to database...')

#Creating a sql cursor   
cur = mycon.cursor()



#Extracting all account numbers from the database into a list
cur.execute("select AccNo from data")
acc_data = cur.fetchall()
allacc_no = []
for a in acc_data:
   allacc_no.append(a[0])
#print(allacc_no)

ch = ""

# m1.ldash()
# print("Login:")
# m1.ldash()
# accno = int(input("Enter account number: "))

accno = input("Enter account number: ")
if accno in allacc_no:
    pass_input = str(pp.pwinput(prompt="Enter password: ", mask="*"))
    m1.ldash()
    cur.execute("select Password from pass where AccNo = {}".format(accno))
    pass_true = cur.fetchone()
    cur.execute("select * from data where AccNo = {}".format(accno))
    alldata = cur.fetchall()    
    if pass_input == pass_true[0]:
        print("Welcome",alldata[0][1],"!")
        print("Press (1) to View Account Details")
        print("Press (2) to ")
        print("Press (3) to Withdraw money")
        print("Press (4) to Deposit money")
        print("Press (5) to")
    else:
        print("Wrong password!")
else:
    print("Account number",accno,"does not exist!")
    m1.menu()
    if m1.num == 1:
        acc_create.acc_create()
    elif m1.num== 2:
        print('tbd')
        


import random
import mainmenu as m1
import mysql.connector as sqltor
import tables

#establishing the connection
mycon = sqltor.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'zzzzzz',
    database = 'bank'
)
if mycon.is_connected() == False:
   print('Could not connect to database...')
   
cur = mycon.cursor()

#tables.tables()

cur.execute("select AccNo from data")
acc_data = cur.fetchall()
allacc_no = []
for a in acc_data:
   allacc_no.append(a[0])
print(allacc_no)
m1.menu()


if m1.num == 1:
    m1.ldash()
    print("| Create New Account |")
    m1.ldash()
    name = str(input("Enter Name: "))
    phone = str(input("Enter Phone: "))
    age = str(input("Enter Age: "))
    address = str(input("Enter Address: "))
    accno = random.randint(100,999)
    while accno in allacc_no:
        accno = random.randint(100,999)
    if accno not in allacc_no:
        cur.execute("insert into data values({},'{}',{},{},'{}')".format(accno,name,phone,age,address))
    mycon.commit()

    password1 = str(input("Create new password: "))
    password2 = str(input("Re-enter new password: "))
    if password1 != password2:
        while password1 != password2:
            print("Passwords do not match!")
            password1 = str(input("Create new password: "))
            password2 = str(input("Re-enter new password: "))
    print("Account Created Successfully!")
    print("Your Account Number:",accno)
    print("Your Password:",password1)
    print("Remember these details!")
    cur.execute("insert into pass values({},'{}')".format(accno,password1))
    mycon.commit()
    
import random
import pwinput as pp #install pwinput lib using "pip3 install pwinput" statement 
import mainmenu as m1
import mysql.connector as sqltor
import tables
import config

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
#m1.menu()


def acc_create():
    m1.ldash()
    print("| Create New Account |")
    m1.ldash()
    name = str(input("Enter Name: "))
    phone = str(input("Enter Phone: "))
    age = str(input("Enter Age: "))
    address = str(input("Enter Address: "))
    accno = random.randint(100,999)
    while accno in allacc_no: #Ensuring the accno remains unique
        accno = random.randint(100,999)
    if accno not in allacc_no:
        cur.execute("insert into data values({},'{}',{},{},'{}')".format(accno,name,phone,age,address))
    mycon.commit()

    password1 = str(pp.pwinput(prompt="Create new password: ", mask="*"))
    password2 = str(pp.pwinput(prompt="Re-enter New Password:", mask="*"))
    if password1 != password2:
        while password1 != password2:
            print("Passwords do not match!")
            password1 = str(pp.pwinput(prompt="Create new password: ", mask="*"))
            password2 = str(pp.pwinput(prompt="Re-enter New Password: ", mask="*"))
    print("Account Created Successfully!")
    print("Your Account Number:",accno)
    #print("Your Password:",password1)  #Note From ashish :Security flaw should not display these
    print("Remember this detail!")
    cur.execute("insert into pass values({},'{}')".format(accno,password1))
    mycon.commit()
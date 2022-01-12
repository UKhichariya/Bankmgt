import tables
#tables.tables()
#Run the above statement just once to make the necessary tables
import random
import pwinput as pp #install pwinput lib using "pip3 install pwinput" statement 
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



ch = ''

while ch.lower() != 'exit':
    #Extracting all account numbers from the database into a list
    cur.execute("select AccNo from data")
    acc_data = cur.fetchall()
    allacc_no = []
    for a in acc_data:
        allacc_no.append(a[0])
    #print(allacc_no)
    m1.menu()
    if m1.num == '1':
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
            cur.execute("insert into data values({},'{}',{},{},'{}',{})".format(accno,name,phone,age,address,0))
        mycon.commit()

        password1 = str(pp.pwinput(prompt="Create new password: ", mask="*"))
        password2 = str(pp.pwinput(prompt="Re-enter New Password:", mask="*"))
        if password1 != password2:
            while password1 != password2:
                print("Passwords do not match!")
                password1 = str(pp.pwinput(prompt="Create new password: ", mask="*"))
                password2 = str(pp.pwinput(prompt="Re-enter New Password: ", mask="*"))
        print("Account Created Successfully!")
        print("You will be able to manage funds after logging in.")
        print("Your Account Number:",accno)
        print("Remember this detail!")
        cur.execute("insert into pass values({},'{}')".format(accno,password1))
        mycon.commit()



    if m1.num == '2':
        while ch.lower() != "x":
            if ch.lower() != "x":
                accno = int(input("Enter account number: "))
            if accno in allacc_no:
                while ch.lower() != 'z':
                    if ch.lower() == "x":
                        break
                    pass_input = str(pp.pwinput(prompt="Enter password: ", mask="*"))
                    m1.ldash()
                    cur.execute("select Password from pass where AccNo = {}".format(accno))
                    pass_true = cur.fetchone()
                    cur.execute("select * from data where AccNo = {}".format(accno))
                    alldata = cur.fetchall()    
                    if pass_input == pass_true[0]:
                        while ch.lower() != 'x' or ch.lower() != 'z':
                            print("Welcome",alldata[0][1],"!")
                            print("Press (1) to View Account Details")
                            print("Press (2) to ")
                            print("Press (3) to Withdraw money")
                            print("Press (4) to Deposit money")
                            print("Press (5) to")
                            print('PRESS (x) to return to main menu')
                            ch = input("Enter 1/2/3/4/5/X: ")
                            if ch == '1':
                                print('Acc. No. Name Phone Age Address Balance(INR)')
                                for a in alldata[0]:
                                    print(a,end = '\t')
                            if ch.lower() == 'x':
                                break
                    else:
                        print("Wrong password!")
                        print('PRESS x to return to main menu')
                        print('PRESS z to return to Login again')
                        ch = input("Enter here(x/z): ")
                        if ch.lower() == 'x':
                            break
                if ch.lower() == 'x':
                    break
                else:
                    ch = ''
            else:
                m1.ldash()
                print("Account number",accno,"does not exist!")
                print('PRESS x to return to main menu')
                print('PRESS z to return to Login again')
                m1.ldash()
                ch = input("Enter here(x/z): ")
                if ch.lower() == 'x':
                    print()
                else:
                    ch = ''
        ch = ''    
    if m1.num.lower() == 'exit':
        print("Thank you for using the program!")
        break
    else:
        print("Please enter correct option!")
        

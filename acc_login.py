import mainmenu as m1
import random
import mysql.connector as sqltor
import config
import pwinput as pp

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

#Program that runs when the user wants to login and access further.
def acc_login():
    cur.execute("select AccNo from data")
    acc_data = cur.fetchall()
    allacc_no = []
    for a in acc_data:
        allacc_no.append(a[0])
    #print(allacc_no)
    ch = ''
    while ch.lower() != "x":
        if ch.lower() != "x":
            m1.ldash()
            print("|\t\t Login\t\t       |")
            m1.ldash()
            accno = int(input("Enter account number: "))
        if accno in allacc_no:
            while ch.lower() != 'z':
                if ch.lower() == "x":
                    break
                pass_input = str(pp.pwinput(prompt="Enter password: ", mask="*"))
                cur.execute("select Password from pass where AccNo = {}".format(accno))
                pass_true = cur.fetchone()
                cur.execute("select * from data where AccNo = {}".format(accno))
                alldata = cur.fetchall()    
                if pass_input == pass_true[0]:
                    while ch.lower() != 'x' or ch.lower() != 'z':
                        fields = ['Account Number','Name','Phone','Age','Address','Balance']
                        print('\n')
                        m1.leq()
                        print("Welcome",(alldata[0][1]).title(),"!")
                        m1.leq()
                        print("Press (1) to View User Details")
                        print("Press (2) to Deposit money")
                        print("Press (3) to Withdraw money")
                        print("Press (4) to")
                        print('PRESS (x) to return to main menu')
                        m1.ldash()
                        ch = input("Enter 1/2/3/4/5/X: ")
                        m1.ldash()
                        if ch == '1':
                            for a in range(5):
                                print(fields[a],':',alldata[0][a]) 
                                m1.ldash()
                            print(fields[5],':',int(alldata[0][5]))
                        if ch == '2':
                            dep = float(input("Enter amount to deposit: ")) 
                            cur.execute("update data set balance = balance+{} where accno = {};".format(dep,accno))
                            mycon.commit()
                            print('.\n..\n...\n')
                            print('Rs',dep,'added to your account successfully!')
                            cur.execute("select * from data where AccNo = {}".format(accno))
                            alldata = cur.fetchall()    
                            #Updating the deposit for the temp python list 'alldata'
                        if ch == '3':
                            wit = float(input("Enter amount to withdraw: "))
                            if wit <= alldata[0][5]-100:
                                cur.execute("update data set balance = balance-{} where accno = {};".format(wit,accno))
                                mycon.commit()
                                m1.ldash()
                                print('Rs',wit,'withdrawn from your account! ')
                                print('.\n..\n...\nPlease collect the cash')
                                m1.ldash()
                                cur.execute("select * from data where AccNo = {}".format(accno))
                                alldata = cur.fetchall()    
                                #Updating the deposit for the temp python list 'alldata'

                            else:
                                print('Your account has a balance of',alldata[0][5])
                                print('You can\'t withdraw more than what you have!')
                                print('The minimum balance in your bank account can\'t go below 100.')
                        
                        if ch.lower() == 'x':
                            break
                    
                else:
                    print()
                    print("Wrong password!")
                    m1.ldash()
                    print('PRESS x to return to main menu')
                    print('PRESS z to return to Login again')
                    m1.ldash()
                    ch = input("Enter here(x/z): ")
                    if ch.lower() == 'x':
                        print()
                        break
            if ch.lower() == 'x':
                break
            else:
                ch = ''
        else:
            m1.ldash()
            print("Account number",accno,"does not exist!")
            m1.ldash()
            print('PRESS x to return to main menu')
            print('PRESS z to return to Login again')
            m1.ldash()
            ch = input("Enter here(x/z): ")
            if ch.lower() == 'x':
                print()
            else:
                ch = ''
    ch = ''    
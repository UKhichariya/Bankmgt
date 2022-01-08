import random
import mainmenu as m1
import mysql.connector as sqltor

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

table_data = ('''create table data(
            AccNo int,
            Name char(30),
            Phone int(20),
            Age int(3),
            Address char(70),
            PRIMARY KEY (AccNo))
        ''')
table_pass = ('''create table pass(
            SNo int,
            AccNo int,
            Password varchar(30),
            FOREIGN KEY (AccNo) REFERENCES data(AccNo))
        ''')
#cur.execute(table_data)
#cur.execute(table_pass)

m1.menu()
cur.execute("select AccNo from data")
dx = cur.fetchall()
print(dx)

if m1.num == 1:
    m1.ldash()
    print("| Create New Account |")
    m1.ldash()
    name = str(input("Enter Name: "))
    phone = str(input("Enter Phone: "))
    age = str(input("Enter Age: "))
    address = str(input("Enter Address: "))
    accno = random.randint(100,999)
    cur.execute("insert into data values({},'{}',{},{},'{}')".format(accno,name,phone,age,address))
    mycon.commit()
    print("Account Created Successfully!")  
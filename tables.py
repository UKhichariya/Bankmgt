import mysql.connector as sqltor
import config
#establishing the connection
mycon = sqltor.connect(
    host = 'localhost',
    user = config.mysql_user,
    passwd = config.mysql_passwd,
    database = 'bank'
)
if mycon.is_connected() == False:
   print('Could not connect to database...')

cur = mycon.cursor()

def tables():
    table_data = ('''create table data(
                AccNo int,
                Name char(30),
                Phone bigint(20),
                Age int(3),
                Address char(70),
                balance float(20),
                PRIMARY KEY (AccNo))
            ''')
    cur.execute(table_data)

    table_pass = ('''create table pass(
                AccNo int,
                Password varchar(30),
                FOREIGN KEY (AccNo) REFERENCES data(AccNo))
            ''')
    cur.execute(table_pass)

def sample_data():
    table_sample1 = ("INSERT INTO data VALUES({},'{}',{},{},'{}',{})".format(111,'Utkarsh Khichariya',23456789,17,'A-169, BC Nagar, New Delhi',10000))
    cur.execute(table_sample1)        
    table_sample2 = ('insert into data values({},"{}",{},{},"{}",{})'.format(543,'Sonal Jaiswal',873483874,19,'B2-312,Dream Board Colony, Kolkata',15000))
    cur.execute(table_sample2)    
    table_sample3 = ('insert into data values({},"{}",{},{},"{}",{})'.format(333,'Ashish Kumar Singh',66755555,25,'129, Real Housing, Goa',20000))
    cur.execute(table_sample3)    
    table_sample4 = ('insert into data values({},"{}",{},{},"{}",{})'.format(212,'Aman Bothra',444433,20,'420, Absolut Villas, Pune',22000))
    cur.execute(table_sample4)    
    table_sample5 = ('insert into data values({},"{}",{},{},"{}",{})'.format(245,'Zakee Ahmed',7654483,22,'554-C, Developed Residency, Jaipur',16000))
    cur.execute(table_sample5)   

    table_samplea = ("INSERT INTO pass VALUES({},'{}')".format(111,'aaa'))
    cur.execute(table_samplea)
    table_sampleb = ("INSERT INTO pass VALUES({},'{}')".format(543,'bbb'))
    cur.execute(table_sampleb)
    table_samplec = ("INSERT INTO pass VALUES({},'{}')".format(333,'ccc'))
    cur.execute(table_samplec)
    table_sampled = ("INSERT INTO pass VALUES({},'{}')".format(212,'ddd'))
    cur.execute(table_sampled)
    table_samplee = ("INSERT INTO pass VALUES({},'{}')".format(245,'eee'))
    cur.execute(table_samplee)        

    mycon.commit()
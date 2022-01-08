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

def tables():
    table_data = ('''create table data(
                AccNo int,
                Name char(30),
                Phone bigint(20),
                Age int(3),
                Address char(70),
                PRIMARY KEY (AccNo))
            ''')
    cur.execute(table_data)

    table_pass = ('''create table pass(
                AccNo int,
                Password varchar(30),
                FOREIGN KEY (AccNo) REFERENCES data(AccNo))
            ''')

    cur.execute(table_pass)
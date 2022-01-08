def ldash(n = 40):
    print('-'*n)
def leq(n = 40):
    print('='*n)

def menu():
    global num
    leq()
    print("\t\tXYZ Bank")
    leq()
    print("Press (1) to Create new account")
    print("Press (2) to Login")
    leq()
    num = int(input("Enter choice: "))
#    print("Press (3) to Withdraw money")
#    print("Press (4) to Deposit money")
#    print("Press (5) to Create new account")

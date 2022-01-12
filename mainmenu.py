def ldash(n = 40):
    print('-'*n)
def leq(n = 40):
    print('='*n)

def menu():
    global num
    leq()
    print("\t\tXYZ Bank")
    leq()
    print("Enter (1) to Create new account")
    print("Enter (2) to Login")
    print("Enter (exit) to Exit the program")
    leq()
    num = str(input("Enter choice: "))


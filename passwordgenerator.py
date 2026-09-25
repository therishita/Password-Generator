import random
import string
print("PASSWORD GENERATOR\n")

while True:
    while True:
        l=int(input("Enter Length of Password: "))
        if l>0:
            break
        else:
            print("Password length must be greater than 0.\n")

    while True:
        print("\nChoose Password Complexity:\n1: Letters Only\n2: Letters + Numbers\n3: Letters + Numbers + Special Characters")
        ch=int(input("Enter Choice: "))
        if ch==1:
            n=string.ascii_letters
            break
        elif ch==2:
            n=string.ascii_letters + string.digits
            break
        elif ch==3:
            n=string.ascii_letters + string.digits + string.punctuation
            break
        else:
            print("\nInvalid Choice!\n")

    password=""

    for i in range(l):
        characters=random.choice(n)
        password+=characters

    print("\nGenerated Password: ",password)
    while True:
        ask=input("\nGenerate another password?(y/n): ")
        if ask == "y":
            break
        elif ask == "n":
            print("\nTHANK YOU FOR USING PASSWORD GENERATOR!")
            ask = "n"
            break
        else:
            print("Invalid Input! Please enter y or n.")

    if ask == "n":
        break
#RISHITA SARKAR 
#CodSoft for Python Programming Task

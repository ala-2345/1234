from numpy import random
x = int(input("enter a four-digit number : "))
while True:
    z = random.randint(1000 , 9999)
    print(z)
    if x == z:
        print("i gussed your number")
        print(f"the password is {z}")
        print("Dr.Mallah was Here")
        break

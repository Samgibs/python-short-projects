def add(a , b):
    answer=a+b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a ,b):
    answer=a-b
    print(str(a) + "-" + str(b) + "=" + str(answer))


def mul(a ,b):
    answer=a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))


def div(a ,b):
    answer=a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. division")
    print("E. Quit")
    choice=input("enter your choice:    ")

    if choice=="a" or choice== "A":
        print("Addition")
        a=int(input("input value of a:  "))
        b=int(input("enter the value of b:  "))
        add(a, b)

    elif choice=="b" or choice== "B":
        print("Subtraction")
        a=int(input("input value of a:  "))
        b=int(input("enter the value of b:  "))
        sub(a, b)

    elif choice=="c" or choice== "C":
        print("Multiplication")
        a=int(input("input value of a:  "))
        b=int(input("enter the value of b:  "))
        mul(a, b)

    elif choice=="d" or choice== "D":
        print("Division")
        a=int(input("input value of a:  "))
        b=int(input("enter the value of b:  "))
        div(a, b)

    elif choice=="e" or choice== "E":
         print("program end here")
         quit()
    
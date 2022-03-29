def divby5(a):
    if a % 5 ==0:
        return True
    else:
        return False


def divby7(a):
    if a % 7 ==0:
        return True
    else:
        return False


def divby9(a):
    if a % 9 ==0:
        return True
    else:
        return False


def divby11(a):
    if a % 11 ==0:
        return True
    else:
        return False
if __name__ == "__main__":
    n1 = int(input("enter the number : "))

    r1 = divby5(n1)
    r2 = divby7(n1)
    r3 = divby9(n1)
    r4 = divby11(n1)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
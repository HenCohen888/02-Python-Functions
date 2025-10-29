#for a given change amount, the program prints a bill breakdown using bills of 20, 10, 5, 1 (₪).

def bill_change(amount):

    original = amount

    n20 = amount // 20
    amount = amount - n20 * 20

    n10 = amount // 10
    amount = amount - n10 * 10

    n5= amount // 5
    amount = amount - n5 * 5

    n1 = amount

    if n20 > 0: print(f"{n20} * 20 = {n20 * 20}")
    if n10 > 0: print(f"{n10} * 10 = {n10 * 10}")
    if n5 > 0: print(f"{n5} * 5 = {n5 * 5}")
    if n1 > 0: print(f"{n1} * 1 = {n1 * 1}")

    print("--------")
    print(original)


x = int(input("please enter the change value:"))
while x < 0:
    print("must be a positive value")
    x = int(input("please enter the change value:"))

bill_change(x)
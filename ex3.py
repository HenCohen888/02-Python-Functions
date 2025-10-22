#function receives a number and returns the digits number
#The program should read numbers from the user (unknown count) and stop when 999 is entered.

def sum_num(n):
    if n == 0:                 # special case: 0 has 1 digit
        return 1
    n = abs(n)                 # ignore minus sign for negatives
    count = 0
    while n > 0:
        n = n // 10            # drop the last digit
        count = count + 1
    return count               # give result back to the caller


while True:
    x = int(input("enter a number (999 to exit): "))
    if x == 999:
        print("thank you")
        break
    print("number of digits:", sum_num(x))
    
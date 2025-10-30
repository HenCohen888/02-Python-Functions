#the function get n numbers and return their avarage 

def avarage_n(n):
    total = 0.0                                       # 1) start a running sum
    for i in range(1, n + 1):                         # 2) repeat exactly n times
        x = float(input(f"enter number #{i}: "))
        total = total + x                             # 3) add to the running sum
    return total / n                                  # 4) RETURN the average

n = int(input("how many numbers? "))
while n <= 0:                                         # tiny validation: must be positive
    print("you must enter a positive number")
    n = int(input("how many numbers?"))

avg = avarage_n(n)                                    # call the function, capture return
print(f"the avarage is: {avg:.2f}")


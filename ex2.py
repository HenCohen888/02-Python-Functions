#the function get n numbers and return the avarage number

def avarage_n(n):
    total = 0.0
    for i in range(1, n + 1):
        x = float(input(f"enter number #{i}: "))
        total = total + x
    return total / n

n = int(input("how many numbers? "))
while n <= 0:
    print("you must enter a positive number")
    n = int(input("how many numbers?"))

avg = avarage_n(n)
print(f"the avarage is: {avg:.2f}")


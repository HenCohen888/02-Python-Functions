#Read an integer from the user, send it to a function, and the function should return 0 if the number is even, 1 if it’s odd.

def even_flag(n):  # If doubling half of n gives back n, it's even
    if (n // 2) * 2 == n:
        return 0
    else:
        return 1

x = int(input("enter an integer: "))
result = even_flag(x)
print("result:", result) # 0 for even, 1 for odd
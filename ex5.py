#the function computes the power of two numbers (base and exponent) without using pow.

def power(base,exp):
    if exp < 0:
        if base == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative exponent")
        base = 1 / base  #if base=!o (2 lines above) , its like else, so it jumps to this line
        exp = -exp

    result = 1
    for _ in range(exp):        # multiply 'exp' times
        result = result * base
    return result

# --- main program ---
b = float(input("Enter base: "))
e = int(input("Enter exponent (integer): "))
print(f"{b}^{e} =", power(b, e))
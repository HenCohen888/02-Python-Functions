#the function solve quadratic equation: ax2+bx+c=0
#Ask the user for a, b, and c.
#Make sure that:
#a is not 0 (because if a == 0, it's not quadratic anymore — it becomes linear).
#The discriminant is non-negative (≥ 0), otherwise the roots are complex (not real numbers).

#Return/print the roots if they are real.

import math

def quar_solve(a,b,c):
   
   if a == 0:
        return "a cannot be zero, it's not quadratic"
   
   d = b*b - 4*a*c  
   
   if d < 0:
        return "discriminant is negative, the roots are complex (not real)"

   sqrt_d = math.sqrt(d)

   x1 = (-b + sqrt_d) / (2 * a)
   x2 = (-b - sqrt_d) / (2 * a)
   
   return (x1, x2)


def main():
    print("Solve ax^2 + bx + c = 0")
    a = float(input("please enter a value for a: "))
    b = float(input("please enter a value for b: "))
    c = float(input("please enter a value for c: "))

    result = quar_solve(a, b, c)

    if isinstance(result, str):
        print("Error:", result)
    else:
        x1, x2 = result
        print(f"The solutions are: x1 = {x1}, x2 = {x2}")

if __name__ == "__main__":
    main()


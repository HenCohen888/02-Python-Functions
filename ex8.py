#The program should:
#Ask the user for two numbers, let’s call them a and b.

#Show a menu with options:
#a) print the biggest divider
#(we’ll clarify in a second what that means)
#b) print the smallest divider
#c) print pow(a, b) (that means 
#d) print sqrt(a) - sqrt(b)
#e) exit the program

#The user can choose options until they pick e (exit).
#So this is an interactive menu loop.

import math

def read_positive_int(prompt):

    while True:
        value = int(input(prompt))
        if value <= 0:
            print("please enter a positive number grater then zero.")
        else:
            return value

def biggest_divider(a, b):
    return math.gcd(int(a), int(b))

def smallest_divider(a, b):
    a = abs(int(a))
    b = abs(int(b))
    if a == 0 or b == 0:
        return "not defined when one number is a zero"
    
def power_result(a, b):
    """return a^b"""
    return pow(int(a), int(b))


def sqrt_diff(a, b):
    """return sqrt(a) - sqrt(b)"""
    # your read_positive_int already ensures a,b > 0, so this is safe.
    # if you ever allow non-positive values, wrap this in try/except ValueError.
    return math.sqrt(float(a)) - math.sqrt(float(b))



def main():
    print("Enter two positive numbers")
    a = read_positive_int("a = ")
    b = read_positive_int("a = ")

    while True:
        
        print("""
        a- the biggest devider
        b- the smallest divider
        c- the result of pow(a,b)
        d- the result of sqrt(a)-sqrt(b)]
        e- exit
          """)
        
        choice = input("please choose an option: ").strip().lower()

        if choice == "a":
         print("the biggest divider is:", biggest_divider(a, b))
        
        elif choice == "b":
         print("the smallest divider is:", smallest_divider(a, b))

        elif choice == "c":
         print(f"{a}^{b} =", power_result(a, b))

        elif choice == "d":
        # a and b are positive per your reader; this is safe.
         print("sqrt(a) - sqrt(b) =", sqrt_diff(a, b))

        elif choice == "e":
         print("bye")
         break

        else:
         print("invalid option, please try again.")


            


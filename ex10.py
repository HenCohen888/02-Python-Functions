#The function manage customer data for a book-printing company. A customer gets special handling only if they satisfy all of these:
#Yearly purchases > 8000 NIS
#Pays all invoices on time
#Customer seniority > 5 years
#Build a small program that:
#Reads basic customer info (id, name, yearly purchases, pays on time yes/no, years as customer)
#Decides if the customer gets special handling
#Prints a clear result


def main():

    print("please enter the following details")

    id = input("id number: ")
    name = input("castomer name: ")

    purch = float(input("yearly purchases: "))

    pay = input("Did he pay all invoices in time (y/n)? ").strip().lower()
    pays_on_time = (pay == "y")


    senior = int(input("castomer seniority in years: "))

    is_pref = treat_handling(purch,pays_on_time,senior)

    print("\n---Result---")
    print(f"Castomer: {name} id: {id}")
    print(f"Preferred: {'Yes - special handling' if is_pref else 'NO - regular handling'}")



def treat_handling(purch: float, pays_on_time: bool, senior: int) -> bool:

     """
    Return True iff customer meets ALL preferred conditions:
      1) yearly_sum > 8000
      2) pays_on_time is True
      3) years_with_company > 5
    """
     
     return((purch > 8000) and pays_on_time and (senior > 5))

if __name__ == "__main__":
     main()
#define a billing function for item price input
def cashier_billing():
    total = 0.0 #total starts at 0

    print("=== Cashier Billing System ===")
    print("Enter item prices one by one")
    print("Type 'done' or enter 0 to complete the transaction.")

    while True: #loop to ensure continuous input
        cashier_input = input("Enter item price: R")

        if cashier_input.lower() == "done": #ends loop & ensures if user input has a capital letter the system still reads 'done'
            break

        try:
            price = float(cashier_input) #allows decimals in input

            if price == 0:
                break

            if price < 0: #ensures input is valid
                print("Price cannot be negative. Try again.")
                continue

            total += price #increments total/ increases with price 

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if total > 1000: #add discount 
        discount_rate = 0.20
    elif total > 500:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discount_amount = total * discount_rate #define discount amount
    final_total = total - discount_amount #define final amount

#Print receipt with all information, ensuring decimal points are to the 2nd degree and translated into a string (f)
    print("\n=== Receipt ===")
    print(f"Total before discount: R{total:.2f}")
    print(f"Discount applied: R{discount_amount:.2f}")
    print(f"Final amount to pay: R{final_total:.2f}")

#call function
cashier_billing()


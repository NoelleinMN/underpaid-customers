
# NOTES BEGIN
# MELON_COST = 1.00

# melon cost is $1
# for all customers in txt list
# need to pull in customer name (first and last), customer number, number of melons ordered, and amount paid
# need to compare amount paid to what is needed to be paid for the order (numer of melons * MELON_COST)
# if amount paid != expected cost, need to print that information for review/action
# NOTES END


def wrong_payment(path):
    """Opens the customer order file at [path][customer-orders.txt], processes each line, and generates list of incorrect payments."""

    print("Review the following payments, and take action, as needed:")
    print("")

    MELON_COST = 1.00 # global variable
    customer_orders = open(path) # open file

    for line in customer_orders: # iterate over lines in file
        line = line.rstrip() # remove spaces
        words = line.split('|') # split into list of strings

        # assign variables to each index
        customer_number = words[0]
        customer_name = words[1]
        number_melons = float(words[2]) # assign type float
        customer_payment = float(words[3]) # assign type float

        expected_payment = number_melons * MELON_COST # calculate correct/expected payment

        if customer_payment > expected_payment:
            # if customer overpaid, print overpayment statement
            print(f"OVERPAID! Cust No. {customer_number} - {customer_name} - ordered {number_melons} of our melons, and paid ${customer_payment}.")

        elif customer_payment < number_melons * MELON_COST:
            # if customer underpaid, note payment needed
            print(f"PAYMENT NEEDED! Cust No. {customer_number} - {customer_name} - ordered {number_melons} of our melons, and paid ${customer_payment}.")

        elif customer_payment == expected_payment:
            # preserve space for future code if sending confirmation/receipt
            pass

    customer_orders.close() # close file

wrong_payment("customer-orders.txt") # call function with path filename
# coding: utf-8
import csv
from pathlib import Path

from numpy import number

loan_costs = [500, 600, 200, 1000, 450]

# Print the number of loans from the list
number_of_loans = len(loan_costs)
print(f"The number of {number_of_loans} loans.")

# Print the total value of the loans
total_of_all_loans = sum(loan_costs)
print(f"The total of all loans is ${total_of_all_loans: .2f}.")

# Print the average loan amount
average_loan_price = total_of_all_loans / number_of_loans
print(f"The average loans price is ${average_loan_price: .2f}.")

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extract the Future Value and Remaining Months on the loan and print each variable.
loan_future_value = loan.get("future_value")
loan_remaining_months = loan.get("remaining_months")

print(f"The future value of the loan is ${loan_future_value: .2f}.")
print(f"{loan_remaining_months} months remaining on the loan.")

# Use the formula for Present Value to calculate a "fair value" of the loan.
annual_discount_rate = 0.2
fair_value = loan.get("future_value") / (1 + annual_discount_rate / 12 ) ** loan.get("remaining_months")

print(f"The fair value of the loan is ${fair_value: .2f}.")

# Conditional statement to decide if the present value represents the loan's fair value.
if fair_value >= loan.get("loan_price"):
    print(f"At ${fair_value: .2f}, the loan is worth at least the cost to buy it.")
else:
    print(f"At ${fair_value: .2f}, the loan is too expensive and not worth the price.")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Function to calculate present value.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate/12)) ** remaining_months
    return present_value

# Use the function to calculate the present value of the new loan given below and print result.
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"],annual_discount_rate)
print(f"The present value of the loan is ${present_value: .2f}.")


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Created an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print(inexpensive_loans)

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path and print progress status message.
output_path = Path("inexpensive_loans.csv")
print(f'--> Writing data to csv file "{output_path}"...')

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

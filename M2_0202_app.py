# Initial imports
import csv
from pathlib import Path


# This function loads a CSV file from the filepath defined in `csvpath`
def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


# This function loads a CSV file with the list of banks and available loans information
# from the file defined in `file_path`
def load_bank_data(file_path):
    csvpath = Path(file_path)
    return load_csv(csvpath)


# As a lender,
# I want to calculate the monthly debt-to-income ratio
# so that we can assess the ability to pay of the borrower
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio


# As a lender,
# I want to calculate the loan-to-value ratio
# so that we can evaluate the risk of lending money to the borrower
def calculate_loan_to_value_ratio(loan_amount, home_value):
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio

# As a lender,
# I want to filter the bank list by checking the customer's desired loan against the bank's maximum loan size
# so that we can know which banks offer the loan amount requested by the customer
def filter_max_loan_size(loan_amount, bank_list):
    loan_amount_approval_list = []
    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_amount_approval_list.append(bank)
    return loan_amount_approval_list


# As a lender,
# I want to filter the bank list by checking if the customer's credit score is equal to or greater than the minimum allowed credit score defined by the bank
# so that we can know which banks are willing to offer a loan to the customer

def filter_credit_score(credit_score, bank_list):
    credit_score_approval_list = []
    for bank in bank_list:
        if credit_score >= int(bank[4]):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list



# As a lender,
# I want to filter the bank list by comparing if the customer's debt-to-income is equal to or less than the maximum debt-to-income ratio allowed by the bank
# so that we can assess if the customer will have payment capacity according to the bank's criteria
def filter_debt_to_income(monthly_debt_ratio, bank_list):
    monthly_debt_ratio_list = []
    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            monthly_debt_ratio_list.append(bank)
    return monthly_debt_ratio_list


# As a lender,
# I want to filter the bank list by checking if the customer's loan-to-value is equal to or less than the maximum loan-to-value ratio allowed by the bank
# so that we assess if the customer's home value is worth as an asset to secure the loan
def filter_loan_to_value(loan_to_value_ratio, bank_list):
    loan_to_value_ratio_list = []
    for bank in bank_list:
        if loan_to_value_ratio <= float(bank[2]):
            loan_to_value_ratio_list.append(bank)
    return loan_to_value_ratio_list


# This function implements the following user story:
# As a customer,
# I want to know what are the best loans in the market according to my financial profile
# so that I can choose the best option according to my needs
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


# This function is the main execution point of the application. It triggers all the business logic.
def run():
    # Set the file path of the CSV file with the banks and loans information
    file_path = Path("M2_02_daily_rate_sheet.csv")
    # Load the latest Bank data
    bank_data = load_bank_data(file_path)

    # This print statement will display all of the bank data that is provided.
    # print(f"bank_data: {bank_data}")

    # The following lines, set the applicant's information and implements the following user story:
    # As a customer,
    # I want to provide my financial information
    # so that I can apply for a loan
    credit_score = 750
    debt = 5000
    income = 20000
    loan_amount = 100000
    home_value = 210000

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Print the list of qualifying loans
    print(qualifying_loans)


run()

# In the customer_banking.py file, you will import the create_savings_account and create_cd_account functions,
# then create a main function that prompts the user to enter the savings and CD account details, call the
# corresponding functions to calculate the interest earned and update the balances, and display the results.

# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the initial balance for the savings account: "))
    savings_interest_rate = float(input("Enter the annual interest rate (in percentage) for the savings account: "))
    savings_months = int(input("Enter the number of months for the savings account: "))


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest_rate, savings_months
    )
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account - Interest Earned: {savings_interest_earned:.2f}")
    print(f"Savings Account - Updated Balance: {updated_savings_balance:.2f}")


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the initial balance for the CD account: "))
    cd_interest_rate = float(input("Enter the annual interest rate (in percentage) for the CD account: "))
    cd_months = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account - Interest Earned: {cd_interest_earned:.2f}")
    print(f"CD Account - Updated Balance: {updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
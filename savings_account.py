# In the savings_account.py file, you will import the Account class and create a create_savings_account
# function that will create a savings account instance, calculate the interest earned based on user input,
# update the account balance with the earned interest, and return the updated balance and interest earned.

"""Import the Account class from the Account.py file."""
from Account import Account


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    savings = Account(balance, 0)

    # Calculate interest earned
    interest = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savings.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    savings.set_interest(interest)

    # Return the updated balance and interest earned.
    return updated_balance, interest

if __name__ == "__main__":
    initial_balance = 1000.0
    annual_interest_rate = 5.0
    duration_in_months = 6
    updated_balance, interest_earned = create_savings_account(initial_balance, annual_interest_rate, duration_in_months)
    print(f"Updated Balance: ${updated_balance:.2f}")
    print(f"Interest Earned: ${interest_earned:.2f}")
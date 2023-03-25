# Loan qualifier 

Add new features and enhancements to the loan qualifier application. The loan qaulifier app is deigned to meet the following *user stories* extracted from the *Bootcamp Asynchronous* lecture notes:

User stories:

⋅⋅* As a lender, I want to calculate the monthly debt-to-income ratio so that we can assess the borrower's ability to repay the loan.

⋅⋅* Given that I want to calculate the monthly debt-to-income ratio, when the monthly debt is less than zero or the monthly income is equal to or less than zero, then the application should raise an error.

⋅⋅* As a lender, I want to calculate the loan-to-value ratio so that we can evaluate the risk of lending money to the borrower.

⋅⋅* Given that I want to calculate the loan-to-value ratio, when the loan amount or the home value are equal to zero, then the application should raise an error.

---

## Technologies

The technologies used are:
1. Python programming language
2. Git
3. Githib
4. Visual Studio
5. Software modules
    -credit_score.py
    -debt_to_income.py
    -loan_to_value.py
    -max_loan_size.py
    -calculators.py
    -fileio.py
---
The following Python modules need to be  installed if not already installed:
⋅⋅* File
⋅⋅* Questionary

## Installation Guide

To install, clone the project onto your directory.

---

## Usage

To run the app open a terminal and type "app.py" followed by "Enter"

Here is a sample step to run the code:..
(dev) C:\Users\bakar\Desktop\FinTech\Bootcamp\Challenge\Module2\Starter_Code\loan_qualifier_app>python  app.py..
? Enter a file path to a rate-sheet (.csv): data/daily_rate_sheet.csv..
? What's your credit score? 750..
? What's your current amount of monthly debt? 2000..
? What's your total monthly income? 70000..
? What's your desired loan amount? 2000..
? What's your home value? 300000..
The monthly debt to income ratio is 0.03..
The loan to value ratio is 0.01...
Found 15 qualifying loans..
? Would you like me to save your qualifying loans? Yes..
? Please enter a file path and file name for the qualifiyng loans (for exapmple data/myfile.csv) data/qualifying_loans.csv..

(dev) C:\Users\bakar\Desktop\FinTech\Bootcamp\Challenge\Module2\Starter_Code\loan_qualifier_app>


---

## Contributors

The project is based on the template of the FinTech Bootcamp Module 2 Challenge.

---

## License

MIT

# banking app

#     Login : user inputs username and password
#         If username and password are correct, ---> check
#         what are acccounts related(owned) to user
#         get balance of each account
#     user expects output on Screen - Account Balance

cust_accounts = {
    "Sumit": {  
        "Name": "Sumit",
        "Contact": "123456789",
        "Address": {
            "Preferred": "Current"
            "Current": { "First Line": "27 Morecambe Close", "City": "Stevenage", "Country": "United Kingdom", "PostCode": "SG1 2AZ" }
            "Permanent": { "First Line": "Bazar Galli", "City": "Auranagabad", "Country": "India", "PostCode": "431003" }
            "Work": { "First Line": "State Bank of India Global IT Center", "City": "Mumbai", "Country": "India", "PostCode": "400705" }
        }
        "accounts": {
            "Savings": {
                "account_number": "12345"
            },
            "Current": {  
                "account_number": "54321"
            },
            "Fixed": {
                "account_number": "123456"
            }
        }
    },
    "SumitSontakke": {  
        "Name": "Sumit Sontakke",
        "Contact": "123456789",
        "Address": {
            "Preferred": "Permanent"
            "Current": { "First Line": "27 Morecambe Close", "City": "Stevenage", "Country": "United Kingdom", "PostCode": "SG1 2AZ" }
            "Permanent": { "First Line": "Bazar Galli", "City": "Auranagabad", "Country": "India", "PostCode": "431003" }
            "Work": { "First Line": "State Bank of India Global IT Center", "City": "Mumbai", "Country": "India", "PostCode": "400705" }
        }
        "accounts": {
            "Savings": {
                "account_number": "12345"
            },
            "Current": {  
                "account_number": "54321"
            },
            "Fixed": {
                "account_number": "123456"
            }
        }
    },
    "John": {
        "Name": "John",
        "Contact": "987654321",
        "accounts": {
            "Savings": {
                "account_number": "2423242423"
            }
        }
    }
}

accounts_balance = {
    "12345": 100,
    "54321": 200,
    "123456": 300,
    "2423242423": 400
}

# get_accounts

# login function takes username and password as arguments
def user_login(username, password):
    # check if username and password are correct
    if username == "Sumit" and password == "123":
        return True
    elif username == "John" and password == "1234":
        return True
    else:
        return False

# if username and password are correct, check what accounts are related to user
def get_accounts(username):
    accounts_list = []
    account_types = [ key for key in cust_accounts.get(username, {}).get('accounts',{}).keys() ]
    for account_type in account_types:
        acc_no = cust_accounts.get(username,{}).get('accounts',{}).get(account_type,{}).get('account_number')
        accounts_list.append(acc_no)
    return accounts_list



# get balance of given account
def get_account_balance(account_number=0):
    if account_number == 0:
        return 0
    else:
        return accounts_balance.get(str(account_number),"Invalid Account")

def get_account_type(account_number = None):
    if account_number:
        users_list = [ key for key in cust_accounts.keys() ]
        for username in users_list:
            accounts_list = get_accounts(username)
            if account_number in accounts_list:
                account_types = [ key for key in \
                    cust_accounts.get(username, {}).get('accounts',{}).keys() ]
                for account_type in account_types:
                    acc_no = cust_accounts.get(username,{}).get('accounts',{}).get(account_type,{}).get('account_number')
                    if acc_no == account_number:
                        return account_type
        return "Unknown Account Type"

    else:
        return "Invalid account number"

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    logged_in = user_login(username, password)
    if logged_in:
        # if user has correct credentials, #
        print("Welcome, " + username)
        # get all accounts are related to user ["1", "2", "3"]
        accounts_list = get_accounts(username)
        # get balance of each account
        for account in accounts_list:
            account_balance = get_account_balance(account_number = account)
            account_type    = get_account_type(account_number = account)
            print(f"account={account} of type {account_type} has balance INR {account_balance} only")
        
    else:
        print("Invalid username or password")



# positional argument

# keyword argument / optional argument / named argument

# arbitory arguments
# keyword arguments
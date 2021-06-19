import os
from dotenv import load_dotenv
from venmo_api import Client, User #https://github.com/mmohades/Venmo

######## Primary Venmo Functions ########

# Get client connection for Venmo API requests using token in environment variable
def get_conn():
    load_dotenv() # Load values from .env
    token = os.environ.get('VENMO_TOKEN')
    return Client(access_token=token)

# Pay or request money from the specified user
def process_transaction(venmo_conn: Client, amount: float, message: str, recipient: User):
    if amount < 0:
        return venmo_conn.payment.request_money(amount, message, recipient.id)
    else:
        return venmo_conn.payment.send_money(amount, message, recipient.id)

# Get the list of friends for the user (based on connection)
def get_friends(venmo_conn: Client):
    userId = venmo_conn.user.get_my_profile().id
    return venmo_conn.user.get_user_friends_list(user_id=userId)

# Get recipient from the list of the user's friends by username (should be unique)
def get_friend(venmo_conn: Client, recipient_user_name: str):
    users = get_friends(venmo_conn)
    for user in users:
        if user.username == recipient_user_name:
            return user
    return None

######## Token Utilities ########

# Get your token - you'll need to go through 2FA process
def get_token(username: str, password: str):
    access_token = Client.get_access_token(username=username,
                                        password=password)
    print("My token:", access_token)

# Access tokens last forever, so log out when you're done
def logout(venmo_conn: Client):
    return venmo_conn.log_out(os.environ.get('VENMO_TOKEN'))


######## Investigative Utilities ########

# Print list of friends for user
def print_friends(venmo_conn: Client):
    users = get_friends(venmo_conn)
    for user in users:
        print(user.username," - ", user.id)

def get_transactions (venmo_conn: Client):
    userId = venmo_conn.user.get_my_profile().id
    transactions_list = venmo_conn.user.get_user_transactions(user_id=userId)
    for transaction in transactions_list:
        print(transaction)
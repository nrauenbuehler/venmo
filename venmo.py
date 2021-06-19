import argparse
from venmo_api import Client, User
from utils import *

def main():
    args = arguments()
    venmo_conn = get_conn()
    recipient = get_friend(venmo_conn, args.user) #limit recipients to friends for the to help prevent transactions with strangers
    return process_transaction(venmo_conn, args.amt, args.msg, recipient)

# https://docs.python.org/2/library/argparse.html
def arguments():
    parser = argparse.ArgumentParser(description='Run parameters')
    parser.add_argument('--amt', dest='amt', type=float, help='Amount of money to pay/request (negative is request)')
    parser.add_argument('--user', dest='user', type=str, help='The Venmo username of the person to receive the payment or request')
    parser.add_argument('--msg', dest='msg', type=str, help='The message to include in the transaction')
    return parser.parse_args()

if __name__ == "__main__":
    main()
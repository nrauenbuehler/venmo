import argparse
from utils import get_transactions, get_conn, logout
from venmo_api import Client, User

def main():
    venmo_conn = get_conn()
    get_transactions (venmo_conn)

if __name__ == "__main__":
    main()
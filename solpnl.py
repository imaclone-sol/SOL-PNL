import requests
import json

def fetch_transactions(wallet_address, api_key, limit=1):
    url = f"https://public-api.solscan.io/account/transactions?account={wallet_address}&limit={limit}"
    headers = {
        'accept': 'application/json',
        'token': api_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: Status code {response.status_code}, Response: {response.text}")
        return None

def display_transactions(transactions):
    # Here you can format and display the transactions as required
    print(json.dumps(transactions, indent=4))

def main():
    wallet_address = input("Enter Solana wallet address: ")
    api_key = ' '  # Replace with your actual API key
    transactions = fetch_transactions(wallet_address, api_key)
    if transactions:
        display_transactions(transactions)

if __name__ == "__main__":
    main()

import sys
import datetime
import time


red = "\033[31;1m"
yellow = "\033[33;1m"
green = "\033[32;1m"
reset = "\033[0m"

def time_counter(card):
   card = time.sleep(3)

def logger():
    print(f"{yellow}Welcome To I Sell Everything.com{reset}\n")
    bought = input(f"\n{green}please input what you want to buy please{reset}  ")
    

    while True:
     bill = input(f"\n{green}please input how much you are paying{reset}  ")
     if not bill.isnumeric():
        print(f"{red}Error: only digit's are allowed")
        continue
     card = input(f"{green}input your card pin{reset}  ")
     if not card.isnumeric():
         print(f"{red} Pin is not a number{reset}")
         continue
     if len(card) != 4:
         print(f"{red}Error: card pin must be 4 digits")
         continue
     else:
        print(f"{green}\nwait for 3 seconds please{reset}")
        time_counter(card)
     break
     
     
     

    transactions = [
    {"id": 1, "items": "coffee", "quantity": "1 cup", "amount": 500},
    {"id": 2, "items": "bread", "quantity": "2 cartons", "amount": 5000},
    {"id": 3, "items": "indomie noodles", "quantity": "2 cartons", "amount": 8000},
    {"id": 1, "items": "drinks", "quantity": "5 creates", "amount": 13000},
     ]
    for transaction in transactions:
     value = f"transaction {transaction['id']} | items: {transaction['items']} | quantity: {transaction['quantity']} amount: {transaction['amount']} "

    time = datetime.datetime.now()
    time_format = f"{yellow}=== Transaction Log | {time} ==={reset}"
    print(time_format)

    sys.exit(0)
logger()
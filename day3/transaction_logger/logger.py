import sys
import datetime
import time
from ai_service import get_ai_price
from email_sender import TransactionEmailer

red = "\033[31;1m"
yellow = "\033[33;1m"
green = "\033[32;1m"
reset = "\033[0m"

def time_counter(card):
   card = time.sleep(3)

def loggers():
    print(f"{yellow}Welcome To I Sell Everything.com{reset}\n")
    bought = input(f"\n{green}please input what you want to buy please{reset}  ")
    print(f"{yellow}looking up estimated price for {bought} wait for a sec{reset} ")
    suggested_price = get_ai_price(bought)
    print(f"Estimated Price: {suggested_price}")
    
    print("you just ended with the AI negotiation phase ")
    while True:
     bill = input(f"\n{green}So Tell Me How Much You agreed to pay with the AI service for records{reset}  ")

     card = input(f"{green}OK Input your card pin For Payment{reset}  ")
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
    
    buyer_name = input(f"{green}Input Your Name please  ")
    buyer_mail = input(f"{green}Input your email here for transaction receipt  ")
    print(f"\n{yellow} You just receive the transaction receipt thank you")
    emailer = TransactionEmailer(
       name = buyer_name,
       email = buyer_mail,
       item_name = bought,
       price = bill
    )

    email_success = emailer.send_receipt()
    if email_success:
        print(f"{yellow}You just received the transaction receipt, thank you!{reset}")

    time = datetime.datetime.now()
    time_format = f"{yellow}=== Transaction Log | {time} You bought ({bought}) | and you paid ${bill}=== {reset}"
    print(time_format)

    sys.exit(0)
loggers()
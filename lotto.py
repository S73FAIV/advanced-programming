####
# The tranlated exercise (by deepl.com):
#
# 1. A shop will reward its December customers under the following conditions:
#
# They must have paid by card.
# They must have purchased an item whose last four digits match those of the lottery jackpot.
# Prizes will be awarded in order of purchase until the campaign budget is exhausted.
# Once the budget is exhausted, no further prizes will be awarded.
# They have already calculated that this will happen, so we can take it for granted.
# The prize will be 90% of the total amount of that purchase
#
# The purchase data is in the file ‘December.com’. There is one line for each purchase:
# day hour minute itemcode itemcode .... 39999 amount cardnumber
# The purchases are already sorted, with the oldest first. 
# If no card was used, then the card number is 0. 
# The code 39999 does not correspond to any item; it is the mark for end and payment.
#
# Write a programme that reads the campaign budget and the winning lottery number from the keyboard
# and writes one line per winning purchase to the file ‘sorteo.prem’ with the card number
# and the prize amount.
# The programme must have at least one other function in addition to main, with the work
# divided into similar parts and with argument passing.
####

class Purchase:
    day, hour, minute = 0, 0, 0
    itemcodes = []
    amount = 0
    cardnumber: int = 0
    prize: float = 0.0

    def __init__(self, day: int, hour: int, minute: int, itemcodes: [], amount: float, cardnumber: int):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.itemcodes = itemcodes
        self.amount = amount
        self.cardnumber = cardnumber

    def __str__(self) -> str:
        return "date: " + str(self.day) + ":" + str(self.hour) + ":" + str(self.minute) + \
                "\nItems:" + str(self.itemcodes) + \
                "\nTotal: " + str(self.amount) + "\nCardnumber: " + str(self.cardnumber) + "\n"

    def is_payed_with_card(self) -> bool:
        if self.cardnumber == 0:
            return False
        return True

    def has_item_with_lottery_code(self, lottery_number: int) -> bool:
        for item in self.itemcodes:
            if str(item)[-4:] == str(lottery_number)[-4:]:
                return True
        return False

def get_num_input() -> int:
    for i in range(3):
        number = input("number: #")
        try:
            return int(number)
        except ValueError:
            print("The provided value \"%s\" was not a number, please provide a valid integer!" % number)


def convert_string_to_purchase(line: str):
    # we expect the structure of the line to be as specified in the excersise.
    array = line.split()
    # extract the time
    day, hour, minute = int(array.pop(0)), int(array.pop(0)), int(array.pop(0))
    # get all itemcodes
    end_position = array.index("39999")
    itemcodes = []
    for i in range(end_position):
        itemcodes.append(int(array.pop(0)))
    
    # delete the end-marker
    array.pop(0)

    # get the last values
    amount = float(array.pop(0))
    cardnumber = int(array.pop(0))
    return Purchase(day, hour, minute, itemcodes, amount, cardnumber)


def get_purchases() -> [Purchase]:
    purchases = []
    with open('diciembre.com', 'r') as file:
        # read the file as a string and split by newlines into a list
        lines = file.read().splitlines()

    for line in lines:
        purchases.append(convert_string_to_purchase(line))
    return purchases


def remove_non_apllicable_purchases(purchases: [Purchase], lottery_number: int) -> [Purchase]:
    cleaned_purchases = []
    for purchase in purchases:
        # 1. remove all purchases not payed with card
        if not purchase.is_payed_with_card():
            continue
        # 2. remove all purchases without matching item-numbers
        if purchase.has_item_with_lottery_code(lottery_number) == False:
            continue
        cleaned_purchases.append(purchase)
    return cleaned_purchases


def find_prize_winners(pruchases: [Purchase], budget):
    prize_winners = []
    for purchase in pruchases:
        # calculate potential prize 
        potential_prize = purchase.amount * 0.9
        if potential_prize >= budget:
            potential_prize = budget
            budget = 0
        else:
            budget = budget - potential_prize

        purchase.prize = potential_prize
        prize_winners.append(purchase)

        # exit the loop, if there is no budget left
        if budget == 0:
            break
        
    return prize_winners


def main():

    # 1. read in lottery number
    print("Please provide the winning lottery number:")
    lottery_number = get_num_input()
    # 2. read in campaign budget
    print("Please provide the campaign budget:")
    budget = get_num_input()
    
    # 3. read in file of payments
    print("Reading in file of payments and searching for valid payments.")
    purchases = get_purchases()

    # 4. remove any purchases not applicable for the lottery
    eligible_purchases = remove_non_apllicable_purchases(purchases, lottery_number)

    # 5. distribute budget
    prize_winners = find_prize_winners(eligible_purchases, budget)

    # 6. print the lucky winners
    print("The lucky winners are:")
    for purchase in prize_winners:
        print(purchase.cardnumber, purchase.prize)


if __name__=="__main__":
    main()

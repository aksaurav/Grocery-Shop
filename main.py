import time

class Shop:
    def __init__(self, products,price):
        self.product = products
        self.price = price

    def show_inventory(self):
        print('WELCOME TO AK STORE')

        print('\nWe have product listed for you... ')

        print('1. Chips - $2')
        print('2. Chanachur - $4')
        print('3. Speed - $8')
        print('4. Lacchi - $4')
        print('5. Biskits - $5')
        print('6. Tiger - $8')
        print('7. Breed - $1')
        print('8. Uro - $4')
        print('9. Miranda - $4')
        print('10. Juice - $3')


    def get_changes(self, budget):
        return budget - self.price

    def valid_input(self, budget):
        try:
            val = int(budget)
        except ValueError:
            try:
                val = float(budget)
            except ValueError:
                print('Please type a number')
        return val
    def get_changed(self, budget):
        return budget - self.price

    def discount_budget(self, budget):
        return budget * 0.1
        

    def shell(self):
        # let's first show the inventory!
        self.show_inventory()
        # let's ask the user budget
        budget = input("What's your budget!: ")
        # let's validate user input\
        self.valid_input(budget)
        print(f'If you shopping upto $50 you get a discount of %10')
        # next! 
        # let's ask the user what they want to buy from our inventory
        price_1 = 0
        while True:
            user = input('What do you want buy?: ')
            if user == self.product:
                print(f'Here\'s your {self.product}')
                # once we've got the product 
                # we need to ask for price
                price = float(input(f'The price for {self.product} is ${self.price}: '))
                if price == self.price:
                    print("It's Completed!")
                    price_1 += self.price
                elif price > self.price:
                    # let's make a helper function to give the changes to our user
                    print(f'It\'s Completed. Here\'s your changes ${self.get_changed(price)}')
                    price_1 += self.price
            else:
                print('Invalid Input!')

            time.sleep(0.8)
            ask_again = input('Do you want to continue buying? (Yes/No): ')
            if ask_again == 'yes':
                continue
            else:
                if price_1 >= 50:
                    bill = price_1 * 0.7
                    print(f'Congratulations!! You have got a discount')
                    print(f'After discount your total amount of shoping is ${bill}')
                else:
                    time.sleep(.8)
                    print(f'Your total amount of shopping is ${price_1}')
                    exit('Thanks for shopping from us!')
                
    

if __name__ == '__main__':
    chips = Shop('chips', 2)
    chips.shell()
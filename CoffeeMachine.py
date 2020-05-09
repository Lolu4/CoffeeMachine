class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def out(self):
        print('The coffee machine has:')
        print('{0} of water'.format(self.water))
        print('{0} of milk'.format(self.milk))
        print('{0} of coffee beans'.format(self.coffee))
        print('{0} of disposable cups'.format(self.cups))
        print('{0} of money'.format(self.money))

    def espresso(self):
        if self.water < 250 or self.coffee < 16 or self.cups < 1:
            print('Sorry, not enough water!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.coffee -= 16
            self.cups -= 1
            self.money += 4

    def latte(self):
        if self.water < 350 or self.milk < 75 or self.coffee < 20 or self.cups < 1:
            print('Sorry, not enough water!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
            self.money += 7

    def cappuccino(self):
        if self.water < 200 or self.milk < 100 or self.coffee < 12 or self.cups < 1:
            print('Sorry, not enough water!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cups -= 1
            self.money += 6

    def fill(self):
        self.water += int(input('Write how many ml of water the coffee machine has:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.coffee += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        print('I gave you $ {0}'.format(self.money))
        self.money = 0


my_mac = CoffeeMachine(400, 540, 120, 9, 550)
action = None
while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        drink = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'))
        if drink == '1':
            my_mac.espresso()
        elif drink == '2':
            my_mac.latte()
        elif drink == '3':
            my_mac.cappuccino()
        elif drink == 'back':
            continue
    elif action == 'fill':
        my_mac.fill()
    elif action == 'take':
        my_mac.take()
    elif action == 'remaining':
        my_mac.out()

class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        return ('''The coffee machine has:
        %s of water
        %s of milk
        %s of coffee beans
        %s of disposable cups
        %s of money
        ''' % (self.water, self.milk, self.beans, self.cups, self.money))

    def buy(self):
        self.choose = input('''What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
    ''')
        if self.choose == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough beans')
            elif self.cups < 1:
                print('Sorry, not enough cups')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1

        if self.choose == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.beans < 20:
                print('Sorry, not enough beans')
            elif self.milk < 75:
                print('Sorry, not enough milk')
            elif self.cups < 1:
                print('Sorry, not enough cups')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1

        if self.choose == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.beans < 12:
                print('Sorry, not enough beans')
            elif self.milk < 100:
                print('Sorry, not enough milk')
            elif self.cups < 1:
                print('Sorry, not enough cups')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1

    def fill(self):

        self.water += int(input('''Write how many ml of water do you want to add:
    '''))
        self.milk += int(input('''Write how many ml of milk do you want to add:
    '''))
        self.beans += int(input('''Write how many grams of coffee beans do you want to add:
    '''))
        self.cups += int(input('''Write how many disposable cups of coffee do you want to add:
    '''))

    def take(self):

        print('I gave you $%s' % self.money)
        self.money = 0

    def button(self):
        while True:
            self.action = input('Write action (buy, fill, take, remaining, exit):')

            if self.action == 'buy':
                self.buy()
            if self.action == 'fill':
                self.fill()
            if self.action == 'take':
                self.take()
            if self.action == 'remaining':
                print(self)
            if self.action == 'exit':
                break


coffee_machine = CoffeeMachine()
coffee_machine.button()

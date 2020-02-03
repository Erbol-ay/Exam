class CoffeeMachine:

    def __init__(self, milk = 1000, coffee = 1000, sugar = 1000):
        self.milk = milk
        self.coffee = coffee
        self.sugar = sugar

    def make_coffee(self, milk, coffee, sugar):
        if milk <= self.milk and coffee <= self.coffee and sugar <= self.sugar:
            print('------------------------------------')
            print('Процесс приготовления кофе завершен!')
            print('------------------------------------')
            CoffeeMachine.__subtract_milk(self, milk)
            CoffeeMachine.__subrtact_coffee(self, coffee)
            CoffeeMachine.__subtract_sugar(self, sugar)
        else:
            print('')
            print('У вас не хватает ресурсов')
            print('')
            if milk > self.milk:
                milk -= self.milk
                print('Пополните запас молока на ', milk, 'мл')

            if coffee > self.coffee:
                coffee -= self.coffee
                print('Пополните запас кофе на ', coffee, 'гр')

            if sugar > self.sugar:
                sugar -= self.sugar
                print('Пополните запас сахара на ', sugar, 'гр')

    def __subtract_milk(self, milk):
        self.milk -= milk
        print('Осталось ', self.milk, 'мл молока')

    def __subrtact_coffee(self, coffee):
        self.coffee -= coffee
        print('Осталось ', self.coffee, 'гр кофе')

    def __subtract_sugar(self, sugar):
        self.sugar -= sugar
        print('Осталось ', self.sugar, 'гр сахара')



if __name__ == "__main__":

    first_client = CoffeeMachine()

    first_client.make_coffee(200, 500, 200)

    second_client = CoffeeMachine()

    second_client.make_coffee(1200, 2333, 9000)

class    Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐厅的名字和菜品"""
        print("The restaurant's name is " + self.name.title())
        print("The cuisine's type is " + self.type.title())

    def open_restaurant(self):
        print(self.name.title() + " is open")

    def served_people(self):
        print(str(self.number_served) + " people have ate here.")

    def set_number_served(self, people):
        if people >= self.number_served:
            self.number_served = people
        else:
            print("wrong number")

    def increment_number_served(self, increase):
        self.number_served += increase


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,):
        super().__init__( restaurant_name, cuisine_type)
        self.flavours = ['apple','orange']

    def print_flavours(self):
         print(self.flavours)

restaurant1 = IceCreamStand('巧乐兹', 'icecream',)
restaurant1.describe_restaurant()
restaurant1.print_flavours()
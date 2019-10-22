class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        Restaurant.name = restaurant_name
        Restaurant.type = cuisine_type

    def describe_restaurant(self):
        """描述餐厅的名字和菜品"""
        print("The restaurant's name is " + self.name.title())
        print("The cuisine's type is " + self.type.title())

    def open_restaurant(self):
        print(self.name.title() + " is open")

restaurant1 = Restaurant('yizhandeng', 'xiangcai')
print(restaurant1.name)
print(restaurant1.type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        Restaurant.restaurant_name = restaurant_name
        Restaurant.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐厅的名字和菜品"""
        print("The restaurant's name is " + self.restaurant_name)
        print("The cuisine's type is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")


restaurant_1 = Restaurant('一盏灯', '湘菜')
restaurant_2 = Restaurant('海底捞', '川菜')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()

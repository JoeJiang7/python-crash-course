class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """描述餐厅的名字和菜品"""

        print(self.name)
        print(self.type)

    def open_restaurant(self):
        print(self.name.title() + " is open")


restaurant1 = Restaurant('一盏灯', '湘菜')
restaurant2 = Restaurant('海底捞', '川菜')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

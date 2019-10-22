class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("餐馆正在营业。")


restaurant1 = Restaurant('KFC','fast food')
restaurant2 = Restaurant('Quanjude', 'Peking Duck')
restaurant3 = Restaurant('Shaxian County snacks','snacks')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

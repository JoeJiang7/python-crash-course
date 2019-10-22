def make_car(brand, type, **car_info):
    car_profile = {}
    car_profile['brand'] = brand
    car_profile['type'] = type
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile
car = make_car('sabaru','outback',color = 'blue', two_package = True)
print(car)
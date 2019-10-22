def make_pizza(*toppings):
    print("Making a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('pepperoni','green peppers',)
make_pizza('extra cheese','pepperoni','green peppers',)
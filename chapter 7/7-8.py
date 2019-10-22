sandwich_orders = ['beacon','pastrami','tuna']
finished_sanwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sanwiches.append(current_order)
    print("I made your " + current_order)
print("Those sandwiched have been finished")
for finished_sandwich in finished_sanwiches:
    print(finished_sandwich)
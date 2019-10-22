import matplotlib.pyplot as plt
x_values = list(range(1,11))
y_values = [x**3 for x in x_values]
plt.figure(1)

fig1 = plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("x axis", fontsize=14)
plt.ylabel("y axis", fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)

plt.figure(2)
x_value = list(range(1,5001))
y_value = [x**3 for x in x_value]
fig2 = plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=5)
plt.title("Square Numbers2", fontsize=24)
plt.xlabel("x axis", fontsize=14)
plt.ylabel("y axis", fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)
plt.axis([0, 5010, 0, 125000000000])
plt.show()

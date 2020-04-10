from tabulate import tabulate

y = [46, 43, 41, 30, 35, 19, 37, 14, 2, 41, 45, 22, 5, 17]
x = [10, 13, 15, 25, 20, 35, 18, 40, 51, 15, 11, 32, 48, 37]
sum_x = sum(x)
sum_y = sum(y)
avg_x = sum(x) / len(x)
avg_y = sum(y) / len(y)

xy = [a * b for a,b in zip(x,y)]
sum_xy = sum(xy)
avg_xy = sum(xy) / len(xy)

x_squared = [i ** 2 for i in x]
sum_x_sqd = sum(x_squared)
avg_x_sqd = sum(x_squared) / len(x_squared)

a = (avg_xy - avg_x * avg_y) / (avg_x_sqd - avg_x ** 2)
b = avg_y - a * avg_x

phi = [a * x[i] + b for i in range(len(y))]

epsilon = [abs((y[i] - phi[i]) / y[i]) for i in range(len(y))]
avg_epsilon = sum(epsilon) / len(epsilon)

table = [['x',x ,'Σ',sum_x,'1/nΣ',avg_x],
         ['y',y,'Σ',sum_y,'1/nΣ',avg_y],
         ['x**2',x_squared,'Σ',sum_x_sqd,'1/nΣ',avg_x_sqd],
         ['x*y',xy, 'Σ', sum_xy, '1/nΣ', avg_xy],]

print(tabulate(table,tablefmt='pipe'))
print(tabulate([['φ', float(str(elem)[:7])] for elem in phi], tablefmt='pipe'))
print('Ɛ = ' + str(avg_epsilon))
    
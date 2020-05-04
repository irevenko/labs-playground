#f_row - first row 
# s_row - second 
# th_row - third 
# fr_row - fourth

f_row = [11, 2.6, 0.4, -3.3, 51.27]
s_row = [-4.1, 22, 2.2, -3.5, -64.66]
th_row = [-1.2, -15.7, 33, -0.1, -104.96]
fr_row = [-7.7, -6.3, 4.8, 44, -27.12]


matrix_norm = max( f_row[1] + f_row[2] + f_row[3] / f_row[4],
                   s_row[0] + s_row[2] + s_row[3] / s_row[4],
                   th_row[0] + th_row[1] + th_row[3] / th_row[4],
                   fr_row[0] + fr_row[1] + fr_row[2] / fr_row[4]
 )  

x0 = f_row[4] / f_row[0], s_row[4] / s_row[1], th_row[4] / th_row[2], fr_row[4] / fr_row[3]

print(f_row)
print(s_row)
print(th_row) 
print(str(fr_row) + "\n")
print("||M|| = " + str(matrix_norm)[:7])
print("x0 = " + str(x0))

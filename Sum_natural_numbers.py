# Python Program for Sum of squares of first n natural numbers

def natural_number(end_num):
    value=0
    for num in range(1,(end_num+1)):
        value=value+((num)**2)
    return value
n_n=natural_number(5)
print(n_n)
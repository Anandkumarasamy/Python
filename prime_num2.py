import os
def prime_num(num):
    if num%2 == 0:
        print(num,'is non prime number')
        exit()
    else:
        for val in range(num): 
            if val > 1: 
                for n in (2, val//2 + 2): 
                    if (val % n) == 0: 
                        break
                    else: 
                        if n == val//2 + 1: 
                            print(num,'is prime number')
prime_num(14)
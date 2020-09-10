#Python Program for Fibonacci numbers

def fibonacci(num):
    pre_num=0
    af_num=1
    cur_num=0
    for iter_num in range(num):
        if iter_num<=1:
            continue
        cur_num=pre_num+af_num
        pre_num=af_num
        af_num=cur_num
        if cur_num == num:
            print(num,'is fibonacci number')
            break
        else:
            if cur_num > num:
                print(num,'is not fibonacci number')
                break
        continue
fibonacci(19)
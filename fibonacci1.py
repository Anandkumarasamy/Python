#Python Program for n-th Fibonacci number

def fibonacci(end_num):
    pre_num=0
    af_num=1
    cur_num=0
    for num in range(end_num):
        if num<=1:
            print(num)
            continue
        cur_num=pre_num+af_num
        print(cur_num)
        pre_num=af_num
        af_num=cur_num
        if cur_num > end_num:
            break
        continue
fibonacci(512)
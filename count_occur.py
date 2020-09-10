# Python | Count occurrences of an element in a list

def count_occurrences(lis,sample_num):
    count=0
    for num in lis:
        if num == sample_num:
            count=count+1
    print(count)
count_occurrences([8, 6, 8, 10, 8, 20, 10, 8, 8],16)

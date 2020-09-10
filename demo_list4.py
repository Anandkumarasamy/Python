import random
import itertools

grocery = ['bread', 'milk', 'butter']
random.shuffle(grocery)
print(grocery)

result1=enumerate(grocery,10)
result2=enumerate(grocery)
print(list(result1))
print(list(result2))

result3=itertools.permutations(grocery)
print(list(result3))

original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)


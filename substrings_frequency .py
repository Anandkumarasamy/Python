'''Input : test_str = “ababa”
Output : {‘a’: 3, ‘ab’: 2, ‘aba’: 2, ‘abab’: 1, ‘ababa’: 1, ‘b’: 2, ‘ba’: 2, ‘bab’: 1, ‘baba’: 1}
Explanation : All substrings with their frequency extracted.

Input : test_str = “GFGF”
Output : {‘G’: 2, ‘GF’: 2, ‘GFG’: 1, ‘GFGF’: 1, ‘F’: 2, ‘FG’: 1, ‘FGF’: 1}
Explanation : All substrings with their frequency extracted.'''
test_str = "abababa"
temp_str=''
count=0
for char in test_str:
    temp_str=temp_str+char
    count=test_str.count(temp_str)
    

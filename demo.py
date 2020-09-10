
#Write a Python program to convert a roman numeral to an integer.
class Roman():
    count=0
    roman_num=''
    def __init__(self):
        self.val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        self.syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    def int_to_roman(self,num):
        while num > 0:
            for iter in range(num//self.val[Roman.count]):
                Roman.roman_num=Roman.roman_num+self.syb[Roman.count]
                num=num-self.val[Roman.count]
            Roman.count=Roman.count+1
        return Roman.roman_num
    def roman_to_int(cls,rom):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_num=0
        for iter in range(len(rom)):
            if iter > 0 and rom_val[rom[iter]] > rom_val[rom[iter-1]]:
                int_num=int_num+rom_val[rom[iter]]-(2*rom_val[rom[iter-1]])
            else:
                int_num=int_num+rom_val[rom[iter]]
        return int_num
        
result=Roman()
print(result.int_to_roman(150))
print(result.roman_to_int(XCIV))
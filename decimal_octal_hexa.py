def print_formatted(number):
    # your code goes here
    octal_tens_count=0
    octal_unit_count=0
    hexa_tens_count=0
    hexa_unit_count=0
    num=0
    for i in range(1,number+1):
        decimal=i
        
        octal_unit_count=octal_unit_count+1
        if octal_unit_count == 8:
            octal_unit_count=0
            octal_tens_count=octal_tens_count+1
            octal=int(str(octal_tens_count)+str(octal_unit_count))
        else:
            octal=int(str(octal_tens_count)+str(octal_unit_count))
        
        #hexa_unit_count=hexa_unit_count+1
        if type(hexa_unit_count) is int:
            hexa_unit_count=hexa_unit_count+1
        else:
            hexa_unit_count=ord(hexa_unit_count)-55+1
        if 10 <= hexa_unit_count <= 16:
            if 10 <= hexa_unit_count <= 15:
                hexa_unit_count=chr(65+num)
                num=num+1
            if hexa_unit_count == 16:
                num=0
                hexa_unit_count=0
                hexa_tens_count=hexa_tens_count+1
                hexa=int(str(hexa_tens_count)+str(hexa_unit_count))
            else:
                if hexa_tens_count==0:
                    hexa=str(hexa_unit_count)
                else:
                    hexa=str(hexa_tens_count)+str(hexa_unit_count)        
        else:
            hexa=int(str(hexa_tens_count)+str(hexa_unit_count))

        
        
        print("{} {} {}".format(decimal,octal,hexa))

print(print_formatted(17))
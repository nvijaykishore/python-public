word ={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
       10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
       17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",
       50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"thousand",
       100000:"lakh",10000000:"crore"}

word_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,100,
             100000,10000000]

multi = {0:0,1:1,2:10,3:100,4:1000,5:10000,6:100000,7:1000000,8:10000000}

number = input("Enter a number to convert to words :")

new_num = int(number)
arr_len = int(len(number))
divisor = multi[arr_len]


word_num = " "

if new_num in word_list:
    word_num += word[new_num]
else:
    for num in range(arr_len):
    #print(number[num])
        ans = int(int(number)/divisor)
        rem = int(number) % divisor
        #if re
            
        word_num += (word[ans] + " ") + word[multi[arr_len]] + " "
        number = rem
        arr_len -= 1
        divisor = multi[arr_len]


print(word_num)
        
    
    
    
    
    
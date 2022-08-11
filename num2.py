word ={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
       10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
       17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",
       50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"thousand",
       100000:"lakh",10000000:"crore"}

word_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,100,
             100000,10000000]

multi = {0:0,1:1,2:10,3:100,4:1000,5:10000,6:100000,7:1000000,8:10000000}
new_word = ""
number = input("Enter a number to convert to words :")

word_len = len(number)
for num in number:
    if int(number) < 21:
        new_word += word[int(number)]
        
    elif int(number) < 100:
        if int(number)/10 == 0:
            new_word += word[int(number)]
            
        else:
            ans = int(int(number)/10)
            rem = int(int(number)%10)
            new_word += word[ans*10]
            new_word += word[rem]
        
    
    else:
        new_word += word[int(num)] + " " + word[int(multi[int(word_len)])] + " "
        word_len -= 1
        
print(new_word)



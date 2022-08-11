alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = "civilization"
shift = 5
new_word =""

for n in range(len(text)):
    idx = alphabet.index(text[n])
    new_num = int(idx+shift)
    if new_num >= 25:
        new_num = new_num - 26
    
    new_word += alphabet[new_num]
               
               
print(new_word)
        
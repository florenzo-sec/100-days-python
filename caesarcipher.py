from string import ascii_lowercase

print(r'''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          ''')
print(r'''
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             ''')

print("Welcome to the Caesar Cipher Encoder/Decoder!")
key = int(input("Please enter the key (a number from 1 to 25): "))
mode = input("Type 'e' to encode or 'd' to decode: ").lower()
text = input("Enter your message: ")

def cipher(text, key, mode):
    result = ""
    for char in text:   
        if char.isalpha():
            char_index = ascii_lowercase.index(char.lower())
            #new_index calculation based on mode, if e it adds key, if d it subtracts key
            new_index = (char_index + key) % 26 if mode == 'e'.strip() else (char_index - key) % 26
            result += ascii_lowercase[new_index]
        else:
            result += char
    return result           
        
print(f"The resulting message is: {cipher(text, key, mode)}")
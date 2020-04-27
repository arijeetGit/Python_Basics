'''
Code to encrypt any text.
Each alphabet will be encrypted to its next alphabet.
For Example :- 'MAN' will be encrypted to as 'NBO'.
'''
encrypt = input('Enter text to encrypt : ')
encrypt = encrypt.lower().replace(" ", "")
for i in encrypt:
    print(chr(ord(i) + 1),end= " ")
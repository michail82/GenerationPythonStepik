# put your python code here
n = int (input())
text = input()
for letter in text:
    decryption = ord(letter) - n
    if decryption < 97:
        decryption += 26
    print(chr(decryption),end='')
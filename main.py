''' things I need 
try to import paperclip
a list of symbols
Ask if the the user wants to encrypt or decrypt
ask the user which key to use
let the user enter the message to decrypt or encrypt
dycrypt or encrypt message 
'''

try: 
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt!')
    response = input('>')
    if response.lower() == 'e':
        mode = 'encrypt'
        break
    elif response.lower() == 'd':
        mode = 'decrypt'
        break

while True:
    maxKey = len(SYMBOLS) - 1
    print('Please select a key (0 - {}) to use'.format(maxKey))
    response = input('>').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message you want to {}'.format(mode))
message = input('>')
message = message.upper()
 
translated = ' '
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num > len(SYMBOLS):
            num = num -len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol
    
print(translated)


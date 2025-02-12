import tkinter as tk
import random as rand

# TODO: MAKE THE DAMN THING

def encrypt():

    print('yo')
    uie_list = []
    uie_list_e = []
    key = rand.randint(5000,10000)
    sub = rand.randint(1,5000)

    uie = input('what do you wish to encrypt?: ')
    uie_list = list(uie)

    for i in uie_list:
        char = ord(i)
        char = char * key
        char -= sub
        uie_list_e.append(char)
    
    print('key: ' + str(key))
    print('sub: ' + str(sub))
    print(uie_list_e)




def decrypt():

    uid = input('what do you wish to decrypt? (NO BRACKETS!): ')
    key = input('input key: ')
    sub = input('input sub: ')

    uid_list = uid.split()
    uid_list_nc = [i.replace(',','') for i in uid_list]
    uid_list_d = []

    for i in uid_list_nc:

        char = int(i) + int(sub)
        char = char / int(key)
        char = chr(int(char))

        uid_list_d.append(char)


    uid_decrypted = "".join(uid_list_d)
    print(uid_decrypted)


q = input('encrypt(e) or decrypt(d)?: ')

if q == 'e':
    encrypt()
elif q == 'd':
    decrypt()
else:
    print('invalid input. closing...')
import tkinter as tk
import random as rand

# TODO: MAKE THE DAMN THING

def encrypt():

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

    # new bit from home

    uie_list_e_split = [int(digit) for number in uie_list_e for digit in str(number)]
    tempList = []

    for x in uie_list_e_split:
        tempList.append(chr(x + 48))
    final_e = ''.join(tempList)


    # end of new bit
    
    print('key: ' + str(key))
    print('sub: ' + str(sub))
    print(final_e)




def decrypt():

    uid = input('what do you wish to decrypt?: ')
    key = input('input key: ')
    sub = input('input sub: ')

    # NEW BIT, CONVERT BACK INTO THING

    temp1 = list(uid)
    uid_list_nc = []
    for s in temp1:
       # print(str(int(s) + 48))
        uid_list_nc.append(chr((int(s) + 48)))
    #print(uid_list_nc)

    chunks = [uid_list_nc[i:i+6] for i in range(0, len(uid_list_nc), 6)]

    # Convert each chunk into a number
    result_chunks = [int(''.join(map(str, chunk))) for chunk in chunks]

    # DONE WITH NEW BIT

    '''uid_list = uid.split()
    uid_list_nc = [i.replace(',','') for i in uid_list]'''
    uid_list_d = []

    for i in result_chunks:

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

    # idea ; turn 3 parts of the 6 digit string into letters and then booyah skedoosh
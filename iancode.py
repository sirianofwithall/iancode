import random as rand
import time as time

# Hello Mr. Levine !!! 
# I just thought u might find this cool so im gonna send it to u

# HOW IT WORKS

# - generates a key (multiplies the characters unicode value)
# - generates the 'sub' (subtracts that from the multiplied value)
# - combines the 2 into one key (key_s)
# - takes each character in the encrypted string and uses that +48 to get a new number which is its inverse unicode value or something (the other way)
# - also it splits each character into a 6 digit integer using the key and sub, and if it ends up being 7 (which will offset the whole thing) it just generates a new one.
# - combines the list into 1 string

# decrypts by splitting it into a list of 6 digit strings, then by reversing everything given the sub and key :)    

def encrypt():

    uie = input('what do you wish to encrypt?: ')
    uie_list = list(uie)
    time_start = time.time()

    def generate_encryption():

        uie_list_e = []
        key = rand.randint(5000,10000)
        sub = rand.randint(1000,5000)
        key_sub = int(str(key) + str(sub))

        for i in uie_list:
            char = ord(i)
            char = char * key
            char -= sub
            if len(str(char)) == 6:
                uie_list_e.append(char)
                success = True
            else:
                success = False
                print('encryption failed, retrying..')
                generate_encryption()
                break

        uie_list_e_split = [int(digit) for number in uie_list_e for digit in str(number)]
        tempList = []

        for x in uie_list_e_split:
            tempList.append(chr(x + 48))
        final_e = ''.join(tempList)
        
        if success == True:
            time_end = time.time()
            print('----------')
            print('Encryption completed in ' + str(time_end - time_start) + ' seconds' )
            print('key_s: ' + str(key_sub))
            print('Encrypted string: ' + final_e)
            print('----------')

    generate_encryption()




def decrypt():

    uid = input('what do you wish to decrypt?: ')
    key_s = input('input key_s: ')
    # turn key_s back into a key and sub
    keylist = list(key_s)
    tempKeyList = []
    tempSubList = []

    for k in range(0,4):
        tempKeyList.append(keylist[k])

    key = ''.join(tempKeyList)

    for s in range(4,8):
        tempSubList.append(keylist[s])
    
    sub = ''.join(tempSubList)


    # done with dat
    time_start = time.time()
    temp1 = list(uid)
    uid_list_nc = []

    for s in temp1:

        uid_list_nc.append(chr((int(s) + 48)))

    chunks = [uid_list_nc[i:i+6] for i in range(0, len(uid_list_nc), 6)]
    result_chunks = [int(''.join(map(str, chunk))) for chunk in chunks]
    uid_list_d = []

    for i in result_chunks:

        char = int(i) + int(sub)
        char = char / int(key)
        char = chr(int(char))

        uid_list_d.append(char)


    uid_decrypted = "".join(uid_list_d)
    time_end = time.time()
    print('----------')
    print('Decryption completed in ' + str(time_end - time_start) + ' seconds')
    print('Decrypted string: ' + uid_decrypted)
    print('----------')

print('Hello and welcome to UMUSU Encryption and Decryption! (Unicode Multiply and Subtract) - clever name thanks i made it myself')
print('Please choose an option.')
print('----------')
q = input('encrypt(e) or decrypt(d)?: ')

if q == 'e':
    encrypt()
elif q == 'd':
    decrypt()
else:
    print('invalid input. closing...')

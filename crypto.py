# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string
import math

def encrypt ( strng ):
    L = len(strng)
    encrypt_strng = ''
    M = (math.floor(math.sqrt(L))+1)**2
    if M == L:
        pad_strng = strng
    elif M!=L:
        pad_strng = strng + ('*' * (M-L))
    #print(M)   
    K = int(math.sqrt(M))
    x= pad_strng.split()
    pad_table = [[0 for col in range(K)]\
                for row in range(K)]
    sec_table = [[0 for col in range(K)]\
                for row in range(K)]
    index_num = 0
    for col in range(K):
        for row in range(K):
            pad_table[col][row] = pad_strng[index_num]
            index_num += 1
    #print(pad_table)
    sec_index = 0
    new_index = -(K-1)
    for col in range(K):
        for row in range(K):
            
            sec_table[row][int(math.fabs(col+new_index))] = pad_strng[sec_index]
            sec_index += 1
    for col in range(K):
        for row in range(K):
            encrypt_strng = encrypt_strng + sec_table[col][row]
    #encrypt_strng.strip('*')        
    #if encrypt_strng.count('*') > 0:
        #encrypt_strng.replace('*','')
       
   
    #print(sec_table[0][3])
    return encrypt_strng
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    pad_strng = strng
    #print(pad_strng)
    decrypt_strng = ''
    dec_index = 0
    L = len(strng)
    if  math.sqrt(L)  == (math.floor(math.sqrt(L))):
        M = L
        #M = (math.floor(math.sqrt(L))+1)**2
    else:
        print("test")
        M = (math.floor(math.sqrt(L))+1)**2
        #L = M
    print(M)
    '''if M == L:
        pad_strng = strng
    elif M!=L:
        pad_strng = strng + ('*' * (M-L))'''
    print(pad_strng)
    K = int(math.sqrt(M))
    print(K)
    new_index = -(K-1)
    sec_table = [[0 for col in range(K)]\
                for row in range(K)]
    
    '''for col in range(K):
        for row in range(K-1):
            if dec_index <= M-1:
                #print(dec_index)
                sec_table[col][row] = pad_strng[dec_index]
            dec_index += 1'''
    #print(sec_table)
    i=0
    crypt_dex = 0
    hi = ('*')
    bi = 0
    test_strng = ''
    while i < K-1:
        
        if L == M:
            pad_strng = pad_strng
        elif L!=M:
            pad_strng = pad_strng + ('*'*(M-L))
            '''while bi< M:
                if bi%K == 0 and bi != 0:
                    pad_strng.insert(bi, ('*'))  + pad_strng[K:] #* (M-L))
                bi += 1'''
            
        print(test_strng)    
        for col in range(K):
            
            for row in range(K):
                #print(pad_strng)
                '''print(crypt_dex)
                print('col',col)
                print('row',row)'''
            #if crypt_dex < L:
                #print("test")
                sec_table[row][int(math.fabs(col+new_index))] = pad_strng[crypt_dex]
                crypt_dex += 1
            #else:
                #break
        for col in range(K):
            for row in range(K):
            #if sec_table[col][row] != 0:
                decrypt_strng = decrypt_strng + str(sec_table[col][row])
                #decrypt_strng = decrypt_strng.replace('*','')
        pad_strng = pad_strng.replace(pad_strng,decrypt_strng.replace('*',''))
        #pad_strng = pad_strng + decrypt_strng
        #pad_strng.rstrip(decrypt_strng)
        '''print(pad_strng)
        print(decrypt_strng)
        print(sec_table)'''
        print(pad_strng)
        decrypt_strng= ''
        i += 1
        crypt_dex = 0
            #int(math.fabs(row+new_index))(col-row)-1
    '''print(sec_table)
    for col in range(K):
        for row in range(K):
            #if sec_table[col][row] != 0:
            decrypt_strng = decrypt_strng + str(sec_table[col][row])'''

    return pad_strng

def main():
    strng = input('enter')
    sec_strng = input('enter')
    print(encrypt(strng).replace('*',''))
    print(decrypt(sec_strng).replace('*',''))
  # read the two strings P and Q from standard imput

  # encrypt the string P

  # decrypt the string Q
    
  # print the encrypted string of P and the 
  # decrypted string of Q to standard out

if __name__ == "__main__":
  main()

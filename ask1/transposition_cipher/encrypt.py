import sys
def rearrange_list(cipher, int_keyword, keyword_len):
    #sort list based on the keyword
    for i in range(keyword_len):
        for j in range(keyword_len):
            if int_keyword[i] < int_keyword[j]:
                int_keyword[i], int_keyword[j] = int_keyword[j], int_keyword[i]
                cipher[i], cipher[j] = cipher[j], cipher[i]
    return cipher
def add_hash(cipher, keyword_len):
    for i in range(keyword_len):
        if len(cipher[i]) < len(cipher[0]):
            cipher[i] += '#'
    
def clear_text(plaintext):
    clear_text = ''
    for char in plaintext:
        if char.isalpha():
            clear_text += char
    return clear_text

def transposition_cipher(keyword, plaintext):
    plaintext = clear_text(plaintext)
    keyword_len = len(keyword)
    int_keyword = [0] * keyword_len
    for i in range(keyword_len):
        int_keyword[i] = ord(keyword[i])
    cipher = [''] * keyword_len

    count = 0
    for char in plaintext:
        cipher[count] += char
        count += 1
        if count == keyword_len:
            count = 0
    add_hash(cipher, keyword_len)
    print ("Before sorting")
    for i in range(keyword_len):
        print(int_keyword[i] ,cipher[i])
    cipher=rearrange_list(cipher, int_keyword, keyword_len)
    print ("After sorting")
    for i in range(keyword_len):
        print(int_keyword[i] ,cipher[i])
    #print cipher with its visual representation 
   
    return cipher

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 encrypt.py <keyword> <plaintext>")
        sys.exit(1)

    keyword = sys.argv[1]
    plaintext = sys.argv[2]
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    cipher = transposition_cipher(keyword, plaintext)

    if cipher != None:
        i = len(cipher)-1
        while i >= 0:
            print(cipher[i], end = '')
            i -= 1
        print('')
    else:
        print("Error in encryption")
import sys

def rearrange_list(plain, sorting_steps):
    #reverse the sorting steps to get the original order
    sorting_steps.reverse()
    for i in range(len(sorting_steps)):
        plain[sorting_steps[i][0]], plain[sorting_steps[i][1]] = plain[sorting_steps[i][1]], plain[sorting_steps[i][0]]
    return plain

def keyword_sort_map(int_keyword, keyword_len):
    sorting_steps = []
    for i in range(keyword_len):
        for j in range(keyword_len):
            if int_keyword[i] < int_keyword[j]:
                int_keyword[i], int_keyword[j] = int_keyword[j], int_keyword[i]
                sorting_steps.append([i, j])
    return sorting_steps

def decrypt_transposition_cipher(keyword, ciphertext):
    keyword_len = len(keyword)
    int_keyword = [0] * keyword_len
    for i in range(keyword_len):
        int_keyword[i] = ord(keyword[i])
    plain = [''] * keyword_len

    flag = int(len(ciphertext) / keyword_len) + (len(ciphertext) % keyword_len > 0)
    i=0
    for char in ciphertext:
        plain[i] += char
        flag -= 1
        if flag == 0:
            i += 1
            flag = int(len(ciphertext) / keyword_len) + (len(ciphertext) % keyword_len > 0)   
    plain.reverse()
    sorting_steps=keyword_sort_map(int_keyword, keyword_len)
    plain=rearrange_list(plain, sorting_steps)
    return plain

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 decrypt.py <keyword> <ciphertext>")
        sys.exit(1)

    keyword = sys.argv[1]
    ciphertext = sys.argv[2]
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    plain = decrypt_transposition_cipher(keyword, ciphertext)

    if plain != None:
        # print the first row of letter and then the next row until the end
        for i in range(len(plain[0])):
            for j in range(len(plain)):
                if plain[j][i] != '#':
                    print(plain[j][i], end = '') 
        print('')
    else:
        print("Error in encryption")
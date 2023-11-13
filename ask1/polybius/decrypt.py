import sys
# 5x5 Polybius Square array
polybius_square = [
        ['X', 'Y', 'A', 'B', 'C'],
        ['D', 'E', 'F', 'G', 'H'],
        ['I', 'Z', 'K', 'L' , 'M'],
        ['N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W']
    ]

def polybiusDecrypt(cipher_text):
    #read cipher text 2 by 2 and find the corresponding character in the polybius square
    plain = ""
    for i in range(0, len(cipher_text), 2):
        row = int(cipher_text[i]) - 1
        col = int(cipher_text[i+1]) - 1
        plain += polybius_square[row][col]
        print("row: ", row, "col: ", col, "char: ", polybius_square[row][col])
    return plain

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 decrypt.py <plain text>")
    cipher_text = sys.argv[1]
    print("polybius Square: ")
    for i in range(5):
        print(polybius_square[i])
    print("Cipher Text: ", cipher_text)
    plain=polybiusDecrypt(cipher_text)
    print("Plain Text: ", plain)

import sys
# 5x5 Polybius Square array
polybius_square = [
        ['X', 'Y', 'A', 'B', 'C'],
        ['D', 'E', 'F', 'G', 'H'],
        ['I', 'Z', 'K', 'L' , 'M'],
        ['N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W']
    ]

def polybiusCipher(plain_text):
    latin_characters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    cipher = ""
    plain_text = plain_text.upper()
    for char in plain_text:
        if char in latin_characters:
            print("char: ", char, end="")
            if char == 'J':
                char = 'I'
            for i in range(5):
                for j in range(5):
                    if char == polybius_square[i][j]:
                        print(" i: ", i+1, "j: ", j+1)
                        cipher += str(i+1) + str(j+1)
    return cipher

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 encrypt.py <plain text>")
    plain_text = sys.argv[1]
    print("polybius Square: ")
    for i in range(5):
        print(polybius_square[i])
    print("Plain Text: ", plain_text)
    cipher=polybiusCipher(plain_text)
    print("Cipher Text: ", cipher)

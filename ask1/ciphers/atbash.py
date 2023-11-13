latin_characters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def atbash_cipher(message):
    lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

    cipher = ''
    for char in message:
        if(char in latin_characters):
            cipher += lookup_table[char]
        else:
            cipher += char
 
    return cipher

def encrypt_atbash(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            plaintext = file.read()

        ciphertext = atbash_cipher(plaintext.upper())

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(ciphertext)

        print(f"Encryption successful. Output written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        encrypt_atbash(input_file_path, output_file_path)

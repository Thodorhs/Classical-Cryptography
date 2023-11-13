import sys

def polybiusCipher(input_path, output_file):
    latin_characters = set('abcdefghijklmnopqrstuvwxyz')
    s = ""
    # open file
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            file_content = file.read().lower()
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        file.close()
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        file.close()
        return
    for char in file_content:
        if char in latin_characters:
            # finding row of the table
            row = int((ord(char) - ord('a')) / 5) + 1

            # finding column of the table 
            col = ((ord(char) - ord('a')) % 5) + 1

            # if character is 'k'
            if char == 'k':
                    row = row - 1
                    col = 5 - col + 1
                    
            # if character is greater than 'j'
            elif ord(char) >= ord('j'):
                    if col == 1 :
                        col = 6
                        row = row - 1
                        
                    col = col - 1
            s += str(row) + str(col)
        else:
            s += char
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write(s)
        except FileNotFoundError:
            print(f"Error: File '{output_file}' not found.")
            outfile.close()
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            outfile.close()
            return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 polybius.py <input_path> <output_file>")
    input_path = sys.argv[1]
    output_file = sys.argv[2]
    polybiusCipher(input_path, output_file)

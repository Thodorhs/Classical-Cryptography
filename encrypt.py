import sys

def encrypt(input_file_path, output_folder_path):

    return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 encrypt.py <input_file_path> <output_folder_path>")
    else:
        input_file_path = sys.argv[1]
        output_folder_path = sys.argv[2]
        encrypt(input_file_path, output_folder_path)
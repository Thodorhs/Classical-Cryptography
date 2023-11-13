import sys
import csv

def count_2_digit_numbers(input_file_path):
    result = {}
    with open(input_file_path, 'r') as input_file:
        s = input_file.read()
        current_number = ''
        for char in s:
            if char.isdigit():
                current_number += char
                if len(current_number) == 2:
                    num = int(current_number)
                    result[num] = result.get(num, 0) + 1
                    current_number = ''
            else:
                current_number = ''
    return result

def write_to_csv(output_file_path, freq_dict):
    with open(output_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['num', 'count']) 

        for num in sorted(freq_dict.keys()):
            csv_writer.writerow([num, freq_dict[num]])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 num_freq.py <input_file> <output_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    freq_dict = count_2_digit_numbers(input_file_path)

    write_to_csv(output_file_path, freq_dict)

    print(f"Results written to {output_file_path}")

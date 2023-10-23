import sys
import csv
from collections import Counter

def count_latin_characters(input_file_path, output_csv_path):
    latin_characters = set('abcdefghijklmnopqrstuvwxyz')
    character_counts = Counter()

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file
            content = file.read().lower()

            # Count the frequency of each Latin character
            for char in content:
                if char in latin_characters:
                    character_counts[char] += 1
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Write the character frequencies to a CSV file
    try:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Character', 'Frequency'])

            for char, frequency in character_counts.items():
                csv_writer.writerow([char, frequency])

        print(f"Latin character frequencies saved to '{output_csv_path}'.")
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 plain_freq.py <input_file_path> <output_csv_path>")
    else:
        input_file_path = sys.argv[1]
        output_csv_path = sys.argv[2]
        count_latin_characters(input_file_path, output_csv_path)

import re
from pathlib import Path

def search_in_files(folder_path, regex_pattern):
    pattern = re.compile(regex_pattern)

    folder = Path(folder_path)

    for txt_file in folder.glob('*.txt'):
        try:
            with txt_file.open('r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if pattern.search(line):
                        print(f"Match found in {txt_file.name} (Line {line_number}): {line.strip()}")
        except Exception as e:
            print(f"Error reading {txt_file}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing .txt files: ")
    regex_pattern = input("Enter the regular expression to search for: ")
    search_in_files(folder_path, regex_pattern)
import random
import os

def generate_file():
    lines = random.randint(5, 100)
    file_name = f"file_{random.randint(1000, 9999)}.txt"
    with open(file_name, 'w') as file:
        for _ in range(lines):
            file.write(f"This is line {_ + 1}\n")
    print(f"Generated file: {file_name} with {lines} lines.")
    return file_name, lines

if __name__ == "__main__":
    generate_file()

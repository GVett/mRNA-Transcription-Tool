"Create text file parser that takes text file from data folder and passes DNA sequences into a list of strings"

file_path = 'data/sample1.txt'

def parse_text_file(file_path):
    """Parse a text file containing DNA sequences and return a list of sequences."""
    sequences = []
    with open(file_path, 'r') as file:
        for line in file:
            sequence = line.strip()
            if sequence:  # Ensure the line is not empty
                sequences.append(sequence)
    return sequences

print(parse_text_file(file_path))
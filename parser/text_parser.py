def parse_text_file(file_path):
    """Parse a text file containing DNA sequences and return a list of sequences."""
    sequences = []
    try:
        with open(file_path, 'r') as file:
            dna_string = ""
            for line in file:
                if line.startswith('>'):  # Skip header lines in FASTA format
                    continue
                elif line.startswith("Sample"):
                    continue

                sequence = line.strip()

                if sequence:  # Ensure the line is not empty
                    dna_string += sequence
                    continue
                else:
                    sequences.append(dna_string) # Add the complete DNA sequence to the list
                    dna_string = "" # Reset dna_string for the next sequence
                    continue

            sequences.append(dna_string) # Add the last DNA sequence to the list
            return sequences
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

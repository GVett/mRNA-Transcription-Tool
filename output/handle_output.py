"""Handles output formatting and display for transcription results."""
import sys

def output_sequences(sequence_list):
    """Formats and prints the list of sequences."""
    print("Transcribed Sequences:")
    for index, item in enumerate(sequence_list, start=1):
        print(f"{index}. {item}")

def output_sequences_to_file(sequence_list, filename):
    """Writes the list of sequences to a text file."""
    with open(filename, "w") as f:
        f.write("Transcribed Sequences:\n")
        for index, item in enumerate(sequence_list, start=1):
            f.write(f"{index}. {item}\n")

def try_get_sequence_by_index(sequence_list, user_input):
    """Tries to get a sequence by index from the list based on user input."""
    try:
        index = int(user_input) - 1
        if 0 <= index < len(sequence_list):
            print(f"Sequence {index + 1}: {sequence_list[index]}")
            return sequence_list[index]
        else:
            print("Invalid number. Please enter a number within the range.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def ask_for_file_write(sequence_list):
    """Asks the user if they want to save the output to a file."""
    save_to_file = input("Do you want to save the output to a file? (y/n): ").strip().lower()
    if save_to_file in ['y', 'n']:
        if save_to_file == 'y':
            filename = input("Enter the filename to save the sequences (e.g., dna_sequences.txt, mrna_sequences.txt, protein_sequences.txt): ")
            if filename.endswith('.txt'):
                output_sequences_to_file(sequence_list, filename)
                print(f"Output saved to {filename}.")
            else:
                output_sequences_to_file(sequence_list, filename + ".txt")
                print(f"Output saved to {filename}.txt.")
    else:
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def output_loop(mrna_sequence_list, dna_sequence_list, protein_sequence_list):
    """Main loop to handle output of DNA and mRNA sequences."""
    
    while True:
        print("\nChoose an option:")
        print("1. Display DNA sequences")
        print("2. Display mRNA sequences")
        print("3. Display protein sequences")
        print("4. Exit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        # DNA display options
        if choice == '1':
            print(f"Enter a number 1 through {len(dna_sequence_list)} to display a specific DNA sequence, or press Enter to display all DNA sequences.")
            user_input = input("Your choice: ")
            if user_input == "":
                output_sequences(dna_sequence_list)
            else:
                try_get_sequence_by_index(dna_sequence_list, user_input)
            ask_for_file_write(dna_sequence_list)

        # mRNA display options
        elif choice == '2':
            print(f"Enter a number 1 through {len(mrna_sequence_list)} to display a specific mRNA sequence, or press Enter to display all mRNA sequences.")
            user_input = input("Your choice: ")
            if user_input == "":
                output_sequences(mrna_sequence_list)
            else:
                try_get_sequence_by_index(mrna_sequence_list, user_input)
            ask_for_file_write(mrna_sequence_list)

        # Protein display options
        elif choice == '3':
            print(f"Enter a number 1 through {len(protein_sequence_list)} to display a specific protein sequence, or press Enter to display all protein sequences.")
            user_input = input("Your choice: ")
            if user_input == "":
                output_sequences(protein_sequence_list)
            else:
                try_get_sequence_by_index(protein_sequence_list, user_input)
            ask_for_file_write(protein_sequence_list)

        # Exit option
        elif choice == '4':
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
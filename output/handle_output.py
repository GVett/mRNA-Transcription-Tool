"""Handles output formatting and display for transcription results."""
import sys

def output_mrna_sequences(mrna_sequence_list):
    """Formats and prints the list of mRNA sequences."""
    print("Transcribed mRNA Sequences:")
    for index, mrna in enumerate(mrna_sequence_list, start=1):
        print(f"{index}. {mrna}")

def output_dna_sequences(dna_sequence_list):
    """Formats and prints the list of DNA sequences."""
    print("Parsed DNA Sequences:")
    for index, dna in enumerate(dna_sequence_list, start=1):
        print(f"{index}. {dna}")

def output_loop(mrna_sequence_list, dna_sequence_list):
    """Main loop to handle output of DNA and mRNA sequences."""
    while True:
        print("\nChoose an option:")
        print("1. Display DNA sequences")
        print("2. Display mRNA sequences")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            print("Enter a number 1 through " + str(len(dna_sequence_list)) + " to display a specific DNA sequence, or press Enter to display all DNA sequences.")
            user_input = input("Your choice: ")
            if user_input == "":
                output_dna_sequences(dna_sequence_list)
            else:
                try:
                    index = int(user_input) - 1
                    if 0 <= index < len(dna_sequence_list):
                        print(f"DNA Sequence {index + 1}: {dna_sequence_list[index]}")
                    else:
                        print("Invalid number. Please enter a number within the range.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == '2':
            print("Enter a number 1 through " + str(len(mrna_sequence_list)) + " to display a specific mRNA sequence, or press Enter to display all mRNA sequences.")
            user_input = input("Your choice: ")
            if user_input == "":
                output_mrna_sequences(mrna_sequence_list)
            else:
                try:
                    index = int(user_input) - 1
                    if 0 <= index < len(mrna_sequence_list):
                        print(f"mRNA Sequence {index + 1}: {mrna_sequence_list[index]}")
                    else:
                        print("Invalid number. Please enter a number within the range.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == '3':
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
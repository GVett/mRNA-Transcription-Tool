# DNA to mRNA Transcription Tool

A small command‑line utility for parsing DNA sequence files and converting the sequences to their corresponding mRNA form.

The program reads a FASTA‑style text file from the `data/` directory, concatenates DNA sequences split across lines, and then "transcribes" each sequence by replacing every thymine (\`t\`) with uracil (\`u\`). After transcription, an interactive menu allows the user to inspect the original DNA and resulting mRNA sequences.

## Prerequisites
- Python 3.8 or newer
- Virtual environment (recommended)

No external dependencies.

## Structure
Modular design with each specific module having a single responsibility:

1. Parsing: handles cleaning input from the FASTA-style text files
2. Transcription: swaps every thymine (\`t\`) with uracil (\`u\`)
3. Output: handles output formatting and display, outputs parsed sequences into working directory

## Running
1. Clone the repo
2. Open a terminal in the source directory and activate a virtual environment
3. Launch the tool ("python main.py")
4. Enter the name of a data file in `data/`
5. Use the following controls to navigate the menu:
  -  1 – display DNA sequences (all or a specific one)
  -  2 – display mRNA sequences (all or a specific one)
  -  3 – exit the program

## Adding data
Create a plain text file in the `data/` folder. The program understands simple FASTA-style headers and will use empty lines as start/end points for each sequence. Lines starting with \`>\` are ignored.

## Extending
You can import individual functions in your own scripts or tests to expand the functionality of this command-line util.

## Notes
- The program is case-sensitive (expects lowercase bases)
- There is minimal error handling

## TODO: 
- Support saving specific sequences to file
- Support uppercase bases
- Improve error handling

Feel free to fork or modify this utility.
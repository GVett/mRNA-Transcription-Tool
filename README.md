# DNA to mRNA Transcription Tool

A small command‑line utility for parsing DNA sequence files and converting the sequences to their corresponding mRNA form.

The program reads a FASTA‑style text file from the `data/` directory, concatenates DNA sequences split across lines, and then "transcribes" each sequence by replacing every thymine (\`t\`) with uracil (\`u\`). After transcription, an interactive menu allows the user to inspect the original DNA and resulting mRNA sequences.
from parser.text_parser import parse_text_file as parse
from transcription.dna_to_mrna import dna_to_mrna as transcribe
from output.handle_output import output_loop as output
from translation.mrna_translator import translate_mrna_to_amino_acid_chain as translate

if __name__ == "__main__":
    while True:
        text_sample = input("Enter the sample text file name (e.g., sample1.txt): ")
        file_path = f'data/{text_sample}'
        dna_sequence_list = parse(file_path)

        if dna_sequence_list:
            mrna_sequence_list = transcribe(dna_sequence_list)
            amino_acid_sequence_list = translate(mrna_sequence_list)
            output(mrna_sequence_list, dna_sequence_list, amino_acid_sequence_list)
        else:
            print("No DNA sequences were parsed. Please check the file and try again.")
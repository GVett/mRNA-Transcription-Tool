def dna_to_mrna(dna_sequence_list):
    """Convert a list of DNA sequences to mRNA sequences by replacing 't' with 'u'."""
    mrna_sequences = []
    for dna_sequence in dna_sequence_list:
        mrna_sequence = dna_sequence.replace('t', 'u')
        mrna_sequences.append(mrna_sequence)
    return mrna_sequences
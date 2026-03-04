def separate_into_codons(mrna_sequences):
    """Convert mRNA sequence(s) into lists of codons."""

    # allow a single sequence to be passed
    if isinstance(mrna_sequences, str):
        mrna_sequences = [mrna_sequences]

    codon_lists = []
    for seq in mrna_sequences:
        seq = seq.lower()
        codons = []
        # take groups of 3, ignore trailing bases
        for i in range(0, len(seq) - (len(seq) % 3), 3):
            codon = seq[i:i+3]
            codons.append(codon)
        codon_lists.append(codons)

    return codon_lists

def translate_codons_to_amino_acids(codon_lists):
    """Translate one or more codon lists to protein sequences."""

    # standard genetic code
    codon_table = {
        'uuu': 'F', 'uuc': 'F', 'uua': 'L', 'uug': 'L',
        'cuu': 'L', 'cuc': 'L', 'cua': 'L', 'cug': 'L',
        'auu': 'I', 'auc': 'I', 'aua': 'I', 'aug': 'M',
        'guu': 'V', 'guc': 'V', 'gua': 'V', 'gug': 'V',
        'ucu': 'S', 'ucc': 'S', 'uca': 'S', 'ucg': 'S',
        'ccu': 'P', 'ccc': 'P', 'cca': 'P', 'ccg': 'P',
        'acu': 'T', 'acc': 'T', 'aca': 'T', 'acg': 'T',
        'gcu': 'A', 'gcc': 'A', 'gca': 'A', 'gcg': 'A',
        'uau': 'Y', 'uac': 'Y', 'uaa': '*', 'uag': '*',
        'cau': 'H', 'cac': 'H', 'caa': 'Q', 'cag': 'Q',
        'aau': 'N', 'aac': 'N', 'aaa': 'K', 'aag': 'K',
        'gau': 'D', 'gac': 'D', 'gaa': 'E', 'gag': 'E',
        'ugu': 'C', 'ugc': 'C', 'uga': '*', 'ugg': 'W',
        'agu': 'S', 'agc': 'S', 'aga': 'R', 'agg': 'R',
        'ggu': 'G', 'ggc': 'G', 'gga': 'G', 'ggg': 'G'
    }

    amino_acids = []
    for codons in codon_lists:
        aa_seq = ''
        for codon in codons:
            aa_seq += codon_table.get(codon, '?')
        amino_acids.append(aa_seq)
    return amino_acids  

def translate_mrna_to_amino_acid_chain(mrna_input):
    """Convert mRNA sequence(s) to protein sequence(s)."""

    codon_lists = separate_into_codons(mrna_input)
    amino_acids = translate_codons_to_amino_acids(codon_lists)

    if isinstance(mrna_input, str):
        return amino_acids[0] if amino_acids else ''
    return amino_acids
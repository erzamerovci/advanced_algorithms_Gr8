
mutation_patterns = ["ATGCCTAG", "GCTAGCTA", "TTAAGCCT"]
dna_sequences = {
    "SEQ001": "AAGCTTAAGCCTGCTAGCGATCGATCGATCGTAGCTAGCTAGCTAGC",
    "SEQ002": "ATGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC",
    "SEQ003": "ATGCCTAGGCTAGCTACGATCGATCGATCGATCGATCGATCGATCGA",
    "SEQ004": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    "SEQ005": "TTAAGCCTGCTAGCTACGATCGATCGATCGATCGATCGATCGATCG",
}

patterns_by_length = {}
for pat in mutation_patterns:
    patterns_by_length.setdefault(len(pat), set()).add(pat)

for seq_id, seq in dna_sequences.items():
    found = set()
    for length, patterns in patterns_by_length.items():
        for i in range(len(seq) - length + 1):
            substring = seq[i:i + length]
            if substring in patterns:
                found.add(substring)
    if found:
        print(f"{seq_id}: MUTATIONS FOUND - {list(found)}")
    else:
        print(f"{seq_id}: CLEAN")

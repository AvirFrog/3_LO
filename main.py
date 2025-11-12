from Bio import SeqIO
from Bio.Seq import Seq

input_file = "dna_sequence.txt"
output_file = "protein.fasta"

translated_sequences = []


for record in SeqIO.parse(input_file, "fasta"):
    dna_seq = record.seq

    protein_seq = dna_seq.translate()

    record.seq = protein_seq
    record.description = record.description + " [translated]"

    translated_sequences.append(record)

    print(f"ID: {record.id}")
    print(f"Długość DNA: {len(dna_seq)}")
    print(f"Długość białka: {len(protein_seq)}")
    print(f"Sekwencja białka: {protein_seq}\n")

SeqIO.write(translated_sequences, output_file, "fasta")
print(f"Przetłumaczone sekwencje zapisano do: {output_file}")

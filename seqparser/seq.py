# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    for i in range(len(seq)):
        rna_nucleotide = TRANSCRIPTION_MAPPING.get(seq[i])
        transcribed_seq = seq.replace(seq[i], rna_nucleotide)
    return transcribed_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    transcript = transcribe(seq)
    reverse_transcript = transcript[::-1]
    return reverse_transcript


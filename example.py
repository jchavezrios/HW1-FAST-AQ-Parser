from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fastaseq = FastaParser()
    
    # Create instance of FastqParser
    fastqseq = FastqParser()
    
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    print("FASTA Sequence:",fastaseq)
    print("Transcribed FASTA Sequence:",transcribe(fastaseq))  
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    print("FASTQ Sequence:",fastqseq)
    print("Transcribed FASTQ Sequence:",transcribe(fastqseq)) 

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print("Reverse Transcribed FASTA Sequence:",reverse_transcribe(fastaseq))

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print("Reverse Transcribed FASTQ Sequence:",reverse_transcribe(fastqseq))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()

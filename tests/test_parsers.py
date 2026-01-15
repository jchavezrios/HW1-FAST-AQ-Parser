# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Read in fasta file 
    fasta_file = 'data/test.fa'
    parser_obj = FastaParser(fasta_file)
    file_lines = [record for record in parser_obj]

    # known seq0 of fasta file
    seq0 = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    assert file_lines[0][1] == seq0, "Something is wrong - panic!"
    

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Read in fasta file
    fasta_file = 'data/test.fa' # if this was a fastq file, an AssertionError is raised
    parser_obj = FastaParser(fasta_file)
    file_lines = [record for record in parser_obj]

    assert file_lines[0][0] != None, "Ensure file is a FastA file."
    


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq_path = "data/test.fq" # Ensure this path is correct for your repo
    parser = FastqParser(fastq_path)
    
    records = list(parser)
    
    assert len(records) > 0
    # Verify the structure: (header, sequence, quality)
    header, seq, qual = records[0]
    assert isinstance(header, str)
    assert isinstance(seq, str)
    assert isinstance(qual, str)
    # In Fastq, sequence and quality strings must be the same length
    assert len(seq) == len(qual)

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fasta_path = "data/test.fa" 
    testingfastq = FastqParser(fasta_path)
    
    myfastq = list(testingfastq)
    
    if len(myfastq) > 0:
        for header, seq, qual in myfastq:
            assert header is None, "This was not ID'd as .fastq"
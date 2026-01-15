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
    # feed in data of good fasta 
    good_fasta = "data/test.fasta"
    
    # create path 
    parse1 = FastaParser(good_fasta)
    # create record of good fasta 
    good_record = list(parse1._get_record(good_fasta))
    # assertion that verifies there is data in the good test fasta file 
    assert len(good_record) > 0  
    
    # empty fasta test 
    empty_fasta = "tests/blank.fa"
    parse2 = FastaParser(empty_fasta)
    empty_record = list(parse2._get_record(empty_fasta))
    # assert that empty fasta will raise an error 
    assert len(empty_record) == 0
    
    # bad fasta test 
    bad_fasta = "tests/bad.fa"
    parse3 = FastaParser(bad_fasta)
    bad_record = list(parse3._get_record(bad_fasta))
    # assert that empty fasta will raise an error 
    assert len(bad_record) == 0
    

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fastq_path = "data/test.fastq" 
    testingfasta = FastaParser(fastq_path)
    
    for header, seq in testingfasta:
        assert header is None, "This is not a fasta file, header is @"
    


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq_path = "data/test.fastq" # Ensure this path is correct for your repo
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
    fasta_path = "data/test.fasta" 
    testingfastqq = FastqParser(fasta_path)
    
    myfastq = list(testingfastqq)
    
    if len(myfastq) > 0:
        for header, seq, qual in myfastq:
            assert header is None, "This was not ID'd as .fastq"
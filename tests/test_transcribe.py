# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    
    write in your file
    call your functions above  
    pass the input into the test functions above 
    """
    testseq = "ATGGTA"
    correct_seq = "UACCAU"
    result1 = transcribe(testseq)
    print(result1)
    assert result1 == correct_seq, "Transcription worked as expected: " + result1

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    sequence = "ATGGTC"
    expected_reverse = "GACCAU"
    result2 = reverse_transcribe(sequence)
    assert result2 == expected_reverse, "Reverse transcription worked: " + result2
    
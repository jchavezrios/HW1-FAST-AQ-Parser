import io
from typing import Tuple, Union, Iterator, Generator


class Parser:
    """
    Base Class for Parsing Algorithms
    """

    def __init__(self, filename: str):
        
        self.filename = filename
        self.store = True
        self._sequences = None

    def get_record(
        self, f_obj: io.TextIOWrapper
    ) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        Returns a sequencing record that will either be a tuple of two strings (header, sequence)
        or a tuple of three strings (header, sequence, quality).
        """
        return self._get_record(f_obj)

    def __iter__(self):
        """
        This is an overriding of the Base Class Iterable function. All classes in python
        have this function, but it is not implemented for all classes in python.

        # Note on the `__iter__` method
            Generally one doesn't call this method directly as `obj.__iter__()`. Instead it
            lets you use the object itself as an iterable. This is really useful in OOP because it
            allows you to represent and use iterable objects very cleanly. You still can call this
            method directly, but it really takes the fun out of python...

            ## How to use the `__iter__` method
            ```
            parser_obj = Parser(filename)
            for record in parser_obj:
              # do something
            ```
        """

        nseq = 0
        # 'with open' reads the filename as f_obj
        with open(self.filename, "r") as f_obj: 
            rec = self.get_record(
                f_obj
            )  # will be a generator that yields tuples of strings

            for seq in rec:
                yield seq
                nseq += 1
            self.store = False

            if nseq == 0:
                raise ValueError(f"File ({self.filename}) had 0 lines.")

        # another way to do this with the original construction: 
        #    while True:
        #        rec = self.get_record(f_obj)
        #        yield rec 
        # is to implement for the FastaParser/FastqParser subclasses' _get_record
        # functionality where you get (with `next(f_obj)`, for example) two lines
        # at a time for the FastaParser and simply assume the first is the 
        # header and the second is the sequence, or something similar.

    def _get_record(
        self, f_obj: io.TextIOWrapper
    ) -> Iterator[Union[Tuple[str, str], Tuple[str, str, str]]]:
        """
        a method to be overridden by inherited classes.
        """
        raise NotImplementedError(
            """
                This function is not meant to be called by the Parser Class.
                It is expected to be overridden by `FastaParser` and `FastqParser`"""
        )


class FastaParser(Parser):
    """
    Fasta Specific Parsing
    """

    def _get_record(self, f_obj: io.TextIOWrapper) -> Iterator[Tuple[str, str]]:
        """
        returns the next fasta record
        """

        seq_name = None

        for idx, line in enumerate(f_obj):
            line = line.strip()
            if line == "":
                raise ValueError(f"Got an empty line for {f_obj.name} @ line {idx+1}")
            if line.startswith(">"):
                seq_name = line[1:]
                continue

            yield (seq_name, line)


class FastqParser(Parser):
    """
    Fastq Specific Parsing
    """

    def _get_record(
        self, f_obj: io.TextIOWrapper
    ) -> Generator[Tuple[str, str, str], None, None]:
        """
        returns the next fastq record
        """
        read_qual = True
        seq_name = None
        seq = None

        for idx, line in enumerate(f_obj):
            line = line.strip()
            if line == "":
                raise ValueError(f"Got an empty line for {f_obj.name} @ line {idx+1}")
            if line == "+":
                continue  # skip this line

            if line.startswith("@"):  # if its a header line, we'll store it
                seq_name = line[1:]
                continue

            if (read_qual is True):  # if read_qual is True, then we'll assume the line is a sequence
                seq = line
                read_qual = False
            else:
                # we assume that quality will always be after the seq, so if we get here and read_qual is False then we can just return the tuple
                yield (seq_name, seq, line)  # line here is the quality string
                read_qual = True
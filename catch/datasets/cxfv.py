"""Dataset with 'Culex flavivirus' sequences.

A dataset with 15 'Culex flavivirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom

__author__ = 'Hayden Metsky <hayden@mit.edu>'


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/cxfv.fasta", relative=True)
sys.modules[__name__] = ds
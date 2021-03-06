"""Dataset with 'Human betaherpesvirus 5' sequences.

A dataset with 309 'Human betaherpesvirus 5' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/human_betaherpesvirus_5.fasta.gz", relative=True)
sys.modules[__name__] = ds

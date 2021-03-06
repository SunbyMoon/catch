"""Dataset with 'Yug Bogdanovac vesiculovirus' sequences.

A dataset with 1 'Yug Bogdanovac vesiculovirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/yug_bogdanovac_vesiculovirus.fasta.gz", relative=True)
sys.modules[__name__] = ds

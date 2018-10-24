"""Dataset with 'Simian torque teno virus 34' sequences.

A dataset with 1 'Simian torque teno virus 34' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/simian_torque_teno_virus_34.fasta.gz", relative=True)
sys.modules[__name__] = ds
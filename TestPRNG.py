#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:00:00 2021

@author: alireza
"""

from LorenzSystem import PRNG
from testsuit.FrequencyTest import FrequencyTest
from testsuit.RunTest import RunTest
from testsuit.Matrix import Matrix
from testsuit.Spectral import SpectralTest
from testsuit.TemplateMatching import TemplateMatching
from testsuit.Universal import Universal
from testsuit.Complexity import ComplexityTest
from testsuit.Serial import Serial
from testsuit.ApproximateEntropy import ApproximateEntropy
from testsuit.CumulativeSum import CumulativeSums
from testsuit.RandomExcursions import RandomExcursions


prng = PRNG()
code = ''
import random as rand
for  i in range(0, 2500):
    if (i%100 == 0):
        print(i)
    prng.SetKey([-5.76 + (rand.random()/100.0),  2.27 + (rand.random()/100.0),  32.82 + (rand.random()/100.0)], 8.0/3.0 + (rand.random()/100.0), 28+ (rand.random()/100.0), 10.0+ (rand.random()/100.0))
    c = prng.generate()
    code += c

print((code.count('1') - code.count('0'))/len(code))

freq_test = FrequencyTest.monobit_test(code)
block_freq_test = FrequencyTest.block_frequency(code)
run_test = RunTest.run_test(code)
longest_run_test = RunTest.longest_one_block_test(code)
binary_mat_test = Matrix.binary_matrix_rank_text(code)
spectral_test = SpectralTest.sepctral_test(code)
non_overlapping_test = TemplateMatching.non_overlapping_test(code, False,'000000001')
overlapping_test = TemplateMatching.overlapping_patterns(code)
universal_test = Universal.statistical_test(code)
linear_complexity_test = ComplexityTest.linear_complexity_test(code)
serial_test = Serial.serial_test(code)
entropy_test = ApproximateEntropy.approximate_entropy_test(code)
cumulative_sum_forward_test = CumulativeSums.cumulative_sums_test(code, 0)
cumulative_sum_backward_test = CumulativeSums.cumulative_sums_test(code, 1)

#result = RandomExcursions.random_excursions_test(code)
#print('2.14. Random Excursion Test:')
#print('\t\t STATE \t\t\t xObs \t\t\t\t P-Value \t\t\t Conclusion')
#for item in result:
#    print('\t\t', repr(item[0]).rjust(4), '\t\t', item[1], '\t\t', repr(item[2]).ljust(14), '\t\t',
#          (item[3] >= 0.01))



from tabulate import tabulate
table = [
        ["Frequency Test", freq_test[0], bool(freq_test[1])],
        ["Block Frequency Test", block_freq_test[0], bool(block_freq_test[1])],
        ["Run Test", run_test[0], bool(run_test[1])],
        ["Run Test (Longest Run of Ones)", longest_run_test[0], bool(longest_run_test[1])],
        ["Binary Matrix Rank Test", binary_mat_test[0], bool(binary_mat_test[1])],
        ["Discrete Fourier Transform (Spectral) Test", spectral_test[0], bool(spectral_test[1])],
        ["Non-overlapping Template Matching Test", non_overlapping_test[0], bool(non_overlapping_test[1])],
        ["Overlappong Template Matching Test", overlapping_test[0], bool(overlapping_test[1])],
        ["Universal Statistical Test", universal_test[0], bool(universal_test[1])],
        
        ["Linear Complexity Test", linear_complexity_test[0], bool(linear_complexity_test[1])],
        ["Serial Test", serial_test[0][0], bool(serial_test[0][1])],
        ["Serial Test", serial_test[1][0], bool(serial_test[1][1])],
        ["Approximate Entropy Test", entropy_test[0], bool(entropy_test[1])],
        ["Cumulative Sums (Forward)", cumulative_sum_forward_test[0], bool(cumulative_sum_forward_test[1])],
        ["Cumulative Sums (Backward)", cumulative_sum_backward_test[0], bool(cumulative_sum_backward_test[1])],
]
print(tabulate(table, headers=["Test", "pvalue", "Passed"]))
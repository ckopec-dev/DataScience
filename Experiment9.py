#
#
#
# The Basel Problem: find a closed form for 1 + 1 / 2^n + 1 / 3^n + 1 / 4^n + ...
#
# Solved for when n is even. E.g. If n = 2, closed form is (pi^2)/6. If n = 4, closed form is (pi^4)/90, etc.
#
# Unsolved for when n is odd. Values converge, but closed form unknown.
# 
#
#

from Helper import *

# N = 1 is just the harmonic series, which is divergent.
print("n\tBasel(n)")
for n in range (2, 11):
    print(str(n) + "\t" + str(Basel(n, 10000)))

#
#
#
# Helper test
#
#
#

from Helper import *
from tabulate import tabulate

print(tabulate([[1000, PrimesLessThanN(1000), NoverN(1000)]],
               headers=['N', 'PrimesLessThanN', 'NoverN']))

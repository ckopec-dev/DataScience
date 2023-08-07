#
#
#
# Helper test
#
#
#

from Helper import *
from tabulate import tabulate

print(tabulate([[100, PrimesLessThanN(100), NoverN(100)],
                [1000, PrimesLessThanN(1000), NoverN(1000)],
                [1000000, PrimesLessThanN(1000000), NoverN(1000000)]
               ],
               headers=['N', 'PrimesLessThanN', 'NoverN']))

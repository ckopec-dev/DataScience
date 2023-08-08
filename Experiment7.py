#
#
#
# Helper test
#
#
#

from Helper import *
from tabulate import tabulate

print(tabulate([[100, PiN(100), NoverPiN(100)],
                [1000, PiN(1000), NoverPiN(1000)],
                [1000000, PiN(1000000), NoverPiN(1000000)]
               ],
               headers=['N', 'Pi(N)', 'N/Pi(N)']))

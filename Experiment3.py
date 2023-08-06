#
#
#
# Power of 2 series convergence: 
# 1 + 1/2 + 1/4 + 1/8 + ... converges to 2.
#
#
#

sum = 0

for n in range (0, 11):
    sum = sum + (1 / 2 ** n)
    print(sum)


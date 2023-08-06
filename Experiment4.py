#
#
#
# Power of 2 series convergence with reversing operator: 
# 1 - 1/2 + 1/4 - 1/8 + 1/16 ... converges to 2/3.
#
#
#

sum = 0
neg = False

for n in range (0, 11):
    if (neg):
        sum = sum - (1 / 2 ** n)
        neg = False
    else:
        sum = sum + (1 / 2 ** n)
        neg = True
    print(sum)
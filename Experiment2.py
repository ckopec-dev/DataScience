#
#
#
# Overhang: For n stacked cards, how much overhang is there?
#
#
#

# 52 cards
cards = 52
overhang = 0

for n in range(1, cards):
    overhang = overhang + (1 / n)

overhang = overhang * 0.5

print(overhang)

#
#
#
# mpmath library demos
#
#
#

import mpmath 


#mpmath.plot([mpmath.cos, mpmath.sin], [-4, 4])
#mpmath.cplot(lambda z: z, [-10, 10], [-10, 10])
#mpmath.cplot(lambda z: z, [-10, 10], [-10, 10], points=100000)
#mpmath.cplot(mpmath.gamma, [-10, 10], [-10, 10], points=100000)

f = lambda z: (z * 2 - 1)*(z + 2 - mpmath.j)**2 / (z * 2 + 2 - 2 * mpmath.j)

# This takes a few seconds to render
mpmath.cplot(f, [-5, 5], [-3, 3], points=100000)

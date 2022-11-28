#from math import log10
from decimal import Decimal as dc
#from decimal import getcontext

'''

Gets the last digit of a number by subtracting from 0 to 9.
If the current subtrahend makes the number divisible by 10,
it records it in 'reductor'

'''

def lastdigit(num):
    for reductor in range(0, 10):
        if (num - reductor ) % 10 == 0:
            return reductor
        
# -------------- # -------------- # -------------- # -------------- #

'''

Attempts to produce 'the most irrational number' i.e. 0.123456789101112...

If i in some range is less than 10, it multiplies i by 10^{-i}, e.g.,
8 x 10^{-8}.

If i is at least 10, it also multiplies it by 10 to the power of its
last digit (neg.) minus 1, per 

0.0000000009
0.000000000010
0.00000000000011 +1
0.0000000000000012 +2
0.000000000000000013 +3
0.00000000000000000014 +4

'''

def irr_gen(x):
    irr_list = []
    for i in range(1, x + 1):
        if i < 10:
            i_trans = dc(i * 10**(-i))
        else:
            i_trans = dc(i * 10**(-i) * 10**(-lastdigit(i) - 1))
        irr_list.append(i_trans)
    finale = dc(sum(irr_list))
    return finale

# -------------- # -------------- # -------------- # -------------- #

'''

Not working due to precision and rounding for floats.

Only goes up to 13 correctly.

Try tinkering with Decimal (there are options for both).

Adjusting precision only won't work due to rounding.

'''

irr_gen(15)
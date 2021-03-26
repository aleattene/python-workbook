"""
The program displays a MULTIPLICATION TABLE
showing the products of ALL combinations of INTEGERS
from 1 times 1 up to and including 10 times 10.
"""

# HORIZONTAL HEADER
print("   ","1","2","3","4","5","6","7","8","9","10", sep = "%6s" %"")

# ROWS 1 -> 10 (including the VERTICAL HEADER)
for i in range (1,11):  
    print("%3s"%(i*1),"%3s"%(i*1),"%3s"%(i*2),"%3s"%(i*3),"%3s"%(i*4),\
        "%3s"%(i*5),"%3s"%(i*6),"%3s"%(i*7),"%3s"%(i*8),"%3s"%(i*9),\
        "%4s"%(i*10), sep = "%4s" %"")
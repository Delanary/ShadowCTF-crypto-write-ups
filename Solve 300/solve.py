from random import randint as despite
from numpy import linalg
def the(lies, that, you):
    if len(lies)!=60:return False
    are=[0 for i in range(60)]
    making=[[False for j in range(len(that[i]))]for i in range(len(that))]
    your=3600
    while your > 0:
        love=despite(0, 59)
        Is=despite(0, 59)
        if not making[love][Is]:
            making[love][Is]=True
            your-=1
            are[love]+=that[love][Is]*ord(lies[Is])
    return are==you
mine=input()
For=open("flag.enc", "r")
The=list(map(int,For.read().split(',')))
For.close()
taking=open("cipher", "r")
Skillet=list(map(lambda x:list(map(int, x.split(','))),taking.read().split('.')))
taking.close()
import numpy 

M2 = numpy.array(Skillet)
v2 = numpy.array(The)
s = numpy.linalg.solve(M2, v2)
for i in s:
    print(chr(int(i+0.5)),end = '')
# print(f"Nice! Your flag is {mine}")if the(mine, Skillet, The)else print(":(")

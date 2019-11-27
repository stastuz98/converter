import sys
from Check import ifLenMore1
from Check import ifLenEquals1

if len(sys.argv)>1:
    ifLenMore1.lenMore1()
else:
    ifLenEquals1.LenEquals1()
    


import os 
import sys
z = 0
counter = 0
argument = sys.argv[1:]
for i in argument:
    total = z+i
    counter +=1

    if counter != 10:
        continue
    else:
        print(total)    

# 2a
import random

ArrayData = [random.randint(1,100) for i in range(10) for j in range(10)]

# 2b
for x in range(len(ArrayData)-1):
    for y in range(len(ArrayData)-2):
        for z in range(len(ArrayData)-y-2):
            if ArrayData[x,z] > ArrayData[x,z+1]:
                ArrayData [x,z], ArrayData[x, z+1] = ArrayData[x, z+1], ArrayData [x,z]
        
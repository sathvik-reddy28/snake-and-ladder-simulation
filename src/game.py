import numpy as np
import math
import random
def simulate_game():
    snakes={
         16 : 7,
         60 : 17,
         63 : 19,
         67 : 30,
         87 : 24,
         93 : 69,
         95 : 75,
         99 : 77

    }
    ladder={
        9  : 7,
        18 : 17,
        25 : 19,
        28 : 30,
        56 : 64,
        68 : 24,
        76 : 69,
        79 : 75
    }
    pos=0
    count=0
    while pos<100:
        j=random.randrange(1,7)
        count+=1
        if pos+j<=100:
            pos+=j
        
        if pos in snakes:
            pos=snakes[pos]
        if pos in ladder:
            pos=ladder[pos]

    return count

n=1000
arr=[]

for i in range(n):
    arr.append(simulate_game())

print(f"Succesfully ran {n} simulations")

brr=np.array(arr)
print(f'Mean rolls: {np.mean(brr)}')
print(f'Median rolls: {np.median(brr)}')
print(f'Standard deviation: {np.std(brr)}')
print(f'Minimum rolls: {np.min(brr)}')
print(f'Maximum rolls: {np.max(brr)}')

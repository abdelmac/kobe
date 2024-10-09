import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

M=[]
A=[]

for i in range(10):
    A.append(0)
for i in range(10):
    M.append(A)
for i in range(10):    
    print(M[i])


for i in range(9):
    for j in input().split():        
        n = int(j)
        a=int(i-1)
        b=int(j-1)
        M[a][b]=n

for i in range(10):
    print(M[i])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

reponse="true"



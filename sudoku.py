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

L=[]


for i in range(9):
    for j in input().split():        
        n = int(j)
        print(n)
        a=int(i)
        b=int(j)
        M[a][b]=n


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

reponse="true"



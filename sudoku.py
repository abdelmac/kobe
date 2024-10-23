import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L=[]
A=[]
M=[]

for i in range(9):
    A.append(0)
for i in range(9):
    L.append(A)

for i in range(9):
    for j in input().split():        
        n = int(j)
        a=int(i)-1
        b=int(j)-1
        M.append(n)
    
    L[i]=M
    M=[]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

reponse="true"

#row
for i in range(9):
    for j in range(9):
        k=L[i].count(j+1)
        if k>1:
            reponse="false"

#column

for i in range(9):
    k=0
    for j in range(9):
        if j+1 in L[i]:
            k=k+1
            if k!=9:
                reponse="false"


#subgrid

for i in range(9):
    for j in range(3):
        for k in range(3):
            s=0
            for l in range(3):
                s=s+L[i*3+k][j*3+l]
                if s!=45:
                    r="false"
       

print(reponse)


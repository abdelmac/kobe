import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L=[]
A=[]

for i in range(9):
    A.append(0)
for i in range(9):
    L.append(A)

for i in range(9):
    for j in input().split():        
        n = int(j)
        a=int(i)-1
        b=int(j)-1
        L[a][b]=n

#for i in range(9):
#    print(L[i])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

reponse="true"

for i in range(9):
    for j in range(9):
        if L[i][i]==L[i][j]:
            reponse="false"




print(reponse)
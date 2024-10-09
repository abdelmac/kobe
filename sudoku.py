import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L=[]
M=[]

for i in range(9):
    for j in input().split():
        
        k=j.split()

        n = int(j)
        print(n)


        L.append(n)
    M.append(L)
    print(M)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("true or false")

print(n)

print(L[1])

reponse="true"

for i in range(9):
    for j in range(9):
        if L[i][i]==L[i][j]:
            reponse="false"

for i in range(9):
    for j in range(9):
        if L[i][i]==L[j][i]:
            reponse="false"

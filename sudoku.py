import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

M=[]
A=[]

for i in range(9):
    A.append(0)
for i in range(9):
    M.append(A)
print(M)

L=[]


for i in range(9):
    for j in input().split():
        
        k=j.split()

        n = int(j)
        print(n)


        L[i].append(n)
    
    print(L)


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



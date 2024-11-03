import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#C=[1,2,5,4,5,6]

#i=C.count(5)

#print(i)


L=[]
L=[[1,2,3,4,5,6,7,8,9],[9,6,4,5,2,3,1,7,8],[9,6,4,5,2,3,1,7,8],[9,6,4,5,2,3,1,7,8],[9,6,4,5,2,3,1,7,8],[9,6,4,5,2,3,1,7,8],[9,6,4,5,2,3,1,7,8],[9,6,4,5,2,3,1,7,8],[9,8,7,6,5,4,3,2,1]]
M=[]


for i in range(9):
    for j in input().split():        
        n = int(j)
        a=int(i)-1
        b=int(j)-1
        M.append(n)
    print(M)
    L[i]=M
    M=[]

for i in range(3):
    for j in range(3):
        print(L[i+1][j])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

reponse="true"
r=123456789
for i in range(9):
    for j in range(9):
        if (L[i][j] in L[i][-j:]) or (L[i][j] in L[i][:j]):
            reponse="false"
            print(reponse)



print( reponse )







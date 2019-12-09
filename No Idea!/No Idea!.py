# Enter your code here. Read input from STDIN. Print output to STDOUT

size = input()    # n and m
n = int(size[0])
m = int(size[2])
arr = []
A = set()
B = set()

arr = list(map(int,input().split())) # n int in the arr for happiness detection
    
A = set(map(int,input().split()))     #setA
    
B = set(map(int,input().split()))  #setB

happy = 0

for ch in arr:
    if ch in A:
        happy += 1
    elif ch in B:
        happy -= 1

print(happy)
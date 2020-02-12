# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = list()
out = list()
count = 0 
d = dict()
for i in range(n):
    l.append(input())
for i in range(n):
    if(l[i] in d.keys()):
        d[l[i]] += 1
    else:
        d[l[i]] = 1
for key,val in d.items():
    count += 1
    out.append(val)
print(count)
for ch in out:
    print(ch,end=" ")
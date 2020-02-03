n= int(input())
out = []
l = []
b = [] 
count = 0 
while(n>0):
    b.append(int(n%2))
    n = int(n/2)
    length = len(b)
for j in range(length):
         #print(b[j],end="")
   if(b[j] == 1):
      count = count+1
      l.append(j+1)
out.append(count)
out = out + l
print(out)




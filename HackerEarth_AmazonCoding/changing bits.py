def call(lst):
    ze = []
    count = 0
    for i in lst:
        if(i==0):
            count+=1
        else:
            count = 0
        ze.append(count)
    return(max(ze))

n = int(input())
s = str(format(n,'b'))
lst = []
for i in s:
    lst.append(int(i))
m = []
for ii in range(0,len(lst)):
    if(lst[ii]==1):
        lst[ii]=0
        x = call(lst)
        m.append(x)
        lst[ii]=1
print(max(m))

def goodString (N, Q, S, arr, ranges):
    # Write your code here
    def init(s,ranges):
        sub = list(s)
        ran = []
        for i in ranges:
            l,h = i[0],i[1]
            newlst = sub[l-1:h]
            if(len(newlst)==len(set(newlst))):
                ran.append(1)
            # print(ran)
        if(sum(ran) == len(ranges) ):
            return 1
        else:
            return 0

    def reagg(newlst):
        s = ''
        for i in newlst:
            if i != '-':
                s+=i
        return list(s)
    
    def check(sub,ranges):
        ran = []
        for i in ranges:
            l,h = i[0], i[1]
            newlst = sub[l-1:h]
            # print(newlst)
            newlst = reagg(newlst)
            if(len(newlst)==len(set(newlst))):
                ran.append(1)
            # print(ran)
        if(sum(ran) == len(ranges) ):
            return 1
        else:
            return 0
    s = S
    n = N
    # print(len(set(s)), len(s))
    if(init(s,ranges)):
        return(0)
    else:
        sub = list(s)
        i = 0
        count = 0
        while( i < n):
            count += 1
            ele = arr[i]
            sub[ele-1] = '-'
            if( check(sub,ranges) ):
                break
            # print("               ",sub)
            i+=1
        return(count)

T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    S = input()
    arr = list(map(int, input().split()))
    ranges = [list(map(int, input().split())) for i in range(Q)]

    out_ = goodString(N, Q, S, arr, ranges)
    print (out_)

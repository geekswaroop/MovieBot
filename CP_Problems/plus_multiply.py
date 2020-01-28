for _ in range(int(input())):
    n=int(input())
    a=b=c=0
    ar=list(map(int,input().split()))
    for i in range(n):
        if(ar[i]==2):
            a=a+1
        elif(ar[i]==0):
            b=b+1
    c=a*(a-1)//2+b*(b-1)//2
    print(c)

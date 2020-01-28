n = int(input())
no=0
no+=int(n/100)
n%=100
no+=int(n/20)
n%=20
no+=int(n/10)
n%=10
no+=int(n/5)
n%=5
no+=n
print (no)

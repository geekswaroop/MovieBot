t = int(input())
my_list=[]
for i in range(0,t):
  k = [int(n) for n in input().split()]
  if k[0] % 2 == 0 :
    my_list.append(min(k[1]*k[0],int(k[0]/2)*k[2]))
  else :
    my_list.append(min(k[1]*k[0],int(k[0]/2)*k[2]+k[1]))
for i in my_list:
  print (i)
 

mainarr = raw_input().split(' ')
list = [int(num) for num in mainarr]

N = list[0]
k = list[1]
x = list[2]

narr = [int(num) for num in range(1,N+1)]

while len(narr) != 1:
   mod = x%k
   
   if mod != 0:
      ind = narr.index(x)
      leng = len(narr)
      print(ind)
      for i in range(1,mod+1):
	     del narr[(ind+i)%leng]
      x = narr[(ind+mod)%len(narr)]
      print(x)
   else:
      ind = narr.index(x)
      x = narr[(ind+1)%len(narr)]
      
print(narr[0])




firstarr = raw_input()  
mainarr = list(map(int,firstarr.split(' ')))

Narr = raw_input().split(' ')
actualarr = [int(num) for num in Narr]

for item in range(0,mainarr[1]):
    temp = raw_input().split(' ')
    temparr = [int(num) for num in temp]
    if temparr[0] == 1:
        x = temparr[1]
        y = temparr[2]
        actualarr[x] = y
    else:
        x = temparr[1]
        y = temparr[2]
        sum = 0
        for i in range(x,y+1):
            sum = sum + actualarr[i]
        print(sum)

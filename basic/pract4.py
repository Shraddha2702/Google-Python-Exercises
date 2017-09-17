n = input()
alist = map(int, raw_input().split(' '))
first = alist[0::3]
second = alist[1::3]
third = alist[2::3]
print sum(first),sum(second),sum(third)
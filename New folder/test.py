geek = 'GEEKSFORGEEKS'
s = [1,2,3,4,5,6]
for i in range(0,len(geek)):
	print(geek[i])

s = [1,2,3,4,5,6]
nS = len(s)
del s[0] 
print(s)

s.pop(1)
print(s)

s.clear()
print(s)

for i in range(0,nS): s.append(i)
print(s)

s.reverse()
print(s)

s.insert(3,4)
s.sort()
print(s)

tup = (0,1,2,3,4,5)
for i in range(0,len(tup)):
	print(tup[i])

print(tup[1:])
print(tup[:])
print(tup[2:4])
print(tup[:4])
print(tup[-2])

ls = [0,1,2,3,4,5]
print(ls[1:])
print(ls[:])
print(ls[2:4])
print(ls[:4])
print(ls[-2])
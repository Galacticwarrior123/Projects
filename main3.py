l = [1, 2, 3, 4, 5]
print(l)

count = 0
for i in l:
    count += i

avg = count / len(l)
print(avg)

print(count)
l.sort()
print(l[0])
print(l[-1])
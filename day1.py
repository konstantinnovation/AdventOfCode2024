day="1"
data = open("input"+day).readlines();
#data = open("input"+day+"test").readlines();
#print(data[:3])
#print("...")
#print(data[-3:])
left = []
right = []
for line in data:
	line = line.split()
#	print(line)
	left.append(int(line[0]))
	right.append(int(line[1]))
left = sorted(left)
right = sorted(right)
#print(left)
#print(right)
diff = []
for i in range(len(left)):
	diff.append(abs(left[i]-right[i]))
print(sum(diff))

sum = 0
for v in left:
	value = v*right.count(v)
	sum += value
	print(value)
print(sum)

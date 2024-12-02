day="2"
data = open("input"+day).readlines();
#data = open("input"+day+"test").readlines();
#print(data[:3])
#print("...")
#print(data[-3:])

def checkall(values):
	for i in range(len(values)):
		res = values[::]
		res.pop(i)
		if check(res)==1:
			return 1
	return 0

def check(values):
#	print("checking")#
#	print(values)
	dampen = True;
	if(values[0]==values[1]):
		return 0
	if(values[0]<values[1]):
		for i in range(len(values)-1):	
			if( values[i] >= values[i+1] or values[i] < values[i+1]-3 ):
				return 0
	if(values[0]>values[1]):
		for i in range(len(values)-1):	
			if( values[i] <= values[i+1] or values[i] > values[i+1]+3 ):
				return 0
	return 1;
values = []
for line in data:
	if(line != ""):
		row = []
		for d in line.split():
			row.append(int(d))
		values.append(row)

count = 0;
for row in values:
	count += check(row)
print(count)
count = 0
for row in values:
	count += checkall(row)
print(count)

day="8"
rawdata = open("input"+day).readlines();
#rawdata = open("input"+day+"test").read().split("\n");
if rawdata[-1]=="":
    rawdata.pop()

rows = len(rawdata)
cols = len(rawdata[0])

anti = []

for d in range(rows):
    anti.append([0]*cols)
# for d in anti:
#     for i in d:
#         print(i,end=" ")
#     print("")

symbols = []
for d in rawdata:
    for c in d:
        if c!="\n" and c != "." and not c in symbols:
            symbols.append(c)
print(symbols)
print(rows,cols)

def mandist(a,b):
    return (a[0]-b[0],a[1]-b[1])

d = {}
for ant in symbols:
    d[ant]=[]
    for r in range(rows):
        for c in range(cols):
            if rawdata[r][c]==ant:
                d[ant].append([r,c])
    pairs = d[ant]
    print(ant,pairs)
    for i in range(len(pairs)):
        for j in range(i,len(pairs)):
            if i!=j:
                offr = mandist(pairs[i],pairs[j])[0]
                offc = mandist(pairs[i],pairs[j])[1]
                a = pairs[i]
                b = pairs[j]
                #print(a,b,offr,offc)
                try:
                    if a[0]+offr >= 0 and a[1]+offc >= 0:
                        anti[a[0]+offr][a[1]+offc]=4;
                except:
                    pass
                try:
                    if b[0]-offr >= 0 and b[1]-offc >= 0:
                        anti[b[0]-offr][b[1]-offc]=4;
                except:
                    pass
for d in rawdata:
    print(d)

# for i in range(len(rawdata)):
#     for j in range(i,len(rawdata[i])):
#         if rawdata[i][j]!='.':
#             anti[i][j]=0

count = 0
for d in anti:
    for i in d:
        if i != 0:
            count+=1
        print(i,end="")
    print("")
print(count)

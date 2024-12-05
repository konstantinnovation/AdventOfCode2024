day="5"
#rawdata = open("input"+day).readlines();
rawdata = open("input"+day+"test").read().split("\n");

part = rawdata.index("")
rules = rawdata[:part]
books = rawdata[part+1:]
#print(rules)
books.pop()
#print(books)
#phase 1
order ={}
allpages = []
for rule in rules:
    pair = rule.strip().split("|")
    if not pair[0] in allpages:
        allpages.append(pair[0])
    if not pair[1] in allpages:
        allpages.append(pair[1])
    if not pair[0] in order:
        order[pair[0]]=[]

for rule in rules:
    pair = rule.strip().split("|")
    order[pair[0]].append(pair[1])
#print(order)

def anyoverlap(a,b):
    for v1 in a:
        for v2 in b:
            if v2 == v1:
                return True
    return False;

def check(num,prev,rest,d,all):
    #print("checking ",num,rest);
    if num in d:
        before = d[num]
        if anyoverlap(before,rest) and not anyoverlap(before,prev):
            return False
    return True
ans = []
#print(order)

for book in books:
    print(book)
    book = book.split(",")
    for i in range(len(book)-1):
        value = book[i]
        rest = book[i+1:]
        prev = book[:i]
        if check(value,prev,rest,order,allpages):
            ans.append(book)
for x in ans:
    print(x)

#phase 2

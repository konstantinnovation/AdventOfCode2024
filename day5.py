import random
day="5"
rawdata = open("input"+day).read().split("\n");
#rawdata = open("input"+day+"test").read().split("\n");

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


def checkBook(book,order,allpages):
        for i in range(len(book)-1):
            value = book[i]
            rest = book[i+1:]
            prev = book[:i]
            if check(value,prev,rest,order,allpages):
                return False
        return True

def reorder(book, order,allpages):
    newbook = [book[0]]
    for page in book[1:]:
        inserted = False;
        for i in range(len(newbook)):
            if newbook[i] in order[page]:
                newbook.insert(i,page)
                inserted = True;
                break;
        if not inserted:
            newbook.append(page)
    return newbook

print(order)
print("----")
total = 0
total2 = 0
id = 0
for book in books:
    book = book.split(",")
    print("book: ",id,"of",len(books))
    id+=1
    if checkBook(book,order,allpages):
        #print("Good ",book, book[len(book)//2])
        total += int(book[len(book)//2])
    else:
        #print("Badd ",book)
        book = reorder(book,order,allpages)
        total2 += int(book[len(book)//2])
print(total)
print(total2)
#phase 2

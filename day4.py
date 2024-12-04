day="4"
#rawdata = open("input"+day).readlines();
rawdata = open("input"+day+"test").read().split("\n");

for line in rawdata:
    print(line.strip())


def checkX(grid,row,col):
    print("found A at",row,col)
    if     grid[row -1 ][col -1] == 'M' and grid[row +1 ][col +1]=='S'     or grid[row -1 ][col -1] == 'S' and grid[row +1 ][col +1]=='A':
        print("found diagonal 1")
        if grid[row -1 ][col +1] == 'M' and grid[row +1 ][col -1]=='S' or grid[row -1 ][col +1] == 'S' and grid[row +1 ][col -1]=='A':
            print("found diagonal 2")
            return 1
    print("Failed to find and X of Mas")
    return 0


def check(grid,row,col,drow,dcol):
    #print("found X at",row,col)
    word = "XMAS"
    for i in range(1,4):
        rowi = row+i*drow
        coli = col+i*dcol
        try:
            if rowi <0 or coli <0:
                #print(word[i],"not found, instead: out of bounds")
                return 0
            if grid[rowi][coli] != word[i] :
                #print(word[i],"not found at r,c=(",rowi,coli,"), instead: ", grid[rowi][coli] )
                return 0
            else:
                #print(word[i],"found")
                pass
        except:
            #print(word[i],"not found, instead: out of bounds")
            return 0
    return 1
count = 0;
for row in range(1,len(rawdata)-1):
    for col in range(1,len(rawdata[row])-1):
        if rawdata[row][col] == 'X':
            count += check(rawdata,row,col,0,1);
            count += check(rawdata,row,col,0,-1);
            count += check(rawdata,row,col,1,0);
            count += check(rawdata,row,col,-1,0);
            count += check(rawdata,row,col,1,1);
            count += check(rawdata,row,col,1,-1);
            count += check(rawdata,row,col,-1,-1);
            count += check(rawdata,row,col,-1,1);
print(count)

count = 0;
for row in range(len(rawdata)):
    for col in range(len(rawdata[row])):
        if rawdata[row][col] == 'A':
            count += checkX(rawdata,row,col);

print(count)

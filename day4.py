day="4"
#rawdata = open("input"+day).readlines();
rawdata = open("input"+day+"test").readlines();

for line in rawdata:
    print(line.strip())

def check(grid,row,col,drow,dcol):
    print("found X at",row,col)
    word = "XMAS"
    for i in range(1,4):
        rowi = row+i*drow
        coli = col+i*dcol
        try:
            if grid[rowi][coli] != word[i] :
                print(word[i],"not found, instead: ", grid[rowi][coli] )
                return 0
        except:
            return 0
    return 1
count = 0;
for row in range(len(rawdata)):
    for col in range(len(rawdata[row])):
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

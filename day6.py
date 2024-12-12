day="6"
rawdata = open("input"+day).readlines();
#rawdata = open("input"+day+"test").read().split("\n");
if rawdata[-1]=="":
    rawdata.pop()

rows = len(rawdata)
cols = len(rawdata[0])

for r in range(rows):
    for c in range(cols):
        if rawdata[r][c] == "^" :
            startr = r
            startc = c
            rawdata[r]= rawdata[r][:c] + "." + rawdata[r][c+1:]

#for row in rawdata:#
#    print(row)
grid = []
for i in range(rows):
    grid.append( [0]*cols )
print(grid)

print(startr,startc)
r=startr
c=startc
direction = 0;
steps = 0;
dir=[[-1,0],[0,1],[1,0],[0,-1]]
while True:
    #print(steps)
    try:
        if rawdata[r][c]==".":
            grid[r][c]+=1;
            r+=dir[direction][0]
            c+=dir[direction][1]
            steps+=1
        else:
            r-=dir[direction][0]
            c-=dir[direction][1]
            grid[r][c]-=1;
            direction+=1
            direction=direction%4
    except Exception as e:
        #print("off grid",e)
        break
total = 0
for row in grid:
    for value in row:
        if value > 0:
            total+=1

print("done in",total,"steps")


def printr(ary):
    for v in ary:
        if v == 0:
            print("_",end="")
        else:
            print("#",end="")
    print("")


def isOffGrid(r,c):
    return r < 0 or c < 0 or r >= rows or c >= cols

printed = 0
total = 0
for blockr in range(rows):
    for blockc in range(cols):
        #reset grid to 0
        grid = []
        for i in range(rows):
            grid.append( [0]*cols )

        #print("checking ",blockr,blockc)
        r=startr
        c=startc
        direction = 0;
        dir=[[-1,0],[0,1],[1,0],[0,-1]]
        count = 1
        while True:
            #print(steps)

            if isOffGrid(r,c):
                break
            if rawdata[r][c]=="." and (r != blockr or c != blockc):
                grid[r][c]+=1;
                count+=1;
                r+=dir[direction][0]
                c+=dir[direction][1]
                if isOffGrid(r,c):
                    break
                if grid[r][c]> 35:
                    total+=1
                    print("found loop at",blockr,blockc)
                    # if printed < 2:
                    #     printed += 1
                    #     for gridr in grid:
                    #         printr(gridr)
                    break
            else:
                r-=dir[direction][0]
                c-=dir[direction][1]
                grid[r][c]-=1;
                direction+=1
                direction=direction%4

print(total,"locations")

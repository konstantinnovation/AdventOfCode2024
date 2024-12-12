day="7"
rawdata = open("input"+day).readlines();
#rawdata = open("input"+day+"test").read().split("\n");
if rawdata[-1]=="":
    rawdata.pop()

rows = len(rawdata)
 #cols = len(rawdata[0])

for i in range(rows):
    rawdata[i]=rawdata[i].split(":")
    rawdata[i][1]=rawdata[i][1].split(" ")
    rawdata[i][1].pop(0)
    rawdata[i][0]=int(rawdata[i][0])
    for j in range(len(rawdata[i][1])):
        rawdata[i][1][j] = int(rawdata[i][1][j])
#for line in rawdata:
#    print(line)

def combineable(total,nums,partial):
    if len(nums) < 0: #error state
        print("This should not happen!",len(nums))
        return False
    elif len(nums) == 0: #done
        #print(partial)
        return total == partial;
    # elif(partial==None): #multiple values to start
    #     if( combineable(total,nums[2:],nums[0]+nums[1]) ):
    #         return True;
    #     elif( combineable(total,nums[2:],nums[0]*nums[1]) ):
    #         return True;
    #     else:
    #         return False
    else: #multiple values not starting
        if combineable(total,nums[1:], partial + nums[0] ):
            return True
        if combineable(total,nums[1:], partial * nums[0]  ):
            return True
        if combineable(total,nums[1:], int(str(partial)+ str(nums[0]))  ):
            return True
        else:
            return False

total = 0
for line in rawdata:
    #print(line)
    if combineable(line[0],line[1][1:],line[1][0]) :
        print("pass:",line)
        total += line[0]
    else:
        print("fail:",line)


print(total)

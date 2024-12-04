
day="3"
rawdata = open("input"+day).readlines();
#rawdata = open("input"+day+"test").readlines();
do = True
total = 0
for data in rawdata:
    index = data.find("mul(")
    while( index >=0):
        doIndex = data.find("do()")
        dontIndex = data.find("don't()")
        print("do",doIndex,"dont",dontIndex)
        if( doIndex >=0 and doIndex < index  ):
            print("Do it!")
            do = True
        if( dontIndex >=0 and dontIndex < index ):
            print("Dont do it!")
            do = False

        data = data[index+4:]
        #print(data)
        parenindex = data.find(")")
        index = data.find("mul(")
        if parenindex > 0  and parenindex < index or index < 0 :
            nums = data[:parenindex]
            #print(nums)
            if("," in nums):
                pair = nums.split(",")
                if(len(pair[0])<4 and len(pair[1])<4):
                    print("nums:",pair, len(pair[0]) , len(pair[1]))
                    if do:
                        total+= int(pair[0]) * int(pair[1])
        else:
            print("rejecting:",data[:parenindex] )

print(total)

#print("...")
#print(data[-3:])

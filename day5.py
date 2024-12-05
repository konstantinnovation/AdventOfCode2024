day="5"
#rawdata = open("input"+day).readlines();
rawdata = open("input"+day+"test").read().split("\n");

for line in rawdata:
    print(line.strip())


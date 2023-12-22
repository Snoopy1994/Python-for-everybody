import re
fname = "regex_sum_1933082.txt"
f = open(fname)

numlst = []
for line in f:
    line = line.rstrip()
    # word = line.split()
    nums = re.findall('[0-9]+', line)
    # print(num)
    for num in nums:
        num = int(num)
        numlst.append(num)

print(sum(numlst))

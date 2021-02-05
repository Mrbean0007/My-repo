floatlist = input().split(',')  # Spliting input based on comma
flist = []  # Created an empty list to add and convert to string data typ we to float data type
for i in floatlist:
    flist.append(float(i))

# Getting interval
interval1 = [x for x in flist if (x >= 0.0) and (x < 0.2)]  # interval[0,0.2)
interval2 = [x for x in flist if (x >= 0.2) and (x < 0.4)]  # interval[0.2,0.4)
interval3 = [x for x in flist if (x >= 0.4) and (x < 0.6)]  # interval[0.4,0.6)
interval4 = [x for x in flist if (x >= 0.6) and (x < 0.8)]  # interval[0.6,0.8)
interval5 = [x for x in flist if (x >= 0.8) and (x < 1.0)]  # interval[0.8,1.0)

# Getting minimum value for set
len_interval = [len(interval1), len(interval2), len(
    interval3), len(interval4), len(interval5)]
min_len = min(len_interval)

outlist = []  # Empty list and append the values inside list based on minimum set for each intervals
for x in range(min_len):
    outlist.append(interval1[x])
    outlist.append(interval2[x])
    outlist.append(interval3[x])
    outlist.append(interval4[x])
    outlist.append(interval5[x])

output = ','.join(map(str, outlist))  # Getting output in strings

print(output)

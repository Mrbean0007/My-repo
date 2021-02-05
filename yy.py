a = 'ABBCCDDAFFSSEEGAA'
li = []
for i in a:
    li.append(i)
print(li)
li2 = []
n = 0
for x in li:
    if li[n] != li[n+1]:
        li2.append(li[n])
    if li[n] == li[n+2]:

    n += 1
print(li2)


fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    print("words", words)
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1
    print("counts", counts)

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
print("lst", lst)
lst = sorted(lst, reverse=True)

print("lst sorted", lst)
print("lst :10", lst[:10])

for val, key in lst[:10]:
    print(key, val)

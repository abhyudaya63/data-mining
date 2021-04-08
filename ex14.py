import random

def buckets(filename, bucketName, separator, classColumn):
    "divinding data into buckets"

    numberOfBuckets = 10
    data = {}
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if separator != '\t':
            line = line.replace(separator, '\t')
        category = line.split()[classColumn]
        data.setdefault(category, [])
        data[category].append(line)
    buckets = []
    for i in range(numberOfBuckets):
        buckets.append([])
    for k in data.keys():
        random.shuffle(data[k])
        bNum = 0
        for item in data[k]:
            buckets[bNum].append(item)
            bNum = (bNum + 1) % numberOfBuckets

    for bNum in range(numberOfBuckets):
        f = open("%s-%02i" % (bucketName, bNum + 1), 'w')
        for item in buckets[bNum]:
            f.write(item)
        f.close()

buckets("pimaSmall.txt", 'pimaSmall',',',8)

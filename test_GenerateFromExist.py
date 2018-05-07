from CompositeKeysStorage import KeysStorage

keys = [set(['this is the 1st', 'this is the 2nd', 'this is the 3rd']),
        set(['this is he 2nd', 'this is the 3rrd', 'this is the 4th']),
        set(['this is the 1st']),
        set(['this is the 2nd']),
        set(['this is th 1st', 'this is tha 2nd', 'this is the 3rd'])]

attrslst = [set(['this is the 1st', 'this is the 2nd', 'this is the 3rd', 'this', 'is', 'nothing'])]

ks = KeysStorage()
for key in keys:
    ks.insert(key)

for allAttrs in attrslst:
    res = ks.findCompositeKeys(allAttrs)
    print(0)
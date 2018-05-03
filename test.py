from PrefixTreeCreation import buildPrefixTree
from NonKeyFind import NonKeyFinder
from KeyFind import KeyFinder

ds = [['Michael', 'Thompson', '3478', '10'],
      ['Sally', 'Kwan', '3478', '20'],
      ['Michael', 'Spencer', '5237', '90'],
      ['Michael', 'Thompson', '6791', '50']]
depth = len(ds[0])


root = buildPrefixTree(ds)
if root == -1:
      print('no composite key')
finder = NonKeyFinder(depth)
finder.find(root, 0)
kFinder = KeyFinder(depth)
keys = kFinder.find(finder.NonKeySet)

print(finder.NonKeySet)
print(keys)

print(0)
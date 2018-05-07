from PrefixTreeCreation import buildPrefixTree
from NonKeyFind import NonKeyFinder
from KeyFind import KeyFinder
from common import decode

# ds = [['Michael', 'Thompson', '3478', '10'],
#       ['Sally', 'Kwan', '3478', '20'],
#       ['Michael', 'Spencer', '5237', '90'],
#       ['Michael', 'Thompson', '6791', '50']]
# depth = len(ds[0])

filePath = 'd:\\open-10000.csv'
filePath1 = 'd:\\toytest.csv'
filePath2 = 'd:\\open-10000-1.csv'
filePath3 = 'd:\\parking-10000.csv'
filePath4 = 'd:\\4.csv' 
filePath5 = 'd:\\5.csv' 
filePath6 = 'd:\\6.csv' 
filePath7 = 'd:\\7.csv' 
filePath8 = 'd:\\8.csv' 

root, depth = buildPrefixTree(filePath3)
if root == -1:
      print('no composite key')
else:
      finder = NonKeyFinder(depth)
      finder.find(root, 0)
      kFinder = KeyFinder(depth)
      keys = kFinder.find(finder.NonKeySet)

      print(decode(finder.NonKeySet, depth))
      print(decode(keys, depth))

      print(0)


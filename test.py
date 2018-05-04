from PrefixTreeCreation import buildPrefixTree
from NonKeyFind import NonKeyFinder
from KeyFind import KeyFinder
import csv

# ds = [['Michael', 'Thompson', '3478', '10'],
#       ['Sally', 'Kwan', '3478', '20'],
#       ['Michael', 'Spencer', '5237', '90'],
#       ['Michael', 'Thompson', '6791', '50']]
# depth = len(ds[0])

def setToPrintSet(s, depth):
      pSet = []
      for key in s:
            printKey = []
            for i in range(depth):
                  if key & 1 == 1:
                        printKey.append('1')
                  else:
                        printKey.append('0')
                  key = key >> 1
            pSet.append(''.join(printKey))
      return pSet

filePath1 = 'd:\\toytest.csv'
filePath2 = 'd:\\open-10000-1.csv'
filePath3 = 'd:\\parking-10000.csv'

root, depth = buildPrefixTree(filePath2)
if root == -1:
      print('no composite key')
else:
      finder = NonKeyFinder(depth)
      finder.find(root, 0)
      kFinder = KeyFinder(depth)
      keys = kFinder.find(finder.NonKeySet)

      print(setToPrintSet(finder.NonKeySet, depth))
      print(setToPrintSet(keys, depth))

      print(0)


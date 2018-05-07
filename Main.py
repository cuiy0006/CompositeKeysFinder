from common import setToPrintSet
from CompositeKeysStorage import KeysStorage
from PrefixTreeCreation import buildPrefixTree
from NonKeyFind import NonKeyFinder
from KeyFind import KeyFinder

def callMeStart(filePaths, columnNames):

    ks = KeysStorage()
    dic = {} # path -> keys

    for i, path in enumerate(filePaths):

        keys = ks.findCompositeKeys(columnNames[i])
        if len(keys) == 0:
            root, depth = buildPrefixTree(path)
            if root == -1:
                dic[path] = None
            else:
                finder = NonKeyFinder(depth)
                finder.find(root, 0)
                kFinder = KeyFinder(depth)
                keys = kFinder.find(finder.NonKeySet) # format ['000000010110010000', '100000000000000000', '010000000010010000']
                for key in setToPrintSet(keys, depth):
                    translatedKey = set(columnNames[i][j] for j, digit in enumerate(key) if digit == '1') # translate '000000010110010000' to format {'col1', 'col2', 'col3'}
                    ks.insert(translatedKey)
                dic[path] = keys
        else:
            dic[path] = keys

    return dic

if __name__ == '__main__':
    filePaths = ['d:\\toytest.csv', 'd:\\open-10000-1.csv', 'd:\\parking-10000.csv', 'd:\\4.csv', 'd:\\5.csv', 'd:\\6.csv', 'd:\\7.csv', 'd:\\8.csv']

    columnNames = [[], [], [], [], [], [], [], []]

    callMeStart(filePaths, columnNames)
class Node:
    def __init__(self):
        self.valToCell = {} #key:vi, value:cell
        self.visited = False
        self.NOofEntity = 0


class Cell:
    def __init__(self, val):
        self.val = val
        self.leafCount = 0
        #self.isLeaf = False
        self.child = Node()

    def isLeaf(self):
        return self.leafCount > 0


def setToPrintSet(s, depth):
      pSet = []
      for key in s:
            printKey = []
            for _ in range(depth):
                  if key & 1 == 1:
                        printKey.append('1')
                  else:
                        printKey.append('0')
                  key = key >> 1
            pSet.append(''.join(printKey))
      return pSet
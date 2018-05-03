from common import Cell, Node

def buildPrefixTree(dataSet):
    root = Node()
    # traverse lines in dataSet
    for entry in dataSet:
        # tier tree from top to down
        node = root
        node.NOofEntity += 1

        t = entry
        # from each column of current row
        for i, val in enumerate(t):
            #6 - 13
            if val not in node.valToCell:
                node.valToCell[val] = Cell(val)
            cell = node.valToCell[val]

            #14 - 22
            if i == len(t) - 1:
                #cell.isLeaf = True
                cell.leafCount += 1 # use leafCount > 0 to represent isLeaf
                if cell.leafCount > 1:
                    return -1
            else:
                node = cell.child
                node.NOofEntity += 1
    return root
            
            
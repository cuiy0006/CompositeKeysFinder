from common import Node, Cell

#toMerge : [Node]
def merge(toMerge):
    if len(toMerge) == 1:
        mergedNode = toMerge[0]
    else:
        mergedNode = Node()
        dic = {} #key: val, value: [cell]
        isLeaf = False #judge whether this is at the leaf level
        for node in toMerge:
            for val, cell in node.valToCell.items():
                if val not in dic:
                    dic[val] = []
                dic[val].append(cell)

                if cell.isLeaf:
                    isLeaf = True

        # 5
        for val, cellList in dic.items():
            mergedNode.valToCell[val] = Cell(val)
            newCell = mergedNode.valToCell[val]

            if isLeaf:
                newCell.leafCount = sum(cell.leafCount for cell in cellList)
                newCell.isLeaf = True # here is what I added
            else:
                partialSet = [cell.child for cell in cellList]
                newCell.child = merge(partialSet)
    return mergedNode
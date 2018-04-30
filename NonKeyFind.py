from PrefixTreeMerge import merge

class NonKeyFinder:
    def __init__(self, depth):
        self.NonKeySet = set()
        self.curNonKey = 0
        self.depth = depth

    def insert(self, NonKey):
        toAdd = True
        for storedNonKey in self.NonKeySet:
            if storedNonKey & NonKey == NonKey:
                toAdd = False
                break
        
        if toAdd:
            for storedNonKey in list(self.NonKeySet):
                if storedNonKey & NonKey == storedNonKey:
                    self.NonKeySet.remove(storedNonKey)
            self.NonKeySet.add(NonKey)

    def find(self, root, attrNo):
        root.visited = True
        origin = self.curNonKey
        self.curNonKey |= (1 << attrNo)

        isLeaf = any(cell.isLeaf for cell in root.valToCell.values())
        if isLeaf:
            for cell in root.valToCell.values():
                if cell.leafCount != 1:
                    self.insert(self.curNonKey)

            self.curNonKey = origin
            if len(root.valToCell) > 1 or any(cell.leafCount > 1 for cell in root.valToCell.values()):
                self.insert(self.curNonKey)
        else:
            if root.NOofEntity == 1:
                return

            for cell in root.valToCell.values():
                if not cell.child.visited:
                    self.find(cell.child, attrNo + 1)
            
            self.curNonKey = origin
            if len(root.valToCell) > 1:
                nonKey = self.curNonKey
                for i in range(attrNo, self.depth):
                    nonKey |= (1 << i)
                if self.isFutile(nonKey):
                    return
                
                mergeTree = merge([cell.child for cell in root.valToCell.values()])
                self.find(mergeTree, attrNo + 1)


    def isFutile(self, nonKey):
        for storedNonKey in self.NonKeySet:
            if storedNonKey & nonKey == nonKey:
                return True
        return False

class KeyFinder:
    def __init__(self, depth):
        self.depth = depth
        self.allOnes = 0
        for i in range(depth):
            self.allOnes |= (1 << i)

    def insert(self, KeySet, key):
        toAdd = True
        for storedKey in KeySet:
            if storedKey & key == storedKey:
                toAdd = False
                break
        
        if toAdd:
            for storedKey in list(KeySet):
                if storedKey & key == key:
                    KeySet.remove(storedKey)
            KeySet.add(key)

    def find(self, NonKeySet):
        KeySet = set()
        for nonKey in NonKeySet:
            complementSet = nonKey ^ self.allOnes

            if len(KeySet) == 0:
                for i in range(self.depth):
                    if (complementSet >> i) & 1 == 1:
                        KeySet.add(1 << i)
            else:
                newSet = set()
                for i in range(self.depth):
                    if (complementSet >> i) & 1 == 1:
                        pKey = (1 << i)
                    
                        for key in KeySet:
                            newKey = key | pKey
                            self.insert(newSet, newKey)
                KeySet = newSet
        return KeySet




            # complementSet = set()
            # for i in range(self.depth):
            #     if (complementKey >> i) & 1 == 1:
            #         complementSet.add(set([i]))
            
            # if KeySet is None:
            #     KeySet = complementSet
            # else:
            #     newSet = set()
            #     for 
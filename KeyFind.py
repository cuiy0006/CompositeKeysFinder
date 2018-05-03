
class KeyFinder:
    def __init__(self, depth):
        self.depth = depth
        self.allOnes = 0
        for i in range(depth):
            self.allOnes |= (1 << i)

    def insert(self, KeySet, key):
        toAdd = True
        for storedKey in KeySet:
            if storedKey & key == storedKey: # means key covers storedKey, storedKey is more short and more like a candidate key
                toAdd = False
                break
        
        if toAdd:
            for storedKey in list(KeySet):
                if storedKey & key == key: # if storedKey covers key, remove it
                    KeySet.remove(storedKey)
            KeySet.add(key)

    def find(self, NonKeySet):
        KeySet = set()
        for nonKey in NonKeySet:
            complementSet = nonKey ^ self.allOnes # complement of nonKey, example nonKey: 1010101, complement: 0101010

            if len(KeySet) == 0:
                for i in range(self.depth):
                    if (complementSet >> i) & 1 == 1:
                        KeySet.add(1 << i) # {0100000, 0001000, 0000010}, this three keys are not included by nonKey 1010101
            else:
                newSet = set()
                for i in range(self.depth):
                    if (complementSet >> i) & 1 == 1:
                        pKey = (1 << i)
                    
                        for key in KeySet:
                            newKey = key | pKey # the key not included by curNonKey and previous NonKey
                            self.insert(newSet, newKey)
                KeySet = newSet
        return KeySet
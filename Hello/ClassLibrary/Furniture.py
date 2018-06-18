class Furniture:
    def __init__(self):
        self.furnitureType = "Teakwood"
        #super(Furniture, self).__init__()
    
    def printFurnitureType(self):
        print (self.furnitureType)


class Chair(Furniture):
    __memberName=""
    def __init__(self, pWoodType):
        #super(Chair, self).__init__()
        self.furnitureType="bla bla"
        self._woodType=pWoodType

    @property
    def woodType(self):
        print("getter!!")
        return self._woodType

    @woodType.setter
    def woodType(self, value):
        print("setter!!!")
        self._woodType = value

    @woodType.deleter
    def woodtype(self):
        del self._woodType

from ClassLibrary.Furniture import Furniture
from ClassLibrary.Chair import Chair

furn = Furniture()

cadeira = Chair("mogno")
cadeira.woodType="compensado"

print(cadeira.woodType)
print(cadeira._woodType)
print(cadeira.furnitureType)
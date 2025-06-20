nama1 = ["umay",'somay','gg']
nama2 = ["ujang",'asep','santoso']

nestedList = [nama1,nama2]
print(nestedList)

copyNestedList = nestedList.copy()
print(copyNestedList)

print(hex(id(nestedList)))
print(hex(id(copyNestedList)))

listPertama = nestedList[0][0]
print(listPertama)

nestedList[0][0] = "darman"
print(nestedList)
print(copyNestedList)

print(hex(id(nestedList[0][0])))
print(hex(id(copyNestedList[0][0])))

from copy import deepcopy

deepcopyNestedList = deepcopy(nestedList)
print(nestedList)
print(copyNestedList)
print(f"{deepcopyNestedList} \n")

nestedList[0][1] = "daraman"
print(nestedList)
print(copyNestedList)
print(deepcopyNestedList)



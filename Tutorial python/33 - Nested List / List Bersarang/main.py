nama1 = ['umay','somay','gg']
nama2 = ['ucup','dadang','asep']

nestedList = [nama1,nama2,2242,2252]
print(nestedList)

# contoh nestedList

peserta0 = ["umay",22,'Lakilaki']
peserta1 = ["somay",17,'Lakilaki']
peserta2 = ["caca",16,'wanita']

pesertaList = [peserta0,peserta1,peserta2]
print(f"peserta {pesertaList}")

for peserta in pesertaList:
    print(f"nama = {peserta[0]}")
    print(f"umur = {peserta[1]}")
    print(f"gender = {peserta[2]}\n")

# dengan refrence

copyList = pesertaList.copy()
print(f"peserta {copyList}")
peserta0[0] = 'ujang'
print(f"peserta copy {copyList}")
print(f"peserta {pesertaList}")

print(hex(id(pesertaList)))
print(hex(id(copyList)))



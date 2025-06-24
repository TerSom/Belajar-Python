import datetime

mahasiswa1 = {
    'nama'     : 'Terry',
    'nim'      : '5353534',
    'sks'      : 140,
    'beasiswa' : str(False),
    'lahir'    : datetime.datetime(2007,5,12)
}

mahasiswa2 = {
    'nama'     : 'Umay',
    'nim'      : '5353534',
    'sks'      : 100,
    'beasiswa' : str(True),
    'lahir'    : datetime.datetime(2000,5,12)
}

mahasiswa3 = {
    'nama'     : 'King',
    'nim'      : '5353534',
    'sks'      : 144,
    'beasiswa' : str(False),
    'lahir'    : datetime.datetime(1999,5,12)
}

dataMahasiswa = {
    "P0001" : mahasiswa1,
    "P0002" : mahasiswa2,
    "P0003" : mahasiswa3
}

print(f"{'key':<6} {'nama':<17} {'sks':<3} {'beasiswa':<9} {'lahir':<9}")
print(49*"-")

for mahasiswa in dataMahasiswa:
    KEY = mahasiswa
    
    NAMA = dataMahasiswa[KEY]['nama']
    SKS = dataMahasiswa[KEY]['sks']
    BEASISWA = dataMahasiswa[KEY]['beasiswa']
    LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<9}")
    
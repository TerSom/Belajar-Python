import datetime
import os
import string
import random

templateMahasiswa = {
    'nama'     : 'Terry',
    'nim'      : '5353534',
    'sks'      : 140,
    'lahir'    : datetime.datetime(2007,12,5)
}

dataMahasiswa = {}

while True:
    os.system('clear')

    print("Selamat Datang")
    print("Data Mahasiswa")
    print(20*"=")

    mahasiswa = dict.fromkeys(templateMahasiswa.keys())
    mahasiswa['nama'] = input("masukan NAMA mahasiswa = ")
    mahasiswa['nim'] = input("masukan NIM mahasiswa = ")
    mahasiswa['sks'] = int(input("masukan SKS mahasiswa = "))
    TAHUN = int(input("masukan tahun lahir = "))
    BULAN = int(input("masukan bulan lahir = "))
    TANGGAL = int(input("masukan tanggal lahir = "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    dataMahasiswa.update({KEY:mahasiswa})
    print(f"{'key':<6} {'nama':<17} {'sks':<3} {'lahir':<9}")
    print(49*"-")
    
    for mahasiswa in dataMahasiswa:
        KEY = mahasiswa
        
        NAMA = dataMahasiswa[KEY]['nama']
        SKS = dataMahasiswa[KEY]['sks']
        LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {LAHIR:<9}")

    print('\n')
    isDone = input("apakah mau lanujut (y/n)")
    if isDone == 'n':
        break

print('AKHIR DARI PROGRAM')
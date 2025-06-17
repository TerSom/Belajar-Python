import datetime as dt

# hariIni = dt.date.today()
# print(hariIni)
# print(f"hari ini adalah {hariIni:%A}")

# tanggal = dt.date(2026,10,12)
# print(tanggal)
# print(f"hari ini adalah {tanggal:%A}")

print("silahkan masukan tanggal,bulan, dan tahun")
tanggal = int(input("masukan tanggal = \t"))
bulan = int(input("masukan bulan = \t"))
tahun = int(input("masukan tahun = \t"))

tanggalLahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir mu adalah {tanggalLahir}")

hariIni = dt.date.today()
umurHari = hariIni - tanggalLahir
umurTahun =umurHari.days // 365
umurBulan =umurHari.days % 365 // 30
print(f"harinya adalah {tanggalLahir:%A}")
print(f"umurHari kamu adalah {umurTahun} tahun dan bulan ke {umurBulan}")

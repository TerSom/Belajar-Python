import datetime

waktu = datetime.datetime.now()

print(f"waktu sekarang adalah {waktu}")
print(f"waktu tahun sekarang adalah {waktu.year}")
print(f"waktu sekarang adalah {waktu.date()}")
print(f"waktu bulan sekarang adalah {waktu.day}")

from collections import Counter

data = ['1','1','2','3','1','1','2','3']
counterData = Counter(data)

# count = 0
# for i in data:
#     if i == "1":
#         count += 1
# print(count)

print(f"counter data = {counterData}")
print(f"counter data = {counterData['1']}")
print(f"counter data = {counterData['2']}")
print(f"counter data = {counterData['3']}")

import io

file = io.open("kocak.txt","r")
print(file.read())

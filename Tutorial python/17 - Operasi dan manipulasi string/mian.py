# merubah menajdi upper case
nama = "umaysomay"
print(nama)
upper = nama.upper()
print("nama akan menjadi huruf besar semua"+ upper)

print(10*"===")

# merubah menajdi lower case
nama = "UmaySOMay"
print(nama)
lower = nama.lower()
print("nama akan menjadi huruf kecil semua" + lower)


print(10*"===")

# pengecekan menggunakan isX

# menggunakan isLower
judul = "To Wong Foo, Thanks for Everything! Julie Newmar"
cekJudul = judul.islower()
print("apakah judulnya menggunakan huruf kecil semua", cekJudul)
judul = "To Wong Foo, Thanks for Everything! Julie Newmar"
judulLower = judul.lower()
cekJudul = judulLower.islower()
print("apakah judulnya menggunakan huruf kecil semua", cekJudul)

print(10*"===")

# menggunakan isUpper
judul = "To Wong Foo, Thanks for Everything! Julie Newmar"
cekJudul = judul.isupper()
print("apakah judulnya menggunakan huruf kecil semua", cekJudul)
judul = "To Wong Foo, Thanks for Everything! Julie Newmar"
judulUpper = judul.upper()
cekJudul = judulUpper.isupper()
print("apakah judulnya menggunakan huruf kecil semua", cekJudul)

# metode isX ada banyak
"""
    1.isalpha
    2.isalnum
    3.isdesimal
    4.isspace
    5.istitle
    dll
"""

judul = "ToWongFooThanksforEverythingJulieNewmar"
cekJudul = judul.isalpha()
print("apakah judul semauanya huruf" + " " + str(cekJudul))
judul = "To WongFoo Thanksfor Everything Julie Newmar"
cekJudul = judul.isalpha()
print("apakah judul semauanya huruf" + " " + str(cekJudul))

print(10*"===")

judul = "ToWongFooThanksforEverythingJulieNewmar123"
cekJudul = judul.isalnum()
print("apakah judul semauanya huruf" + " " + str(cekJudul))
judul = "To WongFoo Thanksfor EverythingJulieNewmar"
cekJudul = judul.isalnum()
print("apakah judul semauanya huruf" + " " + str(cekJudul))

print(10*"===")

judul = "1234123"
cekJudul = judul.isdecimal()
print("apakah judul semauanya huruf" + " " + str(cekJudul))
judul = "12355345 2342"
cekJudul = judul.isdecimal()
print("apakah judul semauanya huruf" + " " + str(cekJudul))

print(10*"===")

judul = " "
cekJudul = judul.isspace()
print("apakah judul semauanya huruf" + " " + str(cekJudul))
judul = " ,"
cekJudul = judul.isspace()
print("apakah judul semauanya huruf" + " " + str(cekJudul))

print(10*"===")

judul = "To Wong Foo Thanks For Everything Julie Newmar"
cekJudul = judul.istitle()
print("apakah judul semauanya huruf" + " " + str(cekJudul))
judul = "To Wong foo Thanks For Everything Julie Newmar"
cekJudul = judul.istitle()
print("apakah judul semauanya huruf" + " " + str(cekJudul))

# mengecek komponenet starswith() dan endswith()
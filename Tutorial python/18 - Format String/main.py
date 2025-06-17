# format string

# contoh generic
# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# bolean
bolean = True
format_boolean = f"bolean adalah {bolean}"
print(format_boolean)

# angka
angka = 200.5
format_angka = f"angka adalah {angka}"
print(format_angka)

# bilangan bulat
angka = 200
format_angka = f"angka adalah {angka:d}"
print(format_angka)

# bilangan ordo ribuan
uang = 5000000
format_uang = f"jumlah uang adalah Rp {uang:,}"
print(format_uang)

# biilangan desimal
angka = 50.00342
format_angka = f"angka desimalnya adalah {angka:.2f}"
print(format_angka)

# menampilkan leading zero
angka = 2005.2425
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda - atau +
angka_minus = -131
angkat_plus = +131.9799879
formatMinus = f"angka minus adalah {angka_minus:-d}"
formatPlus = f"angka minus adalah {angkat_plus:+.2f}"
print(formatMinus)
print(formatPlus)

# mengformat persen
angka = 5
formatPersen = f"angka persen adalah {angka:.0%}"
print(formatPersen)

# format angka lain (binary oktal hexadesimal)

angka = 255
formatbinary = f"angka binarynya adalah {bin(angka)}"
formatOktal = f"angka oktalnya adalah {oct(angka)}"
formatHexadesimal = f"angka hexadesimalnya adalah {hex(angka)}"
print(formatbinary)
print(formatOktal)
print(formatHexadesimal)

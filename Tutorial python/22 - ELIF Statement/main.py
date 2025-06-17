# belajar tentang penkondisian elif

# nama = input("nama kamu siapa = ")

# if nama == "umay":
#     print(f"nicee banget {nama}")
# elif nama == "agus":
#     print(f"kerenn banget {nama}")
# else:
#     print(f"nama lu {nama} gw gk kenal")


# bikin kalkulator dengan banyak operator

angkaPertama = float(input("masukan angka ke 1 = "))
operator = input("masikan operator seperti +,-,/,*,**,% = ")
angkaKedua = float(input("masukan angka ke 2 = "))
hasil = ''

if operator == "+":
    hasil = angkaPertama + angkaKedua
elif operator == "-":
    hasil = angkaPertama - angkaKedua
elif operator == "*":
    hasil = angkaPertama * angkaKedua
elif operator == "/":
    hasil = angkaPertama / angkaKedua
elif operator == "**":
    hasil = angkaPertama ** angkaKedua
elif operator == "%":
    hasil = angkaPertama % angkaKedua
else:
    print("masikan operator seperti +,-,/,*,**,%")

print(f"hasilnya adalah {hasil}")
angkaPertama = int((input("masukan angka pertama : ")))
operator = input("masukan operator contohnya +, -, * , /, ** , % , // : ")
angkaKedua = int((input("masukin angka kedua : ")))
hasil = ""


if operator == '+': 
    hasil = angkaPertama + angkaKedua
elif operator == '-':
    hasil = angkaPertama - angkaKedua
elif operator == '*':
    hasil =  angkaPertama * angkaKedua
elif operator == '/':
   hasil =  angkaPertama / angkaKedua
elif operator == '**':
   hasil =  angkaPertama ** angkaKedua
elif operator == '%':
   hasil =  angkaPertama % angkaKedua
elif operator == '//':
   hasil =  angkaPertama // angkaKedua
else:
    "masukan operator bro"


print("hasilnya adalah", hasil)


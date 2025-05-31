# konversi farenheit ke kelvin

farenheit = float(input("masukan suhu farenheit :"))
print("suhu farenheit adalah ", farenheit ,"farenheit")

kelvin = (5/9) * (farenheit - 32) + 273
print("suhu kelvin adalah ", round(kelvin,2) ,"kelvin")

# konversi kelvin ke farenheit

kelvin = float(input("masukin suhu kelbin :"))
print("suhu kelvin adalah ", kelvin ,"kelvin")

farenheit = (9/5) * (kelvin - 273) + 32
print("suhu farenheit adalah ", round(farenheit,2) ,"farenheit")
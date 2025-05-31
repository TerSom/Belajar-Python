# operasi aritmatika

x = 10
y = 3

# pertambahan
hasil = x + y
print("x + y adalah :", hasil)

# pengurangan
hasil = x - y
print("x - y adlaah :", hasil)

# perkalian
hasil = x * y
print("x * y adalah : ", hasil )

# pembagian
hasil = x / y 
print("x / y adalah : ", hasil)

# exponen atau pangkat
hasil = x ** y
print("x ** y adalah :", hasil)

# modulus atau sisah bagi
hasil = x % y
print("x % y adalah :", hasil)

# floor devision atau di bulatkan
hasil = x // y
print("x // y adalah :", hasil)

# prioritas operasi, atau urutan pejumlahan

'''
    1.()
    2.exponen **
    3.perkalian dan teman temanya * / ** % //
    4.penjumlahan dan pengurangan + -
'''

x = 5
y = 2

hasil = x ** y * x + y - x / y % x // y
print("x ** y * x + y - x / y % x // y adalah",hasil )
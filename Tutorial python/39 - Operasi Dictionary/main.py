# operasi dictionary

nama = {
    "may" : "umay gg",
    "ter" : "Terry gg",
    "sep" : "asep gg"
}

# panjang dictionary
LENNAMA = len(nama)
print(f"panjang dictionarynya adlaah {LENNAMA}")

# mengecek data key 
KEY = 'may'
CHECKEY = KEY in nama
print(f"apakah ada {KEY} di data dictionary = {CHECKEY} ")

# mengakses value dengan (get)
print(nama["may"])
print(nama.get("ter"))
print(nama.get("sep"))
print(nama.get("sgg","tidak ada nama"))

# mengupdate 
nama['may'] = 'kocak gaming'
print(nama)
nama.update({"may": "umay"})
print(nama)
nama.update({"dar":"daraman"})
print(nama)

# mendelet data
del nama["dar"]
print(nama)
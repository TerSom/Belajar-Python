nama_dict = {
    "nama1": "Rizky",
    "nama2": "Alya",
    "nama3": "Budi",
    "nama4": "Citra"
}

# kalo looping biasa dia ngambil keynya
for nama in nama_dict:
    print(nama)
    
# operator untuk mengambil item / interables 
keys = nama_dict.keys()
print(keys)

for key in nama_dict.keys():
    print(nama_dict.get(key))
    
values = nama_dict.values()
print(values)

for key in nama_dict.values():
    print(key)
    
items = nama_dict.items()
print(items)

for key in nama_dict.items():
    print(key)
    
for key,values in nama_dict.items():
    print(f"keynya = {key} valuesnya = {values}")
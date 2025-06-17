nama = "umay"
umur = 17
tinggi = 175
nomerSepatu = 42

# string standar

print(10*"=" + "Data string" + 10*"=")
print(f" nama ={nama} umur ={umur} tinggi ={tinggi} nomer sepatru {nomerSepatu} ")

# string multiline dengan menggunakan newline atau \n
print(10*"=" + "Data string" + 10*"=")
print(f" nama ={nama} \n umur ={umur} \n tinggi ={tinggi} \n nomer sepatru {nomerSepatu} ")

# string multiline dengan menggunakan kutip tripel
print(10*"=" + "Data string" + 10*"=")
print(f"""
    nama = {nama} 
    umur = {umur}
    tinggi = {tinggi}
    nomer sepatu = {nomerSepatu}
""")

# mengatur lebar

print(10*"=" + "Data string" + 10*"=")
print(f"""
    nama   ={nama:>5} 
    umur   ={umur:>5}
    tinggi ={tinggi:>5}
    sepatu ={nomerSepatu:>5}
""")
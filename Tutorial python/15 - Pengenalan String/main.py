data = "ini adalah string"
print(type(data))

# cara membuat string
"""
    1."ini adalah string menggunakan doublee qoute"
    2.'ini adalah string menggunakan single qoute'
"""

data = "halo apa kabar"
print(data)
data = 'halo apa kabar'
print(data)

data = "hari ini adalah jum'at"
print(data)
# atau bisa juga pakai \
data = 'hari ini adalah jum\'at'
print(data)

data = '"hari ini" adalah jumat'
print(data)

sytem = "c:\\user\\ucup"
print(sytem)

# tab
data = "umay\t\t\t\tsomay"
print(data)
# backspacee
data = "umay \bsomay"
print(data)

# newline
print('"hari ini" \nadalah jumat') #ini biasanya di pakai linux dan mac os
print('"hari ini" \radalah jumat') #ini udah jadul
print('"hari ini" \n\radalah jumat') #ini di pakai sama windows

# string literal atau raw
print("c:\nserucup")

# menggunakan raw string
print(r"c\new darman")

# menggunakan literal string
print("""
    nama = ucup
    kelas = 10
""")

# bisa di gabungkan liberal dan raw
print(r"""
    nama : ucup
    kelas : 10
    website : www.youtube.com/watch darnaba
""")
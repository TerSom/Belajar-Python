a = ['umya','gg','ss']
print(a)

b = a 

print(a)
print(b)

b[1] = "umay"
print(b)
print(a)

# adressnya
print(f"adreesnya {(hex(id(a)))}")
print(f"adreesnya {(hex(id(b)))}")

# pakai method .copy agar adressnya tidak sama

c = a.copy()

print(b)
print(a)
print(c)

print(5*"=")
c[0] = 'gg'
print(b)
print(a)
print(c)

print(f"adressnya adalah {(hex(id(a)))}")
print(f"adressnya adalah {(hex(id(b)))}")
print(f"adressnya adalah {(hex(id(c)))}")














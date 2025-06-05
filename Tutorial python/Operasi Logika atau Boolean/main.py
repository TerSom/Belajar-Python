# Logika bolean 
# not or and xor

print("====NOT====")
a = False
b = not a
print("data a",b)
a = True
b = not a
print("data a",b)

print("====OR====")
a = True
b = True
c = a or b
print("data c",c)
a = True
b = False
c = a or b
print("data c",c)
a = False
b = True
c = a or b
print("data c",c)
a = False
b = False
c = a or b
print("data c",c)

print("====AND====")
a = True
b = True
c = a and b
print("data c",c)
a = True
b = False
c = a and b
print("data c",c)
a = False
b = True
c = a and b
print("data c",c)
a = False
b = False
c = a and b
print("data c",c)

print("====XOR====")
a = True
b = True
c = a ^ b
print("data c",c)
a = True
b = False
c = a ^ b
print("data c",c)
a = False
b = True
c = a ^ b
print("data c",c)
a = False
b = False
c = a ^ b
print("data c",c)



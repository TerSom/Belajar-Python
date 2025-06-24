teman_teman = {
    "nama1": "Rizky",
    "nama2": "Alya",
    "nama3": "Budi",
    "nama4": "Citra"
}

friends = teman_teman.copy()

teman_teman["nama1"] = "terry"
print(teman_teman)
print(friends)
# pop dictionary (harus pake key)

popNama = friends.pop("nama1")
print(popNama)
print(friends)

# popitem dictionary (data terakhir)

popNama = friends.popitem()
print(popNama)
print(friends)

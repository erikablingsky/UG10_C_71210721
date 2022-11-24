erika = []
a = input("Masukkan daftar pesanan : ").title()
for x in a.split(", "):
    erika.append(x)
print(f"Daftar pesanan : {erika}")
b = input("Masukkan pesanan yang ingin ditambahkan : ")
if b.title() in erika:
    print(f"{b.upper()} sudah berada dalam daftar pesanan.")
else:
    erika.append(b)
    print(f"Hasil penambahan daftar pesanan : {erika}")

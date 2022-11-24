print(f"{'=' * 10} Pilih Menu {'=' * 10}")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Pilihan Anda: "))

if c == 1:
    hasil = a + b
elif c == 2:
    hasil = a - b
elif c == 3:
    hasil = a * b
elif c == 4:
    hasil = a / b

print(f"hasil: {hasil}")

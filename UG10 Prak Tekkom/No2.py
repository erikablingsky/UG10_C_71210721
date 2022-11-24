bulan = int(input("Masukkan bulang (1-12): "))

if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
    hari = 31
elif bulan == 2:
    hari = 28
elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
    hari = 30

print("Jumlah Hari:", hari)
import datetime as dt

jenisBBM = {
    "Pertamax": 13900,
    "Pertalite": 10000,
    "Solar Subsidi": 6800,
    "Pertamax Turbo": 14300,
    "Pertamina Dex": 18550,
    "Dexlite": 18000,
}
print("==================== Daftar Jenis BBM ====================")
for i in jenisBBM:
    print("Jenis BBM : ", i , "\t Harga : ", jenisBBM[i])
print("Pembelian diatas Rp50.000,- mendapatkan diskon 5%")
print("\n========================================================\n")
nama = str(input("Masukan Nama anda \t : "))
alamat = str(input("Alamat \t\t\t : "))
nomorTelepon = input("Nomor Telepon \t\t : ")
tanggal = dt.date.today()
beli = input("Pilih Jenis BBM \t : ")
jumlah = int(input("Jumlah Pembelian \t : "))
bayar = jumlah * jenisBBM[beli]

if bayar > 50000:
    diskon = bayar*5/100
    total = bayar - diskon
else:
    total = bayar

print("\n==================== Detail Pembayaran ====================\n")
print("Nama \t\t:", nama)
print("Alamat \t\t:", alamat)
print("Nomor Telepon \t:", nomorTelepon)
print("Tanggal \t:", tanggal)
print("Jenis BBM \t:", beli)
print("Jumlah pembelian :", jumlah, "liter")
print("Total biaya \t: ", jumlah, "*", jenisBBM[beli], "=", bayar)
print("Total yang harus dibayar :", total)
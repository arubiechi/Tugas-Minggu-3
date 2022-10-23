import os
os.system("cls")
print("PROGRAM PENJUALAN BUKU".center(80))
print("_"*80)

satuan=float(input("\tHarga Satuan\t\t: Rp "))
beli=float(input("\tJumlah Pembelian\t: "))
diskon=float(input("\tDiskon (%)\t\t: "))
diskon=satuan*beli*diskon/100
total=satuan*beli-diskon
print(f"\tHarga Total\t\t: Rp {total}")

print("_"*80)
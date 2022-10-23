print("PROGRAM MENGHITUNG PEMBELIAN".center(80))
print("_"*80)
satuan=float(input("\tHarga Satuan\t\t: Rp "))
beli=float(input("\tJumlah Pembelian\t: "))
diskon=satuan*beli*10/100
total=satuan*beli-diskon
print(f"\tDiskon 10%\t\t: Rp {diskon}")
print(f"\tHarga Total\t\t: Rp {total}")
print("_"*80)
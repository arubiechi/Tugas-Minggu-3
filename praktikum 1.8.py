import os
os.system("cls")

print("PROGRAM MENGHITUNG KEBUTUHAN".center(80))
print("_"*80)
gaji=float(input("\nGaji\t\t\t: "))
utang=float(input("Utang\t\t\t: "))
sisa=gaji-utang
print("\nBiaya sehari-hari\t : ",sisa*70/100)
print("Tabungan\t\t : ",sisa*20/100)
print("Infak\t\t\t : ",sisa*10/100)
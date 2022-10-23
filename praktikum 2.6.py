import os
os.system("cls")

print("DATA PEGAWAI".center(50))
print('-'*50)

nama=str(input("\tNama\t\t: "))
golongan=str(input("\tGolongan\t: "))
jamkerja=float(input("\tTotal Jam Kerja\t: "))
print('-'*50)

print("\n")
print("PERHITUNGAN GAJI".center(50))
print('-'*50)

if golongan =='A' or golongan=='a':
    gapok=500000.0
    tunjangan=gapok*10/100
    uanglembur=5000.0
elif golongan =='B'or golongan=='b':
    gapok=700000.0
    tunjangan=gapok*15/100
    uanglembur=7500.0
elif golongan =='C'or golongan=='c':
    gapok=900000.0
    tunjangan=gapok*20/100
    uanglembur=10000.0

if jamkerja >200:
    lembur=jamkerja-200
    uanglembur=uanglembur*lembur
else:
    uanglembur=0
print("\tGaji Pokok\t: ",gapok)
print("\tTunjangan\t: ",tunjangan)
print("\tLebur\t\t: ",uanglembur)

print('-'*50)
print("\tTotal\t\t: ",gapok+tunjangan+uanglembur)

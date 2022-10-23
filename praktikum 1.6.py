import os
os.system("cls")

print("PROGRAM GAJI PEGAWAI".center(80))
nama=str(input("\tNama Karyawan\t\t: "))
anak=float(input("\tJumlah Anak\t\t: "))
print("_"*80)

print("Gaji Pokok\tT.Kesejahteraan\t\tT.Keluarga\t\tPajak")
gp=float(input(end=' '))
tks=20/100
tkl=10/100
pjk=10/100
ttks=gp*tks
ttkl=gp*tkl
pjk=(gp+ttks+ttkl)*pjk
gk=gp+ttks+ttkl
gb=gk-pjk
print("\t".ljust(10),ttks,"\t\t",ttkl,"\t\t",pjk)

print("_"*80)

print("Gaji Kotor   : Rp ",gk)
print("Gaji Bersih  : Rp ",gb)

print("_"*80)
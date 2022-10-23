print("PROGRAM MENGHITUNG TAGIHAN TELEPON".center(80))
print("_"*80)

print("\tDATA PELANGGAN")
nama=str(input("\tNama Pelanggan\t\t: "))
cakap=float(input("\tPercakapan (menit)\t: "))
sms=float(input("\tSMS (kali)\t\t: "))
abod=20000
tcakap=cakap*1000
tsms=sms*300
tagih=abod+tcakap+tsms
print("\tTAGIHAN\n")
print(f"\tAbodemen\t\t: Rp {abod}")
print(f"\tBiaya Percakapan\t: Rp {tcakap}")
print(f"\tBiaya SMS\t\t: Rp {tsms}")
print(f"\tTotal Tagihan\t\t: Rp {tagih}")

print("_"*80)
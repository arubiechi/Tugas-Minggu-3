import os
os.system("cls")

print("DATA NILAI MAHASISWA".center(50))
print('-'*50)
nama=str(input("\tNama\t: "))
tugas=float(input("\tTugas\t: "))
uts=float(input("\tUTS\t: "))
uas=float(input("\tUAS\t: "))
print('-'*50)
print("\n")
print("NILAI AKHIR DAN GRADE".center(50))
print('-'*50)
nilai_akhir=tugas*25/100+uts*35/100+uas*40/100
if nilai_akhir>=75:
    grade='A'
elif 60<=nilai_akhir<75:
    grade='B'
elif 45<=nilai_akhir<60:
    grade='C'
else:
    grade='D'

print("\tNama\t\t: ",nama)
print("\tNilai Akhir\t: ",nilai_akhir)
print("\tGrade\t\t: ",grade)
print("-"*50)

import os
os.system("cls")

dbnama=[]
dbnilai=[]
for i in range(0,5):
    nama=str(input("Masukkan nama : "))
    nilai=int(input("Masukkan nilai : "))
    dbnama.append(nama)
    dbnilai.append(nilai)

print("-"*50)
print("No\t\tNama\t\tNilai")
print("-"*50)
for i in range (0,5):
    print(i+1,"\t\t",dbnama[i],"\t\t",dbnilai[i])

print("-"*50)
print(f"Jumlah mahasiswa : {len(dbnama)}")
print(f"Nilai rata-rata : {sum(dbnilai)/len(dbnilai)}")
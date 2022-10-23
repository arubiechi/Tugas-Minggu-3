import os
os.system("cls")

print("Deret Geometri")
print("-"*30)
awal=int(input("Masukkan suku pertama : "))
rasio=int(input("Masukkan rasio : "))
freq=int(input("Sampai suku ke-"))
for n in range(1,freq+1):
    hasil=awal*(rasio**(n-1))
    print(f"suku ke- {n} : " ,hasil)
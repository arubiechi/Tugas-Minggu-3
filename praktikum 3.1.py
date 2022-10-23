import os
os.system("cls")

i=[0.5,800]
f=0
g=0
berapa=int(input("Berapa kali looping? "))
print("Satuan\t\tHarga")
for n in range(0,berapa):

    f=f+i[0]
    g=g+i[1]
    print(f,"\t\t",g)
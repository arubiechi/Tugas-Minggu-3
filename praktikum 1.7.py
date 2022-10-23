import os
os.system("cls")
uang = int(input('Nilai uang = '))
uang_pecahan = [1000, 200, 50]
jumlah_pecahan = {}
sisa = uang
print(f'{uang}  rupiah = ')
for pecahan in uang_pecahan:
    if sisa < pecahan:
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - ( pecahan * banyak_pecahan )
    print('pecahan {} : {}'.format(pecahan, banyak_pecahan),end=' ')

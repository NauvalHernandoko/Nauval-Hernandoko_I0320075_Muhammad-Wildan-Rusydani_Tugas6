print('=====Program Menghitung Nilai Rata-Rata=====')
nama = input('masukkan nama anda: ')
list_nilai = [ ]
nilai = float(input('masukkan nilai anda: '))
while nilai != '':
    list_nilai.append(float(nilai))
    nilai = input('masukkan nilai anda: ')
rata_rata = sum(list_nilai)/len(list_nilai)
print(rata_rata, 'adalah rata-rata nilai', nama)
if rata_rata >= 60:
    print('Selamat', nama, 'anda lulus')
else:
    print('Maaf', nama, 'anda tidak lulus')
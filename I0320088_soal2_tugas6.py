print("=====Menghitung nilai rata-rata=====")
banyak_data = int(input("Banyak data: "))
data = []
jumlah = 0
for nilai in range(0, banyak_data):
    temp = int(input("Masukkan data ke-%d: " % (nilai+1)))
    data.append(temp)
    jumlah += data [nilai]
    rata_rata = jumlah/banyak_data
print("Rata-ratanya adalah: ", rata_rata)

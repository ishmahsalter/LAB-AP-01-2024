sisi_pertama = int(input("Masukkan panjang sisi pertama: "))
sisi_kedua = int(input("Masukkan panjang sisi kedua: "))
sisi_ketiga = int(input("Masukkan panjang sisi ketiga: "))

if sisi_pertama + sisi_kedua > sisi_ketiga and sisi_pertama + sisi_ketiga > sisi_kedua and sisi_kedua + sisi_ketiga > sisi_pertama:

    # Memeriksa jenis segitiga
    if sisi_pertama == sisi_kedua == sisi_ketiga: 
        print("Segitiga Sama Sisi")
    elif sisi_pertama == sisi_kedua or sisi_kedua == sisi_ketiga or sisi_pertama == sisi_ketiga:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")
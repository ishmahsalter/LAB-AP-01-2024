print("# Program Saham #")
print("===================")
print()

saham = int(input("Masukkan Harga Saham Kemarin : "))
saham_hari_ini = 105
persentase = (saham_hari_ini - saham)/saham * 100

rekomendasi = (persentase > 5 )*"Beli" + (-3 <= persentase < 5)*"Tahan" + (persentase <= -3)*"Jual"
print(f"Perubahan persentase harga saham = {persentase:.2f}%")
print(f"Rekomendasi investasi = {rekomendasi}")
penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB/bulan): ").strip())
waktu_penggunaan = input("Apakah mayoritas penggunaan diluar jam sibuk (off-peak) atau di jam sibuk (peak)?").strip()
jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis?").strip()

if penggunaan_data < 10 and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
    print("Paket yang cocok: Paket A")
elif 10 <= penggunaan_data <= 50 and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    print("Paket yang cocok: Paket B")
elif penggunaan_data > 50 and waktu_penggunaan == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
    print("Paket yang cocok: Paket C")
elif penggunaan_data > 50 and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
    print("Paket yang cocok: Paket D")
else:
    print("Tidak ada paket yang cocok") 
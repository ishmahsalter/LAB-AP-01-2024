pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# Total dari harga yang dibayar
total_harga = int(input("Masukkan total harga: "))
uang_dibayar = int(input("Masukkan uang yang diberikan: "))

if total_harga > uang_dibayar: 
    print("Uang Anda Tidak Cukup.")
    exit()
    
# Kembalian
kembalian = uang_dibayar - total_harga

print("Kembalian:")

# Jumlah pecahan uang
for pecahan_uang in pecahan:
    jumlah_pecahan = kembalian // pecahan_uang
    kembalian %= pecahan_uang
    if jumlah_pecahan > 0:
        print(f"{jumlah_pecahan} lembar Rp {pecahan_uang:,}")
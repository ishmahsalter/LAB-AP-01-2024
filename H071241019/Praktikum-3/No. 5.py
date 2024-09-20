populasi_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_B = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

# Loop untuk setiap hari
for hari in range(1, jumlah_hari + 1):
    # Populasi berdasarkan hari ganjil atau genap
    if hari % 2 == 1:
        populasi_A *= 1.3  # Pertumbuhan 30%
        populasi_B *= 1.5  # Pertumbuhan 50%
    else:
        populasi_A *= 0.8  # Penurunan 20%
        populasi_B *= 0.6  # Penurunan 40%
    if populasi_A < 1: 
        populasi_A = 0 
    if populasi_B < 1: 
        populasi_B = 0 

    # Jika hari kelipatan 5, predator memakan 10% dari total populasi
    if hari % 5 == 0:
        total_populasi = populasi_A + populasi_B
        populasi_A *= 0.9
        populasi_B *= 0.9
        print(f'hari ke {hari}: Predator memakan 10% populasi.') 

    print(f"Hari {hari}: Serangga A {f"= {int(populasi_A)}" if populasi_A > 0 else "Telah habis."}, Serangga B {f"= {int(populasi_B)}" if populasi_B > 0 else "Telah habis."}")
N = int(input("Masukkan jumlah baris (N): "))
M = int(input("Masukkan jumlah kolom (M): "))

# posisi awal 
baris = 0
kolom = 0

# mengontrol pergerakan robot
while baris < N:
    # Bergerak ke kanan sampai ujung baris
    if (baris%2 == 0):
        while kolom < M:
            print(f"MOVE to ({baris},{kolom})")
            kolom += 1
        kolom -= 1
    else: 
        while kolom >= 0:
            print(f"MOVE to ({baris},{kolom})")
            kolom -= 1 
        kolom += 1

    # Turun satu baris
    baris += 1
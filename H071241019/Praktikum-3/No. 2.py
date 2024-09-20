import random

# Generate angka acak antara 1 sampai 100
angka_rahasia = random.randint(1, 101)

maksimal_percobaan = 5

print("Selamat datang di permainan Tebak Angka!")
print("Tebak angka antara 1 sampai 100.")

for percobaan in range(maksimal_percobaan):
    tebakan = input("Masukkan tebakan Anda  (0 untuk berhenti):")
    
    # Jika pemain ingin berhenti
    if tebakan == '0':
        print("Anda memilih untuk berhenti.")
        break

    # Konversi tebakan menjadi angka
    try:
        tebakan = int(tebakan)
    except ValueError:
        print("Input harus berupa angka.")
        continue

    if tebakan == angka_rahasia:
        print("Selamat! Anda menebak angka dengan benar.")
        break 
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")

if (percobaan+1) == maksimal_percobaan:
    print("Anda kehabisan percobaan. Angka rahasianya adalah:", angka_rahasia)
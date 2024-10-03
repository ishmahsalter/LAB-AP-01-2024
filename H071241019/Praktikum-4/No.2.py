def langkah():
    try:
        return int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")
        return langkah()

def cek_bahaya(langkah):
    return langkah > 20

def main():
    jarak_total = 0
    bahaya = False

    print("Selamat datang di perburuan harta karun!")

    while True:
        jarak = langkah()

        if jarak <= 0:
            # Pemain berhenti, evaluasi hasil akhir
            break

        jarak_total += jarak
        if cek_bahaya(jarak):
            bahaya = True
            break

        if jarak_total >= 50:
            break

    # Tampilkan hasil akhir setelah permainan selesai
    print(f"Total jarak: {jarak_total} meter")
    print(f"Ada bahaya: {'Ya' if bahaya else 'Tidak'}")

    if bahaya:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif jarak_total == 50:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")

main()

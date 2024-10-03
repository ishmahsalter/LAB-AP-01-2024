def hitung_langkah(n):
    langkah = 0
    # Perulangan sampai n menjadi 1
    while n != 1:
        if n % 2 == 0:
            n //= 2  # Jika genap, bagi 2
        else:
            n = 3 * n + 1  # Jika ganjil, kalikan 3 lalu tambah 1
        print(float(n))  # Cetak nilai n dalam bentuk desimal
        langkah += 1
    return langkah

def main():
    try:
        # Meminta input dari pengguna
        n = int(input("Masukkan angka: "))
        if n <= 0:
            print("Input tidak Valid")
        else:
            langkah = hitung_langkah(n)
            print(f"Jumlah langkah: {langkah}")
    except ValueError:
        # Menangani input yang bukan angka bulat
        print("Input tidak Valid")

main()
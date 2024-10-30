inventory = {}

def tampilkan_menu():
    print("=== Menu Inventory Barang ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

def tambah_barang():
    print("=== Tambah Barang ===")
    id = input("Masukkan ID Barang: ")
    nama = input("Masukkan Nama Barang: ")

    # Validasi jumlah dan harga
    while True:
        try:
            jumlah = int(input("Masukkan Jumlah Barang (harus angka): "))
            break
        except ValueError:
            print("Jumlah harus berupa angka!")

    while True:
        try:
            harga = float(input("Masukkan Harga Barang (harus angka): "))
            break
        except ValueError:
            print("Harga harus berupa angka!")

    inventory[id] = {"nama": nama, "jumlah": jumlah, "harga": harga}
    print("Barang berhasil ditambahkan!")

def hapus_barang():
    print("=== Hapus Barang ===")
    id = input("Masukkan ID Barang yang ingin dihapus: ")

    if id in inventory:
        del inventory[id]
        print("Barang berhasil dihapus!")
    else:
        print("ID Barang tidak ditemukan!")

def tampilkan_daftar_barang():
    print("=== Daftar Barang ===")
    if not inventory:
        print("Tidak ada barang dalam inventory.")
    else:
        for id, data in inventory.items():
            print(f"ID: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")

def cari_barang():
    print("=== Cari Barang ===")
    id = input("Masukkan ID Barang yang ingin dicari: ")

    if id in inventory:
        data = inventory[id]
        print(f"ID: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("ID Barang tidak ditemukan!")

def update_barang():
    print("=== Update Data Barang ===")
    id = input("Masukkan ID Barang yang ingin diupdate: ")

    if id in inventory:
        nama_baru = input("Masukkan Nama Barang baru (kosongkan jika tidak ingin mengubah): ")
        jumlah_baru = input("Masukkan Jumlah Barang baru (kosongkan jika tidak ingin mengubah): ")
        harga_baru = input("Masukkan Harga Barang baru (kosongkan jika tidak ingin mengubah): ")

        if nama_baru:
            inventory[id]["nama"] = nama_baru
        if jumlah_baru:
            try:
                inventory[id]["jumlah"] = int(jumlah_baru)
            except ValueError:
                print("Jumlah harus berupa angka!")
        if harga_baru:
            try:
                inventory[id]["harga"] = float(harga_baru)
            except ValueError:
                print("Harga harus berupa angka!")
                
        print("Data barang berhasil diupdate!")
    else:
        print("ID Barang tidak ditemukan!")

def main():
    while True:
        tampilkan_menu()
        opsi = input("Pilih opsi (1-6): ")

        if opsi == "1":
            tambah_barang()
        elif opsi == "2":
            hapus_barang()
        elif opsi == "3":
            tampilkan_daftar_barang()
        elif opsi == "4":
            cari_barang()
        elif opsi == "5":
            update_barang()
        elif opsi == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Opsi tidak valid! Silakan pilih lagi.")

main()
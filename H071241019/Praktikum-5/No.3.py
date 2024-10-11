def hitung_penghapusan_anagram(str1, str2):
    # Membuat set karakter unik dari kedua string
    semua_karakter = set(str1) | set(str2)
    
    # Hitung total penghapusan dengan menjumlahkan selisih frekuensi karakter dari kedua string
    total_hapus = sum(abs(str1.count(char) - str2.count(char)) for char in semua_karakter)
    
    return total_hapus

# Input dari pengguna
str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

hasil = hitung_penghapusan_anagram(str1, str2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")

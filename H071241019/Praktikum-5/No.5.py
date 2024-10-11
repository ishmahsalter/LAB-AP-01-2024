def caesar_cipher_enkripsi(teks, shift):
    hasil = ""
    
    # Proses enkripsi
    for char in teks:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            # Menentukan batas (a-z atau A-Z)
            batas = ord('a') if char.islower() else ord('A')
            # Menggeser huruf dan memastikan tetap dalam batas abjad
            char = chr((ord(char) - batas + shift) % 26 + batas)
        # Karakter lainnya tetap sama
        hasil += char
    
    return hasil               

# Input dari pengguna
input_string = input("Masukkan String: ")
jumlah_pergeseran = int(input("Masukkan jumlah pergeseran: "))

# Enkripsi dengan Caesar Cipher
cipher_text = caesar_cipher_enkripsi(input_string, jumlah_pergeseran)

# Output hasil enkripsi
print(f"Text: {input_string}")
print(f"Shift: {jumlah_pergeseran}")
print(f"Cipher: {cipher_text}")

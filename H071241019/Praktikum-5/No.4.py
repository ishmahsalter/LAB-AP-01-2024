def cetak_substring(s):
    print("====================")
    # Iterasi untuk panjang substring yang berbeda
    for panjang in range(1, len(s) + 1):
        # Iterasi untuk setiap substring dengan panjang tertentu
        for i in range(len(s) - panjang + 1):
            print(s[i:i + panjang])

# Input dari pengguna
input_string = input("Input your string: ")

# Cetak semua substring
cetak_substring(input_string)

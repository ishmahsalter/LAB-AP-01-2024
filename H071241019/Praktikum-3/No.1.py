
try:
    n = int(input("Masukkan jumlah baris: "))
except ValueError:
    print("Input harus berupa angka.")
    exit()

# Bagian atas 
for a in range((n+1)//2):
    for b in range((n - 1)//2 - a):
        print(' ', end=" ")
    
    for c in range(2 * a + 1):
        print('*', end=" ")
    print()

# Bagian bawah 
for a in range((n//2)-1, -1, -1):
    for b in range((n - 1)//2 - a):
        print(' ', end=" ")
        
    for c in range(2 * a + 1):
        print('*', end=" ")
    print()
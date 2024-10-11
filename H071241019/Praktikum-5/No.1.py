def Palindrome(kalimat):
    kalimat = kalimat.replace(" ", "").lower()
    reversed_kalimat = ''.join(reversed(kalimat))
    
    # Check if the original and reversed strings are the same
    if kalimat == reversed_kalimat:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

Palindrome("Ibu Ratna Antar Ubi") 
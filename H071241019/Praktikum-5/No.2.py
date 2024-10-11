def singkat_akronim(kalimat):
    return ''.join(kata[0].upper() for kata in kalimat.split())

print(singkat_akronim("Dewan Perwakilan Rakyat"))
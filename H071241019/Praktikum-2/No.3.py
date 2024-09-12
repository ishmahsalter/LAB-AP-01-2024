nilai_akhir = int(input("Masukkan nilai akhir: "))
persentase_kehadiran = float(input("Masukkan persentase kehadiran (%): "))

# Memeriksa apakah mahasiswa memenuhi syarat kehadiran
if persentase_kehadiran < 75:
    print("Tidak Lulus: Kehadiran kurang dari 75%.")
else:
    # Memeriksa kelulusan berdasarkan nilai akhir dan tugas tambahan
    if nilai_akhir >= 85:
        print("Lulus dengan Predikat A.")
    elif 70 <= nilai_akhir < 85:
        print("Lulus dengan Predikat B.")
    elif 60 <= nilai_akhir < 70:
        print("Lulus dengan Predikat C.")
    elif nilai_akhir < 60:
        # Memeriksa apakah mahasiswa memenuhi syarat tugas tambahan untuk lulus dengan C
        tugas_tambahan = int(input("Masukkan nilai tugas tambahan: "))
        if tugas_tambahan > 70:
            print("Lulus dengan Predikat C (berdasarkan tugas tambahan).")
        else:
            print("Tidak Lulus: Nilai akhir di bawah 60 dan tugas tambahan tidak mencukupi.")
# Program Konversi Jam dan Menit dalam Python

def konversi_ke_menit(jam, menit):
    return jam * 60 + menit

def konversi_ke_jam(menit):
    jam = menit // 60
    menit_sisa = menit % 60
    return jam, menit_sisa

def main():
    print("Program Konversi Jam dan Menit")

    print("\nPilih opsi konversi:")
    print("1. Konversi Jam dan Menit ke Menit")
    print("2. Konversi Menit ke Jam dan Menit")

    pilihan = int(input("\nMasukkan pilihan (1/2): "))

    if pilihan == 1:
        jam = int(input("\nMasukkan jumlah jam: "))
        menit = int(input("Masukkan jumlah menit: "))
        total_menit = konversi_ke_menit(jam, menit)
        print(f"\n{jam} jam {menit} menit = {total_menit} menit.")
    
    elif pilihan == 2:
        menit = int(input("\nMasukkan jumlah menit: "))
        jam, menit_sisa = konversi_ke_jam(menit)
        print(f"\n{menit} menit = {jam} jam {menit_sisa} menit.")
    
    else:
        print("\nPilihan tidak valid!")


def jumlah_matriks(matriks1, matriks2):
    hasil = [
        [matriks1[0][0] + matriks2[0][0], matriks1[0][1] + matriks2[0][1]],
        [matriks1[1][0] + matriks2[1][0], matriks1[1][1] + matriks2[1][1]],
    ]
    return hasil

def firna():
    print("=== Penjumlahan Matriks 2x2 ===")
    matriks1 = [[int(input("Matriks1[0][0]: ")), int(input("Matriks1[0][1]: "))],
                [int(input("Matriks1[1][0]: ")), int(input("Matriks1[1][1]: "))]]
    matriks2 = [[int(input("Matriks2[0][0]: ")), int(input("Matriks2[0][1]: "))],
                [int(input("Matriks2[1][0]: ")), int(input("Matriks2[1][1]: "))]]

    hasil = jumlah_matriks(matriks1, matriks2)
    print("Hasil Penjumlahan Matriks:")
    for baris in hasil:
        print(baris)

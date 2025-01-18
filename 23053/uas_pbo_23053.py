class Bunga:
    def __init__(self, nama, warna, jenis):
        self.nama = nama 
        self.warna = warna
        self.jenis = jenis

    def deskripsi(self):
        print(f"Bunga: {self.nama}, Warna: {self.warna}, Jenis: {self.jenis}")
    
    def ubah_warna(self, warna_baru):
        self.warna = warna_baru
        print(f"Warna {self.nama} telah diubah menjadi: {self.warna}")

def bunga():
    bunga1 = Bunga("Mawar", "Merah", "Mawar Hybrid")
    bunga1.deskripsi()


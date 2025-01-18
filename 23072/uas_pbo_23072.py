class Wisata:
    def __init__(self, nama_tempat, jenis_wisata, alamat):
        self.nama_tempat = nama_tempat
        self.jenis_wisata = jenis_wisata
        self.alamat = alamat

    def info_wisata(self):
        return f"{self.nama_tempat} adalah tempat wisata {self.jenis_wisata}\nAlamat: {self.alamat}\n"


# Fungsi untuk setiap tempat wisata
def wisata_benteng_oranje():
    benteng_oranje = Wisata("Benteng Oranje", "sejarah", "Kecamatan Ternate Tengah, Kota Ternate")
    return benteng_oranje.info_wisata()


def wisata_pantai_sulamadaha():
    pantai_sulamadaha = Wisata("Pantai Sulamadaha", "pantai", "Kecamatan Ternate Barat, Kota Ternate")
    return pantai_sulamadaha.info_wisata()


def wisata_danau_tolire():
    danau_tolire = Wisata("Danau Tolire", "alam", "Kecamatan Ternate Barat, Kota Ternate")
    return danau_tolire.info_wisata()


def wisata_kedaton_sultan():
    kedaton_sultan = Wisata("Kedaton Sultan Ternate", "sejarah", "Kelurahan Salero, Kecamatan Ternate Utara")
    return kedaton_sultan.info_wisata()


def wisata_pulau_maitara():
    pulau_maitara = Wisata("Pulau Maitara", "pantai", "Antara Pulau Ternate dan Tidore")
    return pulau_maitara.info_wisata()


def wisata_pantai_tobololo():
    pantai_tobololo = Wisata("Pantai Tobololo", "pantai", "Desa Tobololo, Kecamatan Ternate Barat")
    return pantai_tobololo.info_wisata()


def wisata_gunung_gamalama():
    gunung_gamalama = Wisata("Gunung Gamalama", "pendakian", "Pusat Pulau Ternate, Kota Ternate")
    return gunung_gamalama.info_wisata()

def sambarang():
    print(wisata_benteng_oranje() + "\n" + wisata_pantai_sulamadaha() + "\n" + wisata_danau_tolire() + "\n" + wisata_kedaton_sultan() + "\n" + wisata_pulau_maitara() + "\n" + wisata_pantai_tobololo() + "\n" + wisata_gunung_gamalama())


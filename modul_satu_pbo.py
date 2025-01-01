# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/

# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini

# Definisi kelas Mahasiswa dan kelas turunannya

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_data(self):
        return f"Nama: {self.nama}, NIM: {self.nim}"

# Class turunan dari Mahasiswa (Inheritance)
class MahasiswaTeknik(Mahasiswa):
    def __init__(self, nama, nim, jurusan):
        super().__init__(nama, nim)
        self.jurusan = jurusan

    def tampilkan_data(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}"

# Class turunan lain untuk Mahasiswa Ekonomi (Polymorphism)
class MahasiswaEkonomi(Mahasiswa):
    def __init__(self, nama, nim, konsentrasi):
        super().__init__(nama, nim)
        self.konsentrasi = konsentrasi

    def tampilkan_data(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Konsentrasi: {self.konsentrasi}"



# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/
# .
# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;
        
# ini Kontribusi dari Ikhwan 
def batas():
    print("-"*35)

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini

#modul_satu_pbo.py

class Mahasiswa:
    def __init__(self, name, npm, jurusan):
        self.name = name
        self.npm = npm
        self.jurusan = jurusan
        self.nilai = []

    def tambah_nilai(self, mata_kuliah, nilai):
        self.nilai.append({"mata_kuliah": mata_kuliah, "nilai": nilai})

    def rata_rata_nilai(self):
        if not self.nilai:
            return 0
        total_nilai = sum([item["nilai"] for item in self.nilai])
        return total_nilai / len(self.nilai)

    def tampilkan_info(self):
        print(f"Nema: {self.name}")
        print(f"NPM: {self.npm}")
        print(f"Jurusan: {self.jurusan}")
        print("Nilai:")
        for item in self.nilai:
            print(f"  {item['mata_kuliah']}: {item['nilai']}")
        print(f"Rata-rata Nilai: {self.rata_rata_nilai():.2f}")

# <<<<<<< main Alifia 
#Ini Kontribusi Alifia Risman
class alifia:
    def __init__(self,nama,npm,jurusan,kelas,hobi):
        self.n=nama
        self.npm=npm
        self.j=jurusan
        self.k=kelas
        self.h=hobi

    def alifia1(self):
        print(f"Nama Saya {self.n} Npm Saya {self.npm} Jurusan Saya {self.j} Kelas {self.k} Hobi Saya {self.h}")

def alifia_fungsi(nilai):
    if nilai >= 80:
        print("Nilai Yang Anda Peroleh Adalah : A")
    elif nilai >=70:
        print("Nilai Yang Anda Peroleh Adalah : B")
    elif nilai >=60:
        print("Nilai Yang Anda Peroleh Adalah : C")
    elif nilai >=50:
        print("Nilai Yang Anda Peroleh Adalah : D")
    else:
        print("Nilai Yang Anda Peroleh Adalah : E")
# ======= Alifia 
# <<<<<<< main  Firna
#Ini Kontribusi Firna
class firna:
# =======  Firna


#ini kontribusi nurul
class nurul:
# >>>>>>> main 
    def __init__(self,nama,umur,hobi,alamat,jurusan):
        self.nama=nama
        self.umur=umur
        self.hobi=hobi
        self.alamat=alamat
        self.jurusan=jurusan

# <<<<<<< main

# =======
# >>>>>>> main
    def proses (self):
        print(f"nama saya {self.nama} umur saya {self.umur} hobi saya {self.hobi} almat saya {self.alamat} jurusan saya {self.jurusan}")

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b

def pangkat(a, b):
    return a ** b

def akar(a):
    if a < 0:
        return "Error: Tidak dapat menghitung akar kuadrat dari angka negatif."
    return a ** 0.5

def input3():
    return int(input("masukan nilai : "))
# <<<<<<< main
# =======

#modul_satu_pbo_Diki.py

class informasi:
    def __init__ (self, nama, npm, kelas, jurusan, hobi, umur, alamat):
        self.n=nama
        self.npm=npm
        self.k=kelas
        self.j=jurusan
        self.h=hobi
        self.u=umur
        self.a=alamat

    def panggil (self):
        print(f"Nama Saya {self.n}, Npm Saya {self.npm}, Kelas {self.k}, Jurusan {self.j}, Hobi Saya {self.h}, Umur Saya {self.u}, Alamat saya di {self.a}")

def nilai1():
    return nilai(int(input("Masukan Nilai Anda : ")))

def nilai(nilai):
    if nilai >=80:
        print("A")
    elif nilai >=70:
        print("B")
    elif nilai >=60:
        print("C")
    elif nilai >=50:
        print("D")
    else:
        print("E")
    return nilai1()

#ini kontribusi MOH. JASMIN RUMALEAN
class jasmin:
    def __init__ (self, nama, npm, jurusan, tahun_masuk):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
        self.tahun_masuk = tahun_masuk
    def tampilkan_info(self):
        print(f"NAMA: {self.nama}")
        print(f"NPM: {self.npm}")
        print(f"JURUSAN: {self.jurusan}")
        print(f"TAHUN MASUK: {self.tahun_masuk}")
    
def usia_kuliah(usia):
    print(f"Mahasiswa ini sudah kuliah selama {usia} tahun.")
        
def halo():
    print(" Selamat datang di Program Mahasiswa Informatika ")

#Ini Kontribusi Dari Muh. Fadel Nur
class fadel:
    def __init__ (self, nama, npm, kelas, alamat, asal):
        self.n=nama
        self.npm=npm
        self.k=kelas
        self.a=alamat
        self.asal=asal

    def output(self):
        print(f"Nama Saya \t\t: {self.n} \nNpm Saya \t\t: {self.npm} \nKelas \t\t\t: {self.k} \nAlamat Saya Di \t\t: {self.a} \nAsal Saya Dari \t\t: {self.asal}")

def fadel_0():
    return fadel_1(int(input("Masukan Nilai Anda : ")))

def fadel_1(nilai):
    if nilai >= 80:
        print("Nilai Yang Anda Peroleh Adalah : A")

    elif nilai >=70:
        print("Nilai Yang Anda Peroleh Adalah : B")

    elif nilai >=60:
        print("Nilai Yang Anda Peroleh Adalah : C")

    elif nilai >=50:
        print("Nilai Yang Anda Peroleh Adalah : D")

    else:
        print("Nilai Yang Anda Peroleh Adalah : E")

    return fadel_3(str(input("Apakah Anda Ingin Mengulangi Program ( Y / T ) : ")))
    
def fadel_3(masukan):
    if masukan == "Y":
        return fadel_0()
    
    if masukan == "y":
        return fadel_0()
    
    if masukan == "T":
        print("Ini Adalah Akhir Program Terima Kasih Sudah Mencoba Program FADEL :) ")

    if masukan == "t":
        print("Ini Adalah Akhir Program Terima Kasih Sudah Mencoba Program FADEL :) ")

    else:
        print("Ini Adalah Akhir Program Terima Kasih Sudah Mencoba Program FADEL :) ")

# ini Kontribusi dari Refalina
# modul_satu_pbo.py

class Course:
    def __init__(self, kode, nama_mata_kuliah):
        self.kode = kode
        self.nama_mata_kuliah = nama_mata_kuliah
        self.mahasiswa_terdaftar = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_terdaftar.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        print(f"Mata Kuliah: {self.nama_mata_kuliah} ({self.kode})")
        print("Mahasiswa yang Terdaftar:")
        for mahasiswa in self.mahasiswa_terdaftar:
            print(f"- {mahasiswa.name} ({mahasiswa.npm})")
            
# Pengujian Kelas Course
if __name__ == "__main__":
    # Membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa("Budi", "123456", "Informatika")
    mahasiswa2 = Mahasiswa("Siti", "654321", "Matematika")
    
    # Membuat objek Course dan menambahkan mahasiswa
    kursus = Course("IF101", "Pemrograman Berorientasi Objek")
    kursus.tambah_mahasiswa(mahasiswa1)
    kursus.tambah_mahasiswa(mahasiswa2)
    
    # Menampilkan informasi kursus
    kursus.tampilkan_mahasiswa()

# <<<<<<< main khumayra07
#Ini Kontribusi Khumayra A Habsy
class pinky:
    def __init__(self,nama,jurusan,npm,kelas,alamat,umur):
        self.nama=nama 
        self.jurusan=jurusan 
        self.npm=npm 
        self.kelas=kelas 
        self.alamat=alamat 
        self.umur=umur
    def mimo(self):
        print(f"nama saya {self.nama} Jurusan { self.jurusan} Npm saya {self.npm} Kelas {self.kelas} Alamat Saya {self.alamat} Umur Saya {self.umur} Tahun")

def hitung_luas(panjang, lebar):
 return panjang * lebar

# ======= khumayra07
# <<<<<<< main  kardichen27
#Ini Kontribusi La Kardi
class kardi0:
# ======= kardichen27 khumayra07
# <<<<<<< main Sarif04



# ini kontribusi dari sarif soleman
class sarif:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


def sarif1(nama,npm,kelas,ipk):
    print(f"nama saya {nama} npm saya {npm} kelas saya {kelas} ipk saya {ipk}")
# ======= Sarif04
#Ini Kontribusi Dari Srinagita Irwan
class gita_c: 
# >>>>>>> main kardichen27
    def __init__(self,nama,kelas,jurusan,npm,alamat,hobi,umur):
        self.nama=nama
        self.kelas=kelas
        self.jurusan=jurusan
        self.npm=npm
        self.alamat=alamat
        self.hobi=hobi
        self.umur=umur

# <<<<<<< main kardichen27
    def kardi1(self):
        print(f"Perkenalkan nama saya {self.nama} saya dari kelas {self.kelas} jurusan {self.jurusan} npm {self.npm} dan alamat saya dikelurahan {self.alamat} dan hobi saya yaitu {self.hobi} sedangkan umur saya {self.umur}")

def kardi_tambah(a,b):
    print(a+b)

def kardi_kurang(a,b):
    print(a-b)

def kardi_kali(a,b):
    print(a*b)

def kardi_bagi(a,b):
    print(a/b)
# ======= kardichen27
    def gita1(self):
        print(f"Perkenalkan nama saya {self.nama} saya dari kelas {self.kelas} jurusan {self.jurusan} npm saya {self.npm} alamat saya {self.alamat} dan hobi saya {self.hobi} umur saya {self.umur}")

def gita_tambah(a,b):
    print(a+b)

def gita_kurang(a,b):
    print(a-b)

def gita_kali(a,b):
    print(a*b)

def gita_bagi(a,b):
    print(a/b)


# >>>>>>> main
# >>>>>>> main Alifia 
# >>>>>>> main Sarif04
# >>>>>>> main kardichen27
# >>>>>>> main khumayra07

# <<<<<<< main 
#ini kontribusi dari sulastri
# bunga.py

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
# ======= Lastryyy
#ini kontribusi dari nursin
class ocin_sahrin:
    def __init__(self,nama,npm,jurusan,alamat):
        self.nama=nama
        self.npm=npm
        self.jurusan=jurusan
        self.alamat=alamat

    def rimex(self):
        print(f"nama saya {self.nama} npm saya {self.npm} saya dari jurusan {self.jurusan} alamat saya {self.alamat}")

def ocin_kalkulator():
    return int(input("masukkan nilai : "))

def ocin_tambah(a,b):
    print(a+b)

def ocin_kurang(a,b):
    print(a-b)

def ocin_kali(a,b):
    print(a*b)

def ocin_bagi(a,b):
    print(a/b)

def lani(data):
    if data =="+":
        return ocin_tambah(ocin_kalkulator(),ocin_kalkulator())
    if data =="-":
        return ocin_kurang(ocin_kalkulator(),ocin_kalkulator())
    if data =="*":
        return ocin_kali(ocin_kalkulator(),ocin_kalkulator())
    if data =="/":
        return ocin_bagi(ocin_kalkulator(),ocin_kalkulator())

# >>>>>>> main Lastryyy

#ini konstribusi dari marisa husen

class BankAccount:
    def __init__(self, pemilik, saldo=0):
        """Inisialisasi objek akun dengan pemilik dan saldo (default saldo 0)"""
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        """Menambahkan uang ke saldo"""
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Setoran: Rp{jumlah}. Saldo baru: Rp{self.saldo}.")
        else:
            print("Jumlah setoran harus positif.")

    def tarik(self, jumlah):
        """Menarik uang dari saldo, jika saldo mencukupi"""
        if jumlah > 0 and jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Penarikan: Rp{jumlah}. Saldo baru: Rp{self.saldo}.")
        elif jumlah > self.saldo:
            print("Saldo tidak mencukupi.")
        else:
            print("Jumlah penarikan harus positif.")

    def cek_saldo(self):
        """Menampilkan saldo terkini"""
        print(f"Saldo akun {self.pemilik}: Rp{self.saldo}")


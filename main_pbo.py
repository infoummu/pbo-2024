# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")


# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py


# Import kelas dari file kelas_mahasiswa.py
from kelas_mahasiswa import Mahasiswa, MahasiswaTeknik, MahasiswaEkonomi

# Main Program
if __name__ == "__main__":
    # Membuat objek dari masing-masing kelas
    mhs1 = Mahasiswa("Ariyanti", "23072")
    mhs2 = MahasiswaTeknik("Budi", "987654321", "Teknik Informatika")
    mhs3 = MahasiswaEkonomi("Citra", "567890123", "Manajemen Keuangan")

    # Menampilkan data mahasiswa
    print(mhs1.tampilkan_data())
    print(mhs2.tampilkan_data())
    print(mhs3.tampilkan_data())

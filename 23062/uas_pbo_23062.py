class dila:
    def __init__(self,nama,kelas,jurusan,npm):
        self.nama=nama
        self.kelas=kelas
        self.jurusan=jurusan
        self.npm=npm


    def info3(self):
        print(f" nama saya : {self.nama}\nkelas saya : {self.kelas}\njurusan saya : {self.jurusan}\nnpm saya : {self.npm}\n")

def apa():
    ini=dila("dila","info3","informatika","23062")
    ini.info3()


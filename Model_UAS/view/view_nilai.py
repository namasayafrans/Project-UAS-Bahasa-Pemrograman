from model.daftar_nilai import *
class mencari():
    def cetak_daftar_nilai(self):
        if data.items():
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1],
                                                                                            x[1][2], x[1][3], x[1][4],
                                                                                            i))
            print("==================================================================\n")
        else:
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                        TIDAK ADA DATA!                         |")
            print("==================================================================\n")

    def cetak_hasil_pencarian(self):
        cari_nama = input('masukkan nama yang diinginkan: ')
        if cari_nama in data:
            print("\n\033[93m================================================================")
            print("|                   DAFTAR NILAI MAHASISWA                  |")
            print("=============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("=============================================================")

            for x in data.items():
                print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2],
                                                                                    x[1][3], x[1][4]))
            print("==================================================================\n")
        else:
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                        TIDAK ADA DATA!                         |")
            print("==================================================================\n")
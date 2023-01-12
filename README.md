# Project UAS di Readme.md

```
Nama  : Frans Putra Sinaga
Nim   : 312210
Kelas : TI.22.A1
```

## MODEL/daftar_nilai.py

MODEL/daftar_nilai.py merupakan modul yang berisi empat buah fungsi utama, yaitu tambah_data, ubah_data, hapus_data, dan cari_data. Setiap fungsi memiliki parameter dan tipe data yang berbeda-beda, sehingga dapat digunakan untuk mengelola data penilaian mahasiswa dengan cara yang sesuai.
Fungsi tambah_data berfungsi untuk menambahkan data penilaian mahasiswa ke daftar nilai. Fungsi ini memiliki parameter daftar (list) dan data (tuple), kemudian menambahkan data ke daftar nilai dengan menggunakan perintah daftar.append(data).
Fungsi ubah_data berfungsi untuk mengubah data penilaian mahasiswa yang ada di daftar nilai. Fungsi ini memiliki parameter daftar (list), data_baru (tuple), dan data_lama (tuple), kemudian mengubah data yang ada di daftar nilai dengan menggunakan perintah for dan if.
Fungsi hapus_data berfungsi untuk menghapus data penilaian mahasiswa dari daftar nilai. Fungsi ini memiliki parameter daftar (list) dan data (tuple), kemudian menghapus data dari daftar nilai dengan menggunakan perintah daftar.remove(data).
Fungsi cari_data berfungsi untuk mencari data penilaian mahasiswa di daftar nilai. Fungsi ini memiliki parameter daftar (list) dan data (tuple), kemudian mencari data di daftar nilai dengan menggunakan perintah for dan if. Jika data ditemukan, maka data tersebut dikembalikan kepada pengguna. Jika tidak, maka akan dikembalikan pesan "Data tidak ditemukan.".

![Screenshot (54)](https://user-images.githubusercontent.com/115770839/211953990-97b4fc81-1e10-4b16-b0f6-a045622805d7.png)

![Screenshot (55)](https://user-images.githubusercontent.com/115770839/211954020-6e359199-33d2-4786-b5d9-3c22303f43aa.png)

## Penjelasan dari VIEW/input_nilai.py

VIEW/input_nilai.py merupakan modul yang berisi satu buah fungsi utama, yaitu input_data. Fungsi ini berfungsi untuk meminta input data penilaian mahasiswa dari pengguna.
Fungsi ini tidak memiliki parameter, namun akan mengembalikan tuple yang berisi nama, NIM, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir. Setiap data diperoleh dengan menggunakan perintah input() yang akan meminta pengguna memasukkan data terkait. Nilai akhir dihitung dengan menggunakan rumus yang telah ditentukan, yaitu (tugas * 0.3) + (uts * 0.35) + (uas * 0.35).

![Screenshot (56)](https://user-images.githubusercontent.com/115770839/211954207-27d32bb1-83bc-444c-993d-8c8bb6e78c6e.png)

![Screenshot (57)](https://user-images.githubusercontent.com/115770839/211954243-09d88eb7-f3c7-411a-9942-5027905197c6.png)

## Penjelasan dari VIEW/view_nilai.py

Kode pada VIEW/view_nilai.py merupakan modul yang berisi dua buah fungsi utama, yaitu cetak_daftar_nilai dan cetak_hasil_pencarian. Kedua fungsi ini memiliki fungsi yang sesuai dengan namanya, yaitu mencetak daftar nilai atau hasil pencarian ke layar pengguna.
Fungsi cetak_daftar_nilai memiliki parameter daftar (list) yang berisi data penilaian mahasiswa, kemudian mencetak daftar nilai tersebut ke layar pengguna dengan menggunakan perintah print() dan for.
Fungsi ini tidak mengembalikan nilai apapun. Fungsi cetak_hasil_pencarian memiliki parameter data (tuple atau string) yang berisi data penilaian mahasiswa atau pesan "Data tidak ditemukan.", kemudian mencetak data tersebut ke layar pengguna dengan menggunakan perintah print(). Fungsi ini tidak mengembalikan nilai apapun.

![Screenshot (58)](https://user-images.githubusercontent.com/115770839/211954472-68077f57-3c56-4be3-8464-10c06eaf9a71.png)

![Screenshot (59)](https://user-images.githubusercontent.com/115770839/211954507-226638f3-169d-4b3b-9907-944fe875e122.png)

##Penjelasan MAIN.PY

Kode pada MAIN.PY merupakan program utama yang akan dijalankan oleh interpreter Python. Program ini bertugas menjalankan seluruh fungsi yang terdapat dalam modul MODEL.daftar_nilai, VIEW.input_nilai, dan VIEW.view_nilai sesuai dengan pilihan yang dipilih oleh pengguna.
Program ini akan menampilkan menu pilihan kepada pengguna, yaitu:
1.	Tambah data
2.	Ubah data
3.	Hapus data
4.	Cari data
5.	Lihat seluruh data
6.	Keluar
Untuk setiap pilihan, program akan memanggil fungsi yang sesuai dengan pilihan tersebut. Setelah fungsi selesai dijalankan, program akan kembali menampilkan menu pilihan kepada pengguna. Jika pengguna memilih pilihan ke-6 (Keluar), maka program akan berhenti.

![hai 6](https://user-images.githubusercontent.com/115526901/211405034-d36eb4f2-feec-4b83-ab11-0733d311ae31.png)

## Hasila Runningannya 

![hai 7](https://user-images.githubusercontent.com/115526901/211405189-f5687722-4e9c-4aa8-9f84-084036c2fe93.png)

![hai 8](https://user-images.githubusercontent.com/115526901/211405324-dd9004d1-90e6-4457-b0ab-d269a0f1cd9e.png)





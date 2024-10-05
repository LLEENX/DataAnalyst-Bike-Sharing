# Bike-Sharing-Dataset
Project pertama saya dalam menganalisis data  dari Dicoding "Belajar Analisis Data Dengan Python" . File notebook berisi hasil cleaing dan visual yang saya lakukan berdasarkan sumber data dari :  https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view

## Analysis Data dengan Jupyter Notebook
Untuk dapat running file Notebook dapat mengikuti langkah-langkah berikut ini:

1. Download seluruh file di project ini (kecuali image.png).
2. Buka file di IDE seperti VS Code atau bisa buka di Google Colaboratory
3. Install requirement
4. Install extensions jika memakai VS CODE
5. Buka file yang telah di download
6. Rubah terlebih dahulu path dan dari fata dan juga image
7. Jalankan coding tersebut

### Pertanyaan
1. Apakah faktor musim mempengaruhi peminjaman sepeda?
2. Hari apa yang paling banyak melakukan peminjaman sepeda?

### Conclution pertanyaan 1

### Apakah faktor musim mempengaruhi peminjaman sepeda?

1. Musim dengan Peminjaman Tertinggi: Musim Fall (musim gugur) memiliki total peminjaman tertinggi dengan 1,061,129 peminjam.

2. Perbandingan Musim: Summer (musim panas) juga menunjukkan angka yang tinggi dengan 918,589 peminjam, menjadikannya musim kedua dengan peminjaman tertinggi. Winter (musim dingin) dan Spring (musim semi) memiliki total peminjaman yang lebih rendah, dengan 841,613 dan 471,348 peminjam.

3. Dominasi Pengguna Registered: Di setiap musim, jumlah peminjam registered jauh lebih tinggi dibandingkan dengan peminjam casual. Misalnya, pada musim Fall, jumlah peminjam registered mencapai 835,038, sementara peminjam casual hanya 226,091.

4. Faktor Musim: Dari analisis di atas, terlihat bahwa musim sangat mempengaruhi jumlah peminjaman sepeda. Musim Fall dan Summer menunjukkan peminjaman yang signifikan, kemungkinan dipengaruhi oleh faktor cuaca yang lebih baik dan aktivitas luar ruangan yang lebih banyak.

### Conclution pertanyaan 2

###Hari apa yang paling banyak melakukan peminjaman sepeda?

1. Berdasarkan data peminjaman sepeda, kita dapat melihat menyimpulkan bahwa hari dengan Peminjaman Tertinggi adalah hari Kamis (Thu) dengan memiliki total peminjaman sejumlah 485,395 peminjam.

2. Peminjam Casual dan Registered: Pada hari Kamis, terdapat 61,460 peminjam casual dan 423,935 peminjam terdaftar. Ini menunjukkan bahwa pada hari Kamis, pengguna terdaftar jauh lebih mendominasi jumlah peminjaman dibandingkan dengan pengguna casual.

3. Pola Umum: Secara keseluruhan, peminjaman sepeda cenderung meningkat seiring berjalannya minggu, dengan hari Minggu (Sun) sebagai hari dengan peminjaman tertinggi untuk kategori casual, tetapi hari Kamis memiliki total peminjaman yang lebih tinggi karena jumlah pengguna terdaftar yang banyak.


## Dashboard with Streamlit

### Acces via webStreamlit
Anda dapat melihat Dashboard Streamlit melalui Link yang tertera di file url.txt dimana dasboard tersebut berisi mulai dari; data rides berdasarkan perjam, hari, bulan dan musim pada tahun 2011-2012.

Untuk mengecek data di tanggal yang lain anda tinggal memilih batas awal dan akhir lewat fitur calender di sidebar dimana untuk tombol pertama sebagai batas awal dan tombol kedua sebagai batas akhir dari data.

Setelah memilih data akan terganti/terbarui sesuai dengan batas awal dan akhir yang dipilih.


### Run Streamlit on Local

#### Install Dependencies

#### Aktifkan virtual environtment :
```bash
pip install streamlit babel
```

#### Install file requirement
```bash
pip install -r requirements.txt
```
#### Buka file dashboard.py
Jangan lupa untuk mengganti path data dan juga image

#### Run Dashboard
```bash
streamlit run [dasboard.py]
```

Thanks for visiting my project! ✨🔥

# H1D024046-PraktikumKB-Pertemuan10

- **Nama:** Edgina Syafa Ayu Wicaksono
- **NIM:** H1D024046
- **Shift KRS:** B
- **Shift Baru:** F

---

## Deskripsi
Program ini mengimplementasikan Algoritma Genetika (AG) sebagai pendekatan komputasi evolusioner untuk memecahkan permasalahan optimasi. Studi kasus yang digunakan adalah **Knapsack Problem**, di mana program berusaha menemukan kombinasi barang terbaik yang dapat dimuat ke dalam gudang dengan kapasitas terbatas, sekaligus memaksimalkan total keuntungan barang yang dipilih.

---

## Konsep Dasar
Algoritma Genetika bekerja dengan meniru mekanisme seleksi alam Darwin. Setiap solusi direpresentasikan sebagai **kromosom biner**, di mana nilai `1` berarti barang dipilih dan `0` berarti tidak dipilih. Populasi solusi kemudian "berevolusi" dari generasi ke generasi hingga ditemukan solusi terbaik.

---

## Struktur File
| File | Deskripsi |
|---|---|
| `inisiasipopulasi.py` | Membangkitkan populasi awal berupa kumpulan kromosom biner secara acak |
| `EvaluasiFitness.py` | Mengukur kualitas setiap solusi berdasarkan total keuntungan barang yang dipilih |
| `selection.py` | Memilih individu yang akan menjadi parent menggunakan Roulette Wheel Selection (RWS) |
| `crossover.py` | Menghasilkan individu baru dari dua parent melalui One Point Crossover |
| `mutation.py` | Menjaga keragaman populasi dengan Swap Mutation |
| `main.py` | Mengintegrasikan seluruh proses evolusi dan menampilkan hasil akhir |

---

## Cara Kerja Algoritma Genetika
1. **Inisialisasi** - Populasi awal dibangkitkan secara acak dalam bentuk kromosom biner
2. **Evaluasi Fitness** - Setiap individu dihitung nilainya berdasarkan barang yang dipilih
3. **Seleksi** - Individu dengan fitness lebih tinggi memiliki peluang lebih besar untuk terpilih
4. **Crossover** - Dua parent dikombinasikan untuk menghasilkan keturunan baru
5. **Mutasi** - Beberapa gen diubah secara acak untuk menghindari solusi yang stagnan
6. **Generasi Baru** - Populasi lama digantikan oleh hasil keturunan generasi berikutnya

---

## Penjelasan Metode

### Seleksi
- **Roulette Wheel Selection (RWS)** — Peluang terpilih sebanding dengan nilai fitness individu. Semakin tinggi fitness, semakin besar peluang untuk dipilih sebagai parent.

### Crossover
- **One Point** — Kromosom dipotong di satu titik acak lalu bagian ekornya ditukar antara dua parent untuk menghasilkan dua anak baru.

### Mutasi
- **Swap** — Dua posisi gen dipilih secara acak lalu nilainya ditukar satu sama lain.

---

## Metode Berdasarkan NIM
NIM: **H1D024046** → dua digit terakhir = **46**

| Langkah | Digit | Metode |
|---|---|---|
| Seleksi | 4 → RWS | Roulette Wheel Selection |
| Crossover | 6 → One Point | One Point Crossover |
| Mutasi | 4+6=10 → digit terakhir 0 → Swap | Swap Mutation |

---

## Parameter yang Digunakan
| Parameter | Nilai |
|---|---|
| Jumlah Generasi | 50 |
| Jumlah Populasi | 20 |
| Probabilitas Crossover | 0.5 |
| Probabilitas Mutasi | 0.1 |
| Ukuran Maksimal Gudang | 15 |

---

## Data Barang
| Barang | Keuntungan | Ukuran |
|---|---|---|
| Barang1 | 10 | 5 |
| Barang2 | 40 | 4 |
| Barang3 | 30 | 6 |
| Barang4 | 50 | 3 |
| Barang5 | 35 | 7 |

---

## Cara Menjalankan
1. Clone repositori ini
```
git clone https://github.com/edginasyafa273/H1D024046-PraktikumKB-Pertemuan10.git
```
2. Install library yang dibutuhkan
```
pip install matplotlib
```
3. Jalankan program utama
```
python main.py
```

---

## Hasil

Output program terdiri dari dua bagian:
- **Grafik** — Menampilkan perkembangan nilai fitness tertinggi, terendah, dan rata-rata dari setiap generasi
- **Terminal** — Menampilkan barang-barang yang terpilih beserta total keuntungan dan ukuran terbaik

<img width="1366" height="655" alt="pertemuan10_prak kb" src="https://github.com/user-attachments/assets/8ce3c2a1-6ca6-44ab-bf2a-b9527dbb9475" />


### Grafik Perkembangan Fitness

- 🔵 **Biru** — Nilai fitness tertinggi per generasi
- 🔴 **Merah** — Nilai fitness rata-rata per generasi
- 🟡 **Kuning** — Nilai fitness terendah per generasi
- ⚫ **Abu-abu** — Sebaran nilai fitness seluruh individu

## Output Terminal
Keuntungan Maksimal: 125
Total Ukuran: 14
Barang Terpilih:
- Barang2
- Barang4
- Barang5

> Setiap run menghasilkan output berbeda karena sifat acak AG. Ini adalah karakteristik alami algoritma evolusioner, bukan kesalahan program.

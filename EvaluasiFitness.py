# Data barang (nama, keuntungan, ukuran)
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

kapasitas_gudang = 15

def hitung_fitness(kromosom, barang, kapasitas_gudang):
    total_keuntungan = 0
    total_ukuran = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_keuntungan += barang[i][1]
            total_ukuran += barang[i][2]
    if total_ukuran > kapasitas_gudang:
        return 0
    else:
        return total_keuntungan
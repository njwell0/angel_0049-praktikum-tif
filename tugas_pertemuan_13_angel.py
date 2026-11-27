print ("\n TUGAS PERTEMUAN 13 \n")
print ("\n=================\n")

print ("--- NO 1. MENGHITUNG DENDA KETERLAMBATAN \n")
peminjamanBuku = [
    {"Nama": "Rina", "Judul": "Algoritma Dasar", "Hari_Terlambat": 2},
    {"Nama": "Bima", "Judul": "Struktur Data", "Hari_Terlambat": 0},
    {"Nama": "Rina", "Judul": "Basis Data", "Hari_Terlambat": 4},
    {"Nama": "Sari", "Judul": "Jaringan Komputer", "Hari_Terlambat": 1},
    {"Nama": "Bima", "Judul": "Pemrograman Web", "Hari_Terlambat": 3},
]
def rekap_denda(data, denda_perhari=2000):
    hasil = {}
    for item in data:
        nama = item["Nama"]
        denda = item["Hari_Terlambat"] * denda_perhari
        if nama not in hasil:
            hasil[nama] = {
                "total_buku": 0,
                "total_denda": 0,
            }
        hasil[nama]["total_buku"] += 1
        hasil[nama]["total_denda"] += denda
    return hasil
def RekapTabel(rekap):# Header tabel
    print(f"{'Nama':<10} | {'Total Buku':<12} | {'Total Denda (Rp)':<18}")
    print("-" * 46)
    for nama, data in rekap.items(): # Isi baris tabel
        totBuku = data["total_buku"]
        totDenda = f"Rp{data['total_denda']:,}".replace(",", ".") # mengubah koma di angka jadi titik
        print(f"{nama:<10} | {totBuku:<12} | {totDenda:<18}")
rekap = rekap_denda(peminjamanBuku)
RekapTabel(rekap)

print ("\n==================\n")

print ("--- NO 2. TOTAL JAM KERJA DAN UANG LEMBUR\n")
absensi = [
    {"nama": "Dina", "jam_kerja": 9},
    {"nama": "Riko", "jam_kerja": 8},
    {"nama": "Dina", "jam_kerja": 10},
    {"nama": "Santi", "jam_kerja": 7},
    {"nama": "Riko", "jam_kerja": 11},
]
def UpahLembur(data, jamNormal=8, upahPerjam=25000):
    hasil = {}
    for item in data:
        nama = item["nama"]
        jamKerja = item["jam_kerja"]
        jamLembur = max(0, jamKerja - jamNormal)
        uangLembur = jamLembur * upahPerjam
        if nama not in hasil:
            hasil[nama] = {
                "totJamKerja": 0,
                "totUangLembur": 0,
            }
        hasil[nama]["totJamKerja"] += jamKerja
        hasil[nama]["totUangLembur"] += uangLembur
    return hasil
def RekapLembur(rekap): #membuat tabel
    print(f"{'Nama':<10} | {'Total Jam Kerja':<16} | {'Total Uang Lembur (Rp)':<24}")
    print("-" * 56)
    for nama, info in rekap.items(): 
        totJam = info["totJamKerja"]
        totLembur = f"Rp{info['totUangLembur']:,}".replace(",", ".") # mengubah koma di angka jadi titik
        print(f"{nama:<10} | {totJam:<16} | {totLembur:<24}")
rekL = UpahLembur(absensi)
RekapLembur(rekL)
print ("\n")
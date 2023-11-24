"""
import sqlite3

def simpan_data_ke_sqlite(nilai1,nilai2, prodi_terpilih):
# Membuka atau membuat database SQLite
conn = sqlite3.connect("prodidb.db")
cursor = conn.cursor()
# Membuat tabel jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
nilai1 INTEGER, 
nilai2 INTEGER,
prodi_terpilih TEXT)''')
# Memasukkan data mata pelajaran ke dalam tabel
cursor.execute("INSERT INTO hasil_prediksi (mata_pelajaran, nilai, prodi_terpilih) VALUES (?, ?, ?)",
(nilai1, nilai2, prodi_terpilih))
# Melakukan commit dan menutup koneksi
conn.commit()
conn.close()
"""
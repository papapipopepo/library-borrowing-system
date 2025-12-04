import mysql.connector
import matplotlib.pyplot as plt

DENDA_PER_HARI = 2000  # denda per hari telat



# 1. KONEKSI DATABASE

def buat_koneksi():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pakkupluk",
        database="perpustakaan_capstone"
    )
    return conn



# 2. HELPER VALIDASI

def input_int(prompt):
    while True:
        nilai = input(prompt)
        try:
            return int(nilai)
        except ValueError:
            print("Input harus berupa angka, coba lagi.")


def generate_id_peminjaman(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id_peminjaman) FROM peminjaman_buku")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        return 1001
    return max_id + 1



# 3. DAFTAR BUKU (STOK)

def print_daftar_buku_list(rows):
    if not rows:
        print("\nBelum ada data buku.\n")
        return

    print("\n=== DAFTAR BUKU ===")
    header = f"{'ID':<4} {'Judul Buku':<30} {'Tahun':<7} {'Total':<7} {'Tersedia':<10} {'Dipinjam':<9}"
    print(header)
    print("-" * len(header))

    for row in rows:
        id_buku = row[0]
        judul = row[1]
        tahun = row[2]
        total = row[3]
        tersedia = row[4]
        dipinjam = row[5]

        if len(judul) > 28:
            judul_tampil = judul[:27] + "…"
        else:
            judul_tampil = judul

        print(f"{id_buku:<4} {judul_tampil:<30} {tahun:<7} {total:<7} {tersedia:<10} {dipinjam:<9}")

    print()

def show_daftar_buku(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM daftar_buku"
    cursor.execute(query)
    rows = cursor.fetchall()

    print_daftar_buku_list(rows)



# 4. READ TABEL PEMINJAMAN

def print_peminjaman_list(rows, title):
    if not rows:
        print(f"\nBelum ada data {title.lower()}.\n")
        return

    print(f"\n=== {title} ===")
    header = f"{'ID':<5} {'Nama':<12} {'Judul Buku':<30} {'Durasi':<10} {'Status':<13} {'Tahun':<7} {'Denda':<10}"
    print(header)
    print("-" * len(header))

    for row in rows:
        id_peminjaman = row[0]
        nama = row[2]
        judul = row[3]
        durasi = f"{row[4]} hari"
        status = row[5]
        tahun = row[6]
        denda = f"Rp{row[7]}"

        # Potong judul kalau terlalu panjang
        if len(judul) > 28:
            judul_tampil = judul[:27] + "…"
        else:
            judul_tampil = judul

        print(f"{id_peminjaman:<5} {nama:<12} {judul_tampil:<30} {durasi:<10} {status:<13} {tahun:<7} {denda:<10}")

    print()


def read_table(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM peminjaman_buku"
    cursor.execute(query)
    rows = cursor.fetchall()

    print_peminjaman_list(rows, "DATA PEMINJAMAN BUKU")





# 5. STATISTIK

def show_statistics(conn):
    cursor = conn.cursor()

    while True:
        print("\n=== MENU STATISTIK ===")
        print("1. Rata-rata durasi peminjaman")
        print("2. Rata-rata tahun terbit buku (berdasarkan peminjaman)")
        print("3. Jumlah peminjaman per status")
        print("4. Top 3 peminjam terbanyak")
        print("5. Top 3 buku paling sering dipinjam")
        print("6. Total dan rata-rata denda")
        print("0. Kembali")
        pilihan = input("Pilih menu statistik: ")

        if pilihan == "1":
            cursor.execute("SELECT AVG(durasi_hari) FROM peminjaman_buku")
            hasil = cursor.fetchone()[0]
            if hasil is None:
                print("Belum ada data.\n")
            else:
                print(f"Rata-rata durasi peminjaman: {hasil:.2f} hari\n")

        elif pilihan == "2":
            cursor.execute("SELECT AVG(tahun_terbit) FROM peminjaman_buku")
            hasil = cursor.fetchone()[0]
            if hasil is None:
                print("Belum ada data.\n")
            else:
                print(f"Rata-rata tahun terbit buku: {hasil:.2f}\n")

        elif pilihan == "3":
            cursor.execute("""
                SELECT status_peminjaman, COUNT(*) 
                FROM peminjaman_buku 
                GROUP BY status_peminjaman
            """)
            rows = cursor.fetchall()
            print("\nJumlah peminjaman per status:")
            for row in rows:
                print(f"- {row[0]} : {row[1]} kali")
            print()

        elif pilihan == "4":
            cursor.execute("""
                SELECT nama_peminjam, COUNT(*) AS total_pinjam
                FROM peminjaman_buku
                GROUP BY nama_peminjam
                ORDER BY total_pinjam DESC
                LIMIT 3
            """)
            rows = cursor.fetchall()
            print("\nTop 3 peminjam terbanyak:")
            for row in rows:
                print(f"- {row[0]} : {row[1]} kali meminjam")
            print()

        elif pilihan == "5":
            cursor.execute("""
                SELECT judul_buku, COUNT(*) AS total_pinjam
                FROM peminjaman_buku
                GROUP BY judul_buku
                ORDER BY total_pinjam DESC
                LIMIT 3
            """)
            rows = cursor.fetchall()
            print("\nTop 3 buku paling sering dipinjam:")
            for row in rows:
                print(f"- {row[0]} : {row[1]} kali dipinjam")
            print()

        elif pilihan == "6":
            cursor.execute("SELECT SUM(denda), AVG(denda) FROM peminjaman_buku")
            total, rata = cursor.fetchone()
            if total is None:
                total = 0
            if rata is None:
                rata = 0
            print(f"\nTotal denda terkumpul : Rp{total}")
            print(f"Rata-rata denda per peminjaman: Rp{rata:.2f}")

            cursor.execute("""
                SELECT nama_peminjam, SUM(denda) AS total_denda
                FROM peminjaman_buku
                GROUP BY nama_peminjam
                HAVING total_denda > 0
                ORDER BY total_denda DESC
            """)
            rows = cursor.fetchall()
            if rows:
                print("\nPeminjam dengan denda (dari terbesar):")
                for row in rows:
                    print(f"- {row[0]} : Rp{row[1]}")
            print()

        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak dikenal.\n")



# 6. VISUALISASI

def plot_status_peminjaman(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT status_peminjaman, COUNT(*)
        FROM peminjaman_buku
        GROUP BY status_peminjaman
    """)
    data = cursor.fetchall()

    labels = [row[0] for row in data]
    counts = [row[1] for row in data]

    if not counts:
        print("Belum ada data untuk divisualisasikan.\n")
        return

    plt.figure()
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title("Proporsi Status Peminjaman")
    plt.show()


def plot_hist_durasi(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT durasi_hari FROM peminjaman_buku")
    data = cursor.fetchall()

    durasi_list = [row[0] for row in data]

    if not durasi_list:
        print("Belum ada data durasi untuk histogram.\n")
        return

    plt.figure()
    plt.hist(durasi_list, bins=5)
    plt.title("Histogram Durasi Peminjaman")
    plt.xlabel("Durasi (hari)")
    plt.ylabel("Jumlah Peminjaman")
    plt.show()


def plot_buku_terbanyak(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT judul_buku, COUNT(*)
        FROM peminjaman_buku
        GROUP BY judul_buku
        ORDER BY COUNT(*) DESC
    """)
    data = cursor.fetchall()

    if not data:
        print("Belum ada data buku untuk bar chart.\n")
        return

    judul = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.figure()
    plt.bar(judul, counts)
    plt.title("Frekuensi Peminjaman per Judul Buku")
    plt.xlabel("Judul Buku")
    plt.ylabel("Jumlah Peminjaman")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def plot_top_peminjam(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nama_peminjam, COUNT(*) AS total_pinjam
        FROM peminjaman_buku
        GROUP BY nama_peminjam
        ORDER BY total_pinjam DESC
        LIMIT 5
    """)
    data = cursor.fetchall()

    if not data:
        print("Belum ada data peminjaman.\n")
        return

    nama = [row[0] for row in data]
    total = [row[1] for row in data]

    plt.figure()
    plt.bar(nama, total)
    plt.title("Top 5 Peminjam Terbanyak")
    plt.xlabel("Nama Peminjam")
    plt.ylabel("Jumlah Peminjaman")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def plot_denda_per_buku(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT judul_buku, SUM(denda) AS total_denda
        FROM peminjaman_buku
        GROUP BY judul_buku
        HAVING total_denda > 0
        ORDER BY total_denda DESC
    """)
    data = cursor.fetchall()

    if not data:
        print("Belum ada data denda.\n")
        return

    judul = [row[0] for row in data]
    total = [row[1] for row in data]

    plt.figure()
    plt.bar(judul, total)
    plt.title("Total Denda per Judul Buku")
    plt.xlabel("Judul Buku")
    plt.ylabel("Total Denda (Rp)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def menu_visualisasi(conn):
    while True:
        print("\n=== MENU VISUALISASI (ADMIN) ===")
        print("1. Pie chart status peminjaman")
        print("2. Histogram durasi peminjaman")
        print("3. Bar chart buku paling sering dipinjam")
        print("4. Bar chart peminjam terbanyak")
        print("5. Bar chart total denda per buku")
        print("0. Kembali")
        pilihan = input("Pilih menu visualisasi: ")

        if pilihan == "1":
            plot_status_peminjaman(conn)
        elif pilihan == "2":
            plot_hist_durasi(conn)
        elif pilihan == "3":
            plot_buku_terbanyak(conn)
        elif pilihan == "4":
            plot_top_peminjam(conn)
        elif pilihan == "5":
            plot_denda_per_buku(conn)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak dikenal.\n")



# 7. TAMBAH PEMINJAMAN (ADMIN)

def add_data(conn):
    cursor = conn.cursor()

    print("\n=== TAMBAH DATA PEMINJAMAN (ADMIN) ===")
    print("Pilih buku yang akan dipinjam:")
    show_daftar_buku(conn)

    id_buku = input_int("Masukkan ID buku: ")

    query_buku = """
        SELECT judul_buku, tahun_terbit, jumlah_tersedia 
        FROM daftar_buku 
        WHERE id_buku = %s
    """
    cursor.execute(query_buku, (id_buku,))
    row_buku = cursor.fetchone()

    if not row_buku:
        print("ID buku tidak ditemukan.\n")
        return

    judul_buku = row_buku[0]
    tahun_terbit = row_buku[1]
    jumlah_tersedia = row_buku[2]

    if jumlah_tersedia <= 0:
        print("Buku tidak tersedia (stok habis).\n")
        return

    nama = input("Nama peminjam        : ")
    durasi = input_int("Durasi (hari)        : ")

    id_peminjaman = generate_id_peminjaman(conn)
    status_awal = "Dipinjam"
    denda = 0

    query_insert = """
        INSERT INTO peminjaman_buku
        (id_peminjaman, id_buku, nama_peminjam, judul_buku, durasi_hari, status_peminjaman, tahun_terbit, denda)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (id_peminjaman, id_buku, nama, judul_buku, durasi, status_awal, tahun_terbit, denda)
    cursor.execute(query_insert, values)

    # update stok: buku dipinjam
    query_update_stok = """
        UPDATE daftar_buku
        SET jumlah_tersedia = jumlah_tersedia + (-1),
            jumlah_dipinjam = jumlah_dipinjam + 1
        WHERE id_buku = %s
    """
    cursor.execute(query_update_stok, (id_buku,))

    conn.commit()

    print(f"Data berhasil ditambahkan. ID peminjaman: {id_peminjaman}\n")



# 8. CARI PEMINJAMAN BERDASARKAN JUDUL

def search_by_title(conn):
    cursor = conn.cursor()
    print("\n=== CARI PEMINJAMAN BERDASARKAN JUDUL ===")
    keyword = input("Masukkan judul / keyword: ")

    query = "SELECT * FROM peminjaman_buku WHERE judul_buku LIKE %s"
    like_pattern = "%" + keyword + "%"
    cursor.execute(query, (like_pattern,))
    rows = cursor.fetchall()

    if not rows:
        print("Tidak ada data peminjaman dengan judul tersebut.\n")
        return

    print_peminjaman_list(rows, "HASIL PENCARIAN PEMINJAMAN")



# 9. UPDATE STATUS (ADMIN) – Dipinjam -> Dikembalikan

def update_status(conn):
    cursor = conn.cursor()
    print("\n=== UPDATE STATUS PEMINJAMAN (ADMIN) ===")
    id_peminjaman = input_int("Masukkan ID peminjaman: ")

    query = """
        SELECT status_peminjaman, id_buku 
        FROM peminjaman_buku 
        WHERE id_peminjaman = %s
    """
    cursor.execute(query, (id_peminjaman,))
    row = cursor.fetchone()

    if not row:
        print("ID peminjaman tidak ditemukan.\n")
        return

    status_lama = row[0]
    id_buku = row[1]

    if status_lama == "Dikembalikan":
        print("Peminjaman ini sudah Dikembalikan, tidak bisa diubah lagi.\n")
        return

    # status_lama = Dipinjam -> ubah ke Dikembalikan
    telat = input_int("Telat berapa hari (0 jika tepat waktu): ")
    if telat < 0:
        telat = 0
    denda = telat * DENDA_PER_HARI
    print(f"Denda yang dikenakan: Rp{denda}")

    # update stok: buku kembali
    query_stok = """
        UPDATE daftar_buku
        SET jumlah_tersedia = jumlah_tersedia + 1,
            jumlah_dipinjam = jumlah_dipinjam - 1
        WHERE id_buku = %s
    """
    cursor.execute(query_stok, (id_buku,))

    # update status + denda
    query_update = """
        UPDATE peminjaman_buku
        SET status_peminjaman = %s,
            denda = %s
        WHERE id_peminjaman = %s
    """
    cursor.execute(query_update, ("Dikembalikan", denda, id_peminjaman))
    conn.commit()

    print("Status peminjaman berhasil diupdate menjadi Dikembalikan.\n")



# 10. HAPUS DATA (ADMIN) + PERBAIKI STOK

def delete_data(conn):
    cursor = conn.cursor()
    print("\n=== HAPUS DATA PEMINJAMAN (ADMIN) ===")
    id_peminjaman = input_int("Masukkan ID peminjaman yang akan dihapus: ")

    query = """
        SELECT id_buku, status_peminjaman 
        FROM peminjaman_buku
        WHERE id_peminjaman = %s
    """
    cursor.execute(query, (id_peminjaman,))
    row = cursor.fetchone()

    if not row:
        print("ID peminjaman tidak ditemukan.\n")
        return

    id_buku = row[0]
    status = row[1]

    konfirmasi = input("Yakin ingin menghapus data ini? (y/n): ")
    if konfirmasi.lower() != "y":
        print("Hapus data dibatalkan.\n")
        return

    # Kalau masih Dipinjam, berarti stok harus dikembalikan
    if status == "Dipinjam":
        query_stok = """
            UPDATE daftar_buku
            SET jumlah_tersedia = jumlah_tersedia + 1,
                jumlah_dipinjam = jumlah_dipinjam - 1
            WHERE id_buku = %s
        """
        cursor.execute(query_stok, (id_buku,))

    query_del = "DELETE FROM peminjaman_buku WHERE id_peminjaman = %s"
    cursor.execute(query_del, (id_peminjaman,))
    conn.commit()

    print("Data peminjaman berhasil dihapus.\n")



# 11. LIHAT DENDA (PEMINJAM)

def lihat_denda(conn):
    cursor = conn.cursor()
    print("\n=== LIHAT DENDA PEMINJAMAN (PEMINJAM) ===")
    id_peminjaman = input_int("Masukkan ID peminjaman: ")

    query = """
        SELECT id_peminjaman, nama_peminjam, judul_buku, status_peminjaman, denda
        FROM peminjaman_buku
        WHERE id_peminjaman = %s
    """
    cursor.execute(query, (id_peminjaman,))
    row = cursor.fetchone()

    if not row:
        print("Data dengan ID tersebut tidak ditemukan.\n")
        return

    print("\n=== DETAIL DENDA ===")
    print(f"{'ID Peminjaman':<18}: {row[0]}")
    print(f"{'Nama Peminjam':<18}: {row[1]}")
    print(f"{'Judul Buku':<18}: {row[2]}")
    print(f"{'Status':<18}: {row[3]}")
    print(f"{'Denda':<18}: Rp{row[4]}\n")



# 12. MENU ADMIN

def admin_menu(conn):
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat semua data peminjaman")
        print("2. Tambah data peminjaman")
        print("3. Update status peminjaman (Dipinjam -> Dikembalikan)")
        print("4. Hapus data peminjaman")
        print("5. Statistik")
        print("6. Visualisasi data")
        print("7. Cari peminjaman berdasarkan judul")
        print("8. Lihat daftar buku & stok")
        print("0. Kembali ke pilih peran")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_table(conn)
        elif pilihan == "2":
            add_data(conn)
        elif pilihan == "3":
            update_status(conn)
        elif pilihan == "4":
            delete_data(conn)
        elif pilihan == "5":
            show_statistics(conn)
        elif pilihan == "6":
            menu_visualisasi(conn)
        elif pilihan == "7":
            search_by_title(conn)
        elif pilihan == "8":
            show_daftar_buku(conn)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.\n")



# 13. MENU PEMINJAM

def peminjam_menu(conn):
    while True:
        print("\n=== MENU PEMINJAM ===")
        print("1. Lihat semua data peminjaman")
        print("2. Cari peminjaman berdasarkan judul")
        print("3. Lihat denda berdasarkan ID peminjaman")
        print("4. Lihat daftar buku & stok")
        print("0. Kembali ke pilih peran")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_table(conn)
        elif pilihan == "2":
            search_by_title(conn)
        elif pilihan == "3":
            lihat_denda(conn)
        elif pilihan == "4":
            show_daftar_buku(conn)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.\n")



# 14. PILIH PERAN + MAIN

def main():
    conn = buat_koneksi()

    while True:
        print("\n=== APLIKASI PERPUSTAKAAN (PEMINJAMAN BUKU) ===")
        print("Pilih peran:")
        print("1. Admin")
        print("2. Peminjam")
        print("0. Keluar")
        pilihan = input("Pilih peran: ")

        if pilihan == "1":
            attempts = 0
            while attempts < 3:
                pw = input("Masukkan password admin: ")
                if pw == "admin":
                    print("Login admin berhasil.\n")
                    admin_menu(conn)
                    break
                else:
                    attempts += 1
                    print(f"Password salah! Percobaan {attempts}/3\n")

                if attempts == 3:
                    print("Anda salah memasukkan password sebanyak 3 kali. Program dihentikan.")
                    conn.close()
                    exit()

        elif pilihan == "2":
            peminjam_menu(conn)

        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            conn.close()
            break

        else:
            print("Pilihan tidak valid.\n")



main()

CREATE DATABASE perpustakaan_capstone;
USE perpustakaan_capstone;

CREATE TABLE daftar_buku (
    id_buku INT,
    judul_buku VARCHAR(150),
    tahun_terbit INT,
    jumlah_total INT,
    jumlah_tersedia INT,
    jumlah_dipinjam INT
);


CREATE TABLE peminjaman_buku (
    id_peminjaman INT,
    id_buku INT,
    nama_peminjam VARCHAR(100),
    judul_buku VARCHAR(150),
    durasi_hari INT,
    status_peminjaman VARCHAR(30),  -- Dipinjam / Dikembalikan
    tahun_terbit INT,
    denda INT
);


INSERT INTO daftar_buku (id_buku, judul_buku, tahun_terbit, jumlah_total, jumlah_tersedia, jumlah_dipinjam)
VALUES
(1,  'Python Dasar',                2020, 6, 3, 3),
(2,  'Belajar SQL',                 2019, 5, 3, 2),
(3,  'Data Science 101',            2021, 7, 3, 4),
(4,  'Machine Learning',            2018, 4, 3, 1),
(5,  'Algoritma dan Struktur Data', 2017, 5, 5, 0),
(6,  'Pemrograman Web',             2022, 4, 2, 2),
(7,  'Basis Data Lanjutan',         2016, 3, 2, 1),
(8,  'Jaringan Komputer',           2015, 3, 2, 1),
(9,  'Sistem Operasi',              2014, 4, 2, 2),
(10, 'Kecerdasan Buatan',           2023, 5, 2, 3);


INSERT INTO peminjaman_buku 
(id_peminjaman, id_buku, nama_peminjam, judul_buku, durasi_hari, status_peminjaman, tahun_terbit, denda)
VALUES
(1001, 1, 'Andi',  'Python Dasar',        7, 'Dipinjam',     2020, 0),
(1002, 1, 'Andi',  'Python Dasar',        7, 'Dikembalikan', 2020, 2000),
(1003, 1, 'Budi',  'Python Dasar',        5, 'Dipinjam',     2020, 0),
(1004, 1, 'Cici',  'Python Dasar',        3, 'Dipinjam',     2020, 0),
(1005, 1, 'Cici',  'Python Dasar',        3, 'Dikembalikan', 2020, 0),
(1006, 2, 'Budi',  'Belajar SQL',         3, 'Dipinjam',     2019, 0),
(1007, 2, 'Budi',  'Belajar SQL',         3, 'Dikembalikan', 2019, 0),
(1008, 2, 'Eka',   'Belajar SQL',         4, 'Dipinjam',     2019, 0),
(1009, 2, 'Fajar', 'Belajar SQL',         6, 'Dipinjam',     2019, 4000),
(1010, 3, 'Gita',  'Data Science 101',    10, 'Dipinjam',     2021, 0),
(1011, 3, 'Hani',  'Data Science 101',    8,  'Dipinjam',     2021, 0),
(1012, 3, 'Fajar', 'Data Science 101',    5,  'Dipinjam',     2021, 0),
(1013, 3, 'Fajar', 'Data Science 101',    5,  'Dikembalikan', 2021, 4000),
(1014, 3, 'Budi',  'Data Science 101',    7,  'Dipinjam',     2021, 0),
(1015, 3, 'Budi',  'Data Science 101',    7,  'Dikembalikan', 2021, 0),
(1016, 4, 'Ivan',  'Machine Learning',    7, 'Dipinjam',     2018, 0),
(1017, 4, 'Gita',  'Machine Learning',    5, 'Dipinjam',     2018, 0),
(1018, 4, 'Gita',  'Machine Learning',    5, 'Dikembalikan', 2018, 0),
(1019, 5, 'Joko',  'Algoritma dan Struktur Data', 3, 'Dipinjam',     2017, 0),
(1020, 5, 'Joko',  'Algoritma dan Struktur Data', 3, 'Dikembalikan', 2017, 2000),
(1021, 5, 'Kiki',  'Algoritma dan Struktur Data', 9, 'Dipinjam',     2017, 0),
(1022, 6, 'Lina',  'Pemrograman Web',     4, 'Dipinjam',     2022, 0),
(1023, 6, 'Lina',  'Pemrograman Web',     4, 'Dikembalikan', 2022, 0),
(1024, 6, 'Mira',  'Pemrograman Web',     6, 'Dipinjam',     2022, 0),
(1025, 7, 'Nina',  'Basis Data Lanjutan', 2, 'Dipinjam',     2016, 0),
(1026, 7, 'Omar',  'Basis Data Lanjutan', 5, 'Dipinjam',     2016, 0),
(1027, 8, 'Omar',  'Jaringan Komputer',   5, 'Dipinjam',     2015, 0),
(1028, 8, 'Omar',  'Jaringan Komputer',   5, 'Dikembalikan', 2015, 2000),
(1029, 9, 'Putra', 'Sistem Operasi',      7, 'Dipinjam',     2014, 0),
(1030, 9, 'Quinn','Sistem Operasi',       4, 'Dipinjam',     2014, 0),
(1031, 9, 'Quinn','Sistem Operasi',       4, 'Dikembalikan', 2014, 0),
(1032,10, 'Rani',  'Kecerdasan Buatan',   10, 'Dipinjam',     2023, 0),
(1033,10, 'Rani',  'Kecerdasan Buatan',   10, 'Dikembalikan', 2023, 0),
(1034,10, 'Sari',  'Kecerdasan Buatan',   6,  'Dipinjam',     2023, 0),
(1035,10, 'Sari',  'Kecerdasan Buatan',   6,  'Dikembalikan', 2023, 2000),
(1036,10, 'Andi',  'Kecerdasan Buatan',   8,  'Dipinjam',     2023, 0);

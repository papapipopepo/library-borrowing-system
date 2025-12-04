# 📚 Library Book Borrowing System  
Capstone Project — Python + MySQL

This project is a simple library management system built with **Python** and **MySQL**.  
The system supports two roles: **Admin** and **Borrower**, with features such as book borrowing, returning, automatic fines, searching, statistics, and data visualization.

---

## 🛠️ Technologies Used
- Python 3  
- MySQL  
- MySQL Connector for Python  
- matplotlib  

---

## 📂 Database Structure

### 📌 1. `daftar_buku` (Books Table)
Stores book information and stock levels.

| Column           | Type         | Description                     |
|------------------|--------------|---------------------------------|
| id_buku          | INT          | Book ID                         |
| judul_buku       | VARCHAR(150) | Book title                      |
| tahun_terbit     | INT          | Publication year                |
| jumlah_total     | INT          | Total number of books           |
| jumlah_tersedia  | INT          | Books available to borrow       |
| jumlah_dipinjam  | INT          | Books currently borrowed        |

---

### 📌 2. `peminjaman_buku` (Borrowing Table)
Stores borrowing transactions.

| Column             | Type          | Description                          |
|--------------------|---------------|--------------------------------------|
| id_peminjaman      | INT           | Transaction ID (starts at 1001)      |
| id_buku            | INT           | Book reference                        |
| nama_peminjam      | VARCHAR(100)  | Borrower's name                       |
| judul_buku         | VARCHAR(150)  | Book title                            |
| durasi_hari        | INT           | Borrowing duration                    |
| status_peminjaman  | VARCHAR(30)   | Borrowed / Returned                   |
| tahun_terbit       | INT           | Publication year                      |
| denda              | INT           | Late fine (if applicable)             |

### Notes:
- Each borrowing transaction is **ONE ROW**.  
- Returning a book updates the *same row*, instead of inserting a new one.

---

## 🔐 Admin Login

To access admin mode:
Password: admin

⚠️ If the password is wrong **3 times**, the program will automatically exit.

---

# 🎛️ Admin Features

### ✔ 1. View All Borrowing Data  
Displays all transactions in neatly formatted columns.

### ✔ 2. Add New Borrowing  
- Automatically generates a new borrowing ID.  
- Reduces book stock automatically.

### ✔ 3. Update Borrowing Status  
- Changes status from **Borrowed → Returned**  
- Automatically calculates fines  
- Restores book stock  

### ✔ 4. Delete Borrowing Data  
Deletes a transaction by ID.

### ✔ 5. Statistics  
Admin can view:
- Average borrowing duration  
- Average publication year  
- Total borrowings per status  
- Top 3 most active borrowers  
- Top 3 most borrowed books  
- Total and average fines  

### ✔ 6. Data Visualization  
Using **matplotlib**, the system generates:
- Borrowing status pie chart  
- Histogram of borrowing duration  
- Most borrowed book bar chart  
- Top borrower bar chart  
- Total fine per book bar chart  

### ✔ 7. Search Borrowing by Book Title  
Searches for transactions using keywords.

### ✔ 8. View Book List and Stock  
Displays:
- Total books  
- Books available  
- Books currently borrowed  

---

# 🧑‍🤝‍🧑 Borrower Features

Borrowers can access:

### ✔ View All Books  
Displays book list and stock.

### ✔ Search Books  
Search by title keyword.

### ✔ View Borrowing History  
Filter borrowing records by borrower's name.

### ✔ View Fine Information  
Enter borrowing ID to check fines.

---

# 📊 Data Visualization

Examples of visual charts generated:
- Borrowing status distribution  
- Duration histogram  
- Most borrowed books  
- Most active borrowers  
- Total fines per book  

These help users understand borrowing patterns easily.

---

# 🔧 Installation & Setup

### 1. Install Required Libraries
```bash
pip install mysql-connector-python
pip install matplotlib
```
### 2. Import SQL File
```pgsql
perpustakaan_capstone.sql
```
In MySQL Workbench:
1. Open SQL Script
2. Run (Execute)

### 3. Run the Program
```bash
perpustakaan.py
```
# 🧠 Important Notes
- Borrowing ID increases automatically.
- Returning a book updates the existing row only.
- Table output is formatted with fixed-width columns.
- All menu interactions include validation.

## 👨‍💻 Author

**Ezra Satria Bagas Airlangga**  
Master’s Student – Electrical Engineering, Telkom University  
📧 ezra.satria16@gmail.com
🔗[LinkedIn](https://linkedin.com/in/ezrasatriabagas/)  
#python #mysql #librarysystem #librarymanagement  
#capstoneproject #datavisualization #databaseproject
#pythonproject #Purwadhika

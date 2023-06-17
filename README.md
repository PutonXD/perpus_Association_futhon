# Sistem Peminjaman Buku di Perpustakaan
Program ini merupakan implementasi sederhana untuk sistem peminjaman buku di perpustakaan menggunakan konsep Association antara kelas Book dan LibraryMember. Program ini memungkinkan anggota perpustakaan untuk meminjam dan mengembalikan buku, serta menampilkan daftar buku yang dipinjam oleh setiap anggota.

# Kelas Book
Kelas Book merepresentasikan atribut-atribut yang dimiliki oleh sebuah buku. Setiap objek Book memiliki atribut sebagai berikut:

- title (string): judul buku.
- author (string): penulis buku.
- is_available (bool): status ketersediaan buku (True jika tersedia, False jika sedang dipinjam).
Kelas Book juga memiliki metode __str__() untuk mengembalikan judul buku dalam bentuk string.

# Kelas LibraryMember
Kelas LibraryMember merepresentasikan seorang anggota perpustakaan yang memiliki daftar buku yang dipinjam. Setiap objek LibraryMember memiliki atribut sebagai berikut:

- name (string): nama anggota perpustakaan.
- borrowed_books (list): daftar objek Book yang dipinjam oleh anggota.

Selain atribut, kelas LibraryMember juga memiliki metode sebagai berikut:
- borrow_book(book): untuk meminjam buku dengan menambahkannya ke dalam daftar buku yang dipinjam oleh anggota.
- return_book(book): untuk mengembalikan buku dengan menghapusnya dari daftar buku yang dipinjam oleh anggota.
- display_borrowed_books(): untuk menampilkan daftar buku yang dipinjam oleh anggota beserta informasi detailnya, seperti judul, penulis, dan status ketersediaan.

# Cara Menggunakan Program
Berikut adalah langkah-langkah untuk menggunakan program ini:

- Buat objek LibraryMember dengan menyediakan nama anggota perpustakaan.
- Buat objek Book dengan menyediakan judul dan penulis buku.
- Gunakan metode borrow_book() untuk meminjam buku dengan menyediakan objek Book yang ingin dipinjam.
- Gunakan metode return_book() untuk mengembalikan buku dengan menyediakan objek Book yang ingin dikembalikan.
- Panggil metode display_borrowed_books() untuk menampilkan daftar buku yang dipinjam oleh anggota.

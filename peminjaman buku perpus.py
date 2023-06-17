class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return self.title


class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} berhasil meminjam buku {book}")
        else:
            print(f"Buku {book} sedang dipinjam oleh orang lain.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} berhasil mengembalikan buku {book}")
        else:
            print(f"Buku {book} tidak ada dalam daftar peminjaman {self.name}.")

    def display_borrowed_books(self):
        print(f"Daftar buku yang dipinjam oleh {self.name}:")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(f"Judul: {book.title}")
                print(f"Penulis: {book.author}")
                print(f"Status Ketersediaan: {book.is_available}")
                print()
        else:
            print("Tidak ada buku yang dipinjam.")


# Membuat objek LibraryMember
member1 = LibraryMember("John")
member2 = LibraryMember("Jane")

# Membuat objek Book
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Peminjaman buku oleh anggota perpustakaan
member1.borrow_book(book1)
member2.borrow_book(book2)
member1.borrow_book(book2)

# Pengembalian buku oleh anggota perpustakaan
member1.return_book(book1)
member2.return_book(book3)

# Menampilkan daftar buku yang dipinjam oleh anggota perpustakaan
member1.display_borrowed_books()
member2.display_borrowed_books()

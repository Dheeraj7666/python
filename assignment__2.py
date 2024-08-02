def library():
    library = []  
    book_set = set()  
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search a book")
        print("4. List all books")
        print("5. Categorize books")
        print("6. Check for duplicates")
        print("7. Exit")
        choice = input("Enter a choice: ")
        if choice == '1':
            book_id = input("Enter book id: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            price = float(input("Enter book price: "))
            add_book(library, book_set, book_id, title, author, copies, price)
            write_book_to_file(book_id, title, author, copies, price) 
        elif choice == '2':
            book_id = input("Enter book id to delete: ")
            delete_book(library, book_set, book_id)
        elif choice == '3':
            book_id = input("Enter book id to search: ")
            search_book(library, book_id)
        elif choice == '4':
            display_library(library)
        elif choice == '5':
            categorize_books(library)
        elif choice == '6':
            check_duplicates(library)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

def add_book(library, book_set, book_id, title, author, copies, price):
    if book_id in book_set:
        print("Please enter id.")
        return
    new_book = (book_id, title, author, copies, price)
    library.append(new_book)
    book_set.add(book_id)
    print("Book added successfully.")

def delete_book(library, book_set, book_id):
    if book_id not in book_set:
        print("Book not found.")
        return
    for book in library:
        if book[0] == book_id:
            library.remove(book)
            book_set.remove(book_id)
            return

def search_book(library, book_id):
    for book in library:
        if book[0] == book_id:
            print(f"Found book: ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Copies: {book[3]}, Price: {book[4]}")
            return
    print("Book not found.")

def categorize_books(library):
    categories = {}
    for book in library:
        if book[2] not in categories:
            categories[book[2]] = []
        categories[book[2]].append(book)
    
    for author, books in categories.items():
        print(f"Author: {author}")
        for book in books:
            print(f"  ID: {book[0]}, Title: {book[1]}, Copies: {book[3]}, Price: {book[4]}")

def check_duplicates(library):
    seen_books = {}
    for book in library:
        key = (book[1], book[2])  
        if key in seen_books:
            seen_books[key].append(book)
        else:
            seen_books[key] = [book]
    
    duplicates = {key: books for key, books in seen_books.items() if len(books) > 1}
    
    if duplicates:
        print("Duplicate books found:")
        for key, books in duplicates.items():
            print(f"Title: {key[0]}, Author: {key[1]}")
            for book in books:
                print(f"  ID: {book[0]}, Copies: {book[3]}, Price: {book[4]}")
    else:
        print("No duplicate books found.")

def display_library(library):
    if not library:
        print("Library is empty.")
    else:
        print("Current library:")
        for book in library:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Copies: {book[3]}, Price: {book[4]}")

def write_book_to_file(book_id, title, author, copies, price):
    file = open('book_details.txt', 'a')
    file.write(f"Book ID: {book_id}, Title: {title}, Author: {author}, Copies: {copies}, Price: {price}\n")
    
library()

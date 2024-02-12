#Question 1: Multiplication Table

#Asking the user for the number
number = int(input("Enter the number for the multiplication table: "))

#Display the multiplication table
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}")



#Question 2
#Creating an empty dictionary to store author names and book titles
library = {}

#Creating a function to search for books or authors
def search_books_or_authors(query):
    found = False
    for author, books in library.items():
        if query.lower() == author.lower():
            print(f"Author: {author}")
            print("Books:")
            for book in books:
                print(f"- {book}")
            found = True
        else:
            for book in books:
                if query.lower() in book.lower():
                    print(f"Author: {author}")
                    print(f"Book: {book}")
                    found = True
    if not found:
        print("No such book or author in the library.")

#Creating a function to add new books or authors
def add_book_or_author(author, book):
    if author in library:
        library[author].append(book)
    else:
        library[author] = [book]

#Populating the dictionary with some initial books and authors
library["J.K. Rowling"] = ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets"]
library["George Orwell"] = ["1984", "Animal Farm"]
library["Agatha Christie"] = ["Murder on the Orient Express", "The Murder of Roger Ackroyd"]

#Main program loop
while True:
    print("\nMenu:")
    print("1. Search for books or authors")
    print("2. Add a new book or author")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        query = input("Enter the author or book title you're searching for: ")
        search_books_or_authors(query)
    elif choice == '2':
        author = input("Enter the author's name: ")
        book = input("Enter the book title: ")
        add_book_or_author(author, book)
        print("Book added successfully!")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Happy Coding!!!😎")


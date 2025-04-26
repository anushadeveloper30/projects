# 📦 Importing necessary modules
import json       # For saving and loading data in JSON format
import os         # To check if the file exists
import sys        # To make sure output shows up before exit

# 📁 File where all book records will be stored
LIBRARY_FILE = "library.json"

# 🧾 Load the book library from the file (if it exists)
def load_library():
    if os.path.exists(LIBRARY_FILE):  # Check if the file exists
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)  # Read the file and return the data
    return []  # If file doesn't exist, return empty list

# 💾 Save the current library (list of books) to the file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)  # Save data with nice formatting

# 🧾 Print a nice welcome message at the top
def print_header():
    print("╔════════════════════════════════════════════════╗")
    print("║        📚 Welcome to Personal Library!         ║")
    print("║         Manage your books like a pro! 🎯        ║")
    print("╚════════════════════════════════════════════════╝")

# 🖋 Print a goodbye/footer message at the end
def print_footer():
    print("╔════════════════════════════════════════════════╗")
    print("║ ✍ Made by: Anusha Akhter             ║")
    print("║ 🐍 Powered by Python                          ║")
    print("╚════════════════════════════════════════════════╝\n")
    sys.stdout.flush()  # Make sure this message is shown before program ends

# ➕ Function to add a new book to the library
def add_book(library):
    print("\n📘 Add a New Book")
    # Take input from user for book details
    title = input("📖 Enter Book Title: ").strip()
    author = input("✍ Enter Author Name: ").strip()
    year = input("📅 Enter Publication Year: ").strip()
    genre = input("📂 Enter Book Genre: ").strip()
    read = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"

    # Create a dictionary for the book
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)      # Add the book to the list
    save_library(library)     # Save updated list
    print(f"\n✅ '{title}' added successfully!\n")

# ❌ Remove a book by matching its title
def remove_book(library):
    print("\n🗑 Remove a Book")
    title = input("📖 Enter the title to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():  # Case-insensitive match
            library.remove(book)
            save_library(library)
            print(f"\n❌ '{title}' removed successfully!\n")
            return
    print("\n⚠ Book not found!\n")  # If no match found

# 🔍 Search for a book by title
def search_book(library):
    print("\n🔍 Search for a Book")
    title = input("📖 Enter the title to search for: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():  # Case-insensitive match
            print("\n📖 Book Found:")
            print_book(book)  # Show book details
            return
    print("\n⚠ Book not found!\n")

# 📚 List all books in the library
def list_books(library):
    if not library:
        print("\n📚 Your library is empty!\n")
        return
    print("\n📚 Your Book Collection:")
    # Show all books with numbering
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
    print()

# 🔁 Toggle (change) the read/unread status of a book
def update_read_status(library):
    print("\n🔄 Update Read Status")
    title = input("📖 Enter the book title: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():  # Match title
            book["read"] = not book["read"]  # Flip True/False
            save_library(library)
            status = "Read" if book["read"] else "Not Read"
            print(f"\n✅ '{title}' marked as {status}.\n")
            return
    print("\n⚠ Book not found!\n")

# 📊 Show some useful stats like how many books read/unread
def show_statistics(library):
    total_books = len(library)  # Total books
    read_books = sum(1 for book in library if book["read"])  # Count read books
    unread_books = total_books - read_books  # Remaining are unread

    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"✅ Books Read: {read_books}")
    print(f"❌ Books Unread: {unread_books}\n")

# 📝 Nicely display details of one book
def print_book(book):
    print(f"\n📖 Title: {book['title']}")
    print(f"✍ Author: {book['author']}")
    print(f"📅 Year: {book['year']}")
    print(f"📂 Genre: {book['genre']}")
    print(f"📘 Read: {'✅ Yes' if book['read'] else '❌ No'}\n")

# 🧭 This is the main function that shows the menu and handles user choices
def main():
    library = load_library()  # Load existing books
    print_header()            # Show welcome message

    # Keep running the menu until user exits
    while True:
        print("\n📚 Main Menu")
        print("1️⃣ Add a Book")
        print("2️⃣ Remove a Book")
        print("3️⃣ Search for a Book")
        print("4️⃣ List All Books")
        print("5️⃣ Mark Book as Read/Unread")
        print("6️⃣ Show Statistics")
        print("7️⃣ Exit")

        # Ask user to choose an option
        choice = input("\n➡ Enter your choice (1-7): ").strip()

        # Run the function based on user's choice
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            update_read_status(library)
        elif choice == "6":
            show_statistics(library)
        elif choice == "7":
            print_footer()  # Show exit message
            print("\n👋 Goodbye! Happy Reading!\n")
            break
        else:
            print("\n⚠ Invalid choice! Please enter a number from 1 to 7.\n")

# 🚀 Start the program from here
if __name__ == "__main__":
    main()
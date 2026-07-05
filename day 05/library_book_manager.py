original_list_of_books = ["Python", "Java", "C", "C++", "JavaScript", "SQL"]
books = ["Python", "Java", "C", "C++", "JavaScript", "SQL"]
books.append("Data structures")
books.insert(1,"HTML")
books.remove("C")
books.pop(5)
sort_books = sorted(books)
reverse_books = sorted(books)
reverse_books.reverse()
total_books = len(books)
print(f"============================== LIBRARY BOOK MANAGER =============================== \n Original books list: {original_list_of_books} \n Final book list: {books} \n First book: {books[0]} \n Last book: {books[-1]} \n Sorted order: {sort_books} \n Reverse order: {reverse_books} \n Total books: {total_books} \n ==============================================================")
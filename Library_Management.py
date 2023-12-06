class Library():
    def __init__(self,list):
        self.books_list = list                              # instance variables
        self.available_books_list = list[:] # to avoid list copy issue (One list but 2 reference variable)
        self.books_lent = {}  # key : books | value : username

    def display_available_books(self):
        for  book in self.available_books_list:
            print(book)

    def display_all_books(self):
        for  book in self.books_list:
            print(book)

    def lend_book(self,name,book):
        if book not in self.books_list:         # checking if entered book is available in list
            print("Incorrect book name. Please check book list")
            return
        if book in self.available_books_list:
            self.books_lent.update({book:name}) # updating dictionary | Entha book yaru eduthurukaa
            self.available_books_list.remove(book)
            print("\nYou can take the book")
        else:
            print("\nThe book is already taken by " + self.books_lent[book]) # passing key and returns name 


    def return_book(self):
        # remove from lents list
        # add to availbal list
        del self.books_lent[book]
        self.available_books_list.append(book)


if __name__ == "__main__":      # if this module runs directly then do this operations

    lib = Library(["The Life Divine","Da Vinci code","The Alchemist","Educated","Harry Potter"]) # obj creation

    print("Welcome to Library. Enter an option : ")
    while True:
        print("\n1. Display available books")
        print("\n2. Display all books")
        print("\n3. Borrow a book")
        print("\n4. Return a book")
        print("\n5. Quit\n")
        user_choice = int(input())
        if user_choice == 1:
            lib.display_available_books()
        elif user_choice == 2:
            lib.display_all_books()
        elif user_choice == 3:
            name = input("\nEnter User Name : ")
            book = input("\nEnter Book Name : ")
            lib.lend_book(name,book)
        elif user_choice == 4:
            book = input("\nEnter the name of the book you are returning")
            lib.return_book(book)
        elif user_choice == 5:
            break
        else:
            print("\nInvalid choice")




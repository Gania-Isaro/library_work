import json
import os
from datetime import datetime


class BaseModel:

    def __init__(self, file_name):

        self.file_name = file_name
        self.id = 1

        current_time = str(datetime.now())

        self.created_at = current_time
        self.updated_at = current_time

    def to_dict(self):

        return self.__dict__

    def save(self):

        filename = f"{self.file_name}.json"

        # check if file already exists
        if os.path.exists(filename):

            with open(filename, "r") as file:

                old_data = json.load(file)

                # keep old id and created_at
                self.id = old_data["id"]
                self.created_at = old_data["created_at"]

            # update time
            self.updated_at = str(datetime.now())

        # save new data
        with open(filename, "w") as file:

            json.dump(self.to_dict(), file, indent=4)

        print(filename, "saved successfully")


class User(BaseModel):

    def __init__(self, file_name, username, email):

        super().__init__(file_name)

        self.username = username
        self.email = email


class Book(BaseModel):

    def __init__(self, file_name, title, author):

        super().__init__(file_name)

        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.is_borrowed = False


# ---------------- USER CLASS ----------------

class User(Base):

    def __init__(self, file_name, name, user_id):
        super().__init__(file_name)

        self.name = name
        self.user_id = user_id

    def borrow_book(self, book):

        if not book.is_borrowed:
            book.is_borrowed = True
            book.save()
            print(f"{book.title} borrowed by {self.name}")
        else:
            print(f"{book.title} is not available")


# ---------------- OBJECTS ----------------

book1 = Book("book", "Python Basics", "John", 120, "Programming")
book2 = Book("book", "Java Basics", "Mike", 150, "Programming")
book3 = Book("book", "C++ Basics", "David", 180, "Programming")

user1 = User("user", "John", "U001")
user2 = User("user", "Jane", "U002")
user3 = User("user", "Bob", "U003")


# ---------------- SAVE DATA ----------------

book1.save()
book2.save()
book3.save()

user1.save()
user2.save()
user3.save()


# ---------------- BORROW ----------------

user1.borrow_book(book1)
user2.borrow_book(book2)
user3.borrow_book(book3)

user1.borrow_book(book2)
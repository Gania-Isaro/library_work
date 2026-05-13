import json
import os
import datetime

class Base:

    def __init__(self, file_name):
        self.file_name = file_name
        self.id = 1
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return self.__dict__

    def save(self):

        filename = f"{self.file_name}.json"

        data_list = []

        # load old data if file exists
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try:
                    data_list = json.load(f)
                except:
                    data_list = []

        # update time
        self.updated_at = datetime.datetime.now()

        # convert object to dict
        data = self.to_dict()
        data["created_at"] = str(data["created_at"])
        data["updated_at"] = str(data["updated_at"])

        # append new object
        data_list.append(data)

        # save everything back
        with open(filename, "w") as f:
            json.dump(data_list, f, indent=4)

    def load(self):

        filename = f"{self.file_name}.json"

        if os.path.exists(filename):
            with open(filename, "r") as f:
                return json.load(f)

        return []


# ---------------- BOOK CLASS ----------------

class Book(Base):

    def __init__(self, file_name, title, author, pages, genre):
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


book1.save()
book2.save()
book3.save()

user1.save()
user2.save()
user3.save()


user1.borrow_book(book1)
user2.borrow_book(book2)
user3.borrow_book(book3)

user1.borrow_book(book2)
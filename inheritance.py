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


# objects
userOne = User(
    "userOne",
    "Alice",
    "alice@gmail.com"
)

bookOne = Book(
    "bookOne",
    "Python Basics",
    "John Doe"
)

# save objects
userOne.save()
bookOne.save()
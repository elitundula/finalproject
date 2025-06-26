#Challenges With JSON Serialization Of Custom Objects
import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_json(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }

my_book = Book("1984", "George Orwell", 1949)

try:
    json_str = json.dumps(my_book)
except TypeError as e:
    print("Error:", e)

json_str = json.dumps(my_book.to_json(), indent=4)
print(json_str)

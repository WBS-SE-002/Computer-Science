

class Pet:

    '''This is a class about a pet'''

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.happiness = 5

    def __str__(self):
        return f"Hi I am {self.name}. My owner is {self.owner}. Happiness: {self.happiness}"

    def introduce(self):
        print(f"Hi am am {self.name}")

    def bark(self):
        print("Bark! Bark")

    def increase_happiness(self, amount):
        self.happiness += amount


print(Pet.__doc__)
my_pet = Pet("whiskers", owner="jane")
print(type(my_pet))
# my_second_pet = Pet("Rex", "john")

print(my_pet.name)
# print(my_second_pet.name)

print(my_pet)

my_pet.introduce()
# my_second_pet.introduce()

my_pet.bark()

while my_pet.happiness < 100:
    my_pet.increase_happiness(5)


book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)


# Create a book collection
my_collection = BookCollection()

# # Add books to the collection
my_collection.add_book(book1)
my_collection.add_book(book2)
my_collection.add_book(book3)

# # List all books
my_collection.list_books()

# # Mark a book as read
my_collection.mark_as_read("1984")

# # List books again to see updated status
my_collection.list_books()

# # Try to mark a non-existing book as read
my_collection.mark_as_read("Unknown Book")

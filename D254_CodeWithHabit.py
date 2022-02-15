# special methods
# is a way of how to use built-in functions such as print, len with my own objects
# special methods = dunder methods = magic methods

my_list = [1,2,3]
print(len(my_list))

class Sample():
    pass

my_sample = Sample()

# print(len(my_sample))
print(my_sample)


class Book():

    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages

    # creating a string represantation, that goona be called when we call a print function
    def __str__(self):
        return f"{self.name} by {self.author}, {self.pages} pages"

    # defining what will be returned when we call a len function
    def __len__(self):
        return self.pages

    # defining what will be done, when we delete the object by calling the key word "del"
    def __del__(self):
        print("The book object has been deleted.")

my_book = Book("'Python by Kamil'","Kamil Klemsa",200)

print(my_book)

print(len(my_book))

# deleting an object from memory by calling the key word "del"
del my_book



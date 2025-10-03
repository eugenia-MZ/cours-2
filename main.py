"""
-----Ex 1-----

# TODO: Create a list of your favorite fruits
fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]

# TODO: Add a new fruit to the end of the list
fruits.append("poire")

# TODO: Remove the second fruit from the list
fruits.pop(1)

# TODO: Sort the list alphabetically
fruits.sort()
# TODO: Create a new list with the first three fruits
nouvelle_liste = fruits[:3]

# Print the original list and the new list
print(f"Fruits :{fruits}")
print(f"Nouvelle_liste :{nouvelle_liste}")
"""

"""
-----Ex 2-----
# TODO: Create a tuple with your favorite colors
colors = ("rouge", "vert", "bleu")

# TODO: Try to modify one of the colors (this should raise an error)
# favorite_colors.pop(0)

# TODO: Count how many times a specific color appears in the tuple
nombre_colors = colors.count("vert")
# TODO: Find the index of a specific color
index_rouge = colors.index("bleu")
print(index_rouge)
# TODO: Create a new tuple by concatenating two existing tuples
tuple_1 = ("a1", "a2")
tuple_2 = ("b1", "b2", "b3", "b4")
merge_tuple = tuple_1 + tuple_2
# Print the results of each operation
print(f"tuple fusionné : {merge_tuple}")
"""

"""
-----Ex 3-----
# TODO: Create a dictionary representing a person (name, age, city)
person = {
    "name": "Mehdi",
    "age": 25,
    "city": "Paris"
}
# TODO: Add a new key-value pair for the person's occupation
person["occupation"] = "Designer"

# TODO: Update the person's age
person["age"] = 26

# TODO: Remove the 'city' key-value pair
del person["city"]

# TODO: Print all keys, then all values
print(person.keys())
print(person.values())
# TODO: Check if a specific key exists in the dictionary
if "age" in person:
    print("age est présent")
else:
    print("y a pas age")
# Print the final dictionary
print(f"voici le dictionnaire : {person}")
"""

"""
-----Ex 4-----
# TODO: Create two sets of numbers
numberset1 = {12, 4, 5, 69}
numberset2 = {45, 12, 36, 69.1, 152056}

# TODO: Find the union of the two sets
union_set = numberset1 | numberset2
print(f"l'union est : {union_set}")

# TODO: Find the intersection of the two sets
inter_set = numberset1 & numberset2
print(f"l'intersection est : {inter_set}")

# TODO: Find the difference between the first and second set
diff_set = numberset1 - numberset2
print(f"la différence entre le 1er set et le 2ème est : {diff_set}")

# TODO: Add a new element to one of the sets
numberset1.add(52)
print(f"nouveau set 1 : {numberset1}")
# TODO: Remove an element from one of the sets
numberset2.remove(45)
print(f"nouveau set 2 : {numberset2}")
# Print the results of each operation
"""


# TODO: Create a list of dictionaries representing books (title, author, year)
book1 = {
    "title": "le titre là",
    "author": "Mehdi l'écrivain", 
    "year": 2025
}

book2 = {
    "title": "j'ai pas d'idée de titre chef",
    "author": "Mehdi Kafka", 
    "year": 1897
}

book3 = {
    "title": "toujours pas d'inspi",
    "author": "Mehdi Kafka", 
    "year": 1989
}

books = [book1, book2, book3]

# TODO: Add a new book to the list
book4 = {
    "title": "ah je tiens peut etre un truc",
    "author": "El authoro",
    "year": 2013
} 
books.append(book4)
print(books)

# TODO: Sort the list of books by year
books.sort(key=lambda book: book["year"])
print(f"\nListe de livres triée\n : {books}")

# TODO: Create a dictionary where keys are authors and values are lists of their books
books_by_author = {}

for book in books:
    author = book["author"]
    title = book["title"]
    if author not in books_by_author:
        books_by_author[author] = []  # créer la liste si l'auteur n'existe pas
    books_by_author[author].append(title)  # ajouter le titre à la liste

print(f"\nLivres par auteur\n : {books_by_author}")

# TODO: Print all books by a specific author
for i in books:
    if i["author"] == "Mehdi Kafka":
        print("\nlivres écrits par Mehdi Kafka : ")
        print(i["title"])

# Print the final nested data structure

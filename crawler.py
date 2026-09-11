from pymongo import MongoClient

client = MongoClient('mongodb+srv://Argelznozel69cluster0.xqovrds.mongodb.net/myFirstDatabase" --apiVersion 1 --username Erlangga')

db = client.dbsparta

db.books.insert_one({
    'tittle': 'Harry Potter',
    'author' : 'J.K Rowling',
    'rating' : 90
})

db.books.insert_one({
    'tittle': 'The Fisherman and the fish',
    'author' : 'Joseph Choi',
    'rating' : 10
})

db.books.insert_one({

    'tittle': 'Fire in the water',
    'author' : 'Some Dude',
    'rating' : 57
})
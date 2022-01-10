import os
import sys
import unittest
import json
from tveesion import bookstore_solution as bookstore

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from mocks_requests import MockRequests

class TestBookStore(unittest.TestCase):
    def test_bookstore_authors(self):
        """ Implement the method authors in BookStore
        to make the test pass.
        """
        store = bookstore.BookStore()
        expected = set(["Flaubert", "Proust", "Orwell"])
        for name in store.authors():
            self.assertTrue(name in expected)
            expected.remove(name)
        self.assertEquals(len(expected), 0)


    def test_author_books(self):
        """ Implement the method sell in BookStore
        to make the test pass.
        """
        store = bookstore.BookStore()

        books = list(store.author("Orwell"))
        expected =  [("1984", 3),('La ferme des animaux', 1)]
        self.assertEquals(expected, books)


    def test_search(self):
        """ Implement the method sell in BookStore
        to make the test pass.
        """
        store = bookstore.BookStore()

        books = sorted(list(store.search("er")))
        expected =  [('La ferme des animaux', 1), ('La recherche du temps perdu', 10)]
        self.assertEquals(expected, books)

    def test_addbook(self):
        """ Implement the method addbook in BookStore
        to make the test pass.
        """
        store = bookstore.BookStore()

        self.assertFalse("Hemingway" in store.authors())

        title = "Le vieil homme et la mer"
        author = "Hemingway"
        store.addbook(author, title)

        self.assertTrue("Hemingway" in store.authors())

        for book, n in store.search("mer"):
            self.assertEquals(book, title)
            self.assertEquals(n, 1)

        store.addbook(author, title, 10)

        for book, n in store.search("mer"):
            self.assertEquals(book, title)
            self.assertEquals(n, 11)

    def test_sell(self):
        store = bookstore.BookStore()

        expected = [("1984", 3)]
        self.assertEquals(expected, list(store.search("1984")))

        store.sell("Orwell", "1984")

        expected = [("1984", 2)]
        self.assertEquals(expected, list(store.search("1984")))

        store.sell("Orwell", "1984")
        store.addbook("Orwell", "1984")

        expected = [("1984", 2)]
        self.assertEquals(expected, list(store.search("1984")))

        store.sell("Orwell", "1984")
        store.sell("Orwell", "1984")

        self.assertEquals([], list(store.search("1984")))

        with self.assertRaises(Exception) as e:
            store.sell("Orwell", "1984")

        self.assertTrue(type(e.exception) is LookupError)
        self.assertEquals("book 1984 by Orwell not found", str(e.exception))


    def test_request(self):
        """use json library to parse """
        requests = MockRequests("case1")
        res = requests.get("https://books.veesion.io/authors")
        self.assertEquals(200, res.status_code)
        self.assertEquals('["Flaubert", "Proust", "Orwell"]', res.text)
        expected = ["Flaubert", "Proust", "Orwell"]

        # Use the json library to create the expected list from request answer
        answer = expected # You should replace expected by the right python code

        self.assertEquals(expected, answer)


    def test_matching_title(self):
        """The librarian want to add to the class some utility function that will be able to tell if two book titles are the same
        
        the rules defining if two book titles are the same are in the method doctstring.
        
        You are expected to write both the code and the tests to ensure it's passing
        
        HINTS: read docstrings, read requirements

        """

        store = bookstore.BookStore()

        self.assertTrue(store.title_match("Le vieil home et la mer", "Le vieil home et la Mer"))


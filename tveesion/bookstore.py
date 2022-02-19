# coding: utf-8
import re
from unidecode import unidecode
import string

class BookStore:
    def __init__(self):
        """Inventory data is stored in a dictionnary where each key is an author name
        books for a given author are stored as a list of tuple
        each tuple contains both:
        - the name of the author as first element
        - the number of copies of this book available in stock
        """
        self.inventory = {
                "Flaubert": [("Bouvard et Pecuchet", 5)],
                "Proust": [("La recherche du temps perdu", 10)],
                "Orwell": [("1984", 3), ("La ferme des animaux", 1)]
                }

    def authors(self):
        """Return the list of authors"""
        return self.inventory.keys()
        # raise NotImplementedError()

    def author(self, name):
        """
        Return the list of books from this author in inventory
        as a list of couples (title, number)
        """
        return self.inventory.get(name, [])
        # raise NotImplementedError()

    def search(self, partialtitle):
        """
        Search if a given book is available from a partial title
        for all books matchin title returns how many books
        we have in stock and the full title.
        """
        matched_search = []
        for author in self.authors():
            for title, number in self.author(author):
                if partialtitle.lower() in title.lower():
                    matched_search.append((title, number))
        return matched_search
        # raise NotImplementedError()

    def sell(self, author, title):
        """
        Remove one book from inventory
        """
        for i, book in enumerate(self.author(author)):
            _title, _number = book
            if _title == title:
                _number -= 1
                # Remove current item form list of book beacause of tuple.
                # We may add again the item if only if the amount is
                # greater than 0
                del self.inventory[author][i]
                if _number > 0:
                    self.inventory[author].append((title, _number))
                # We break to optimize
                break
        else:
            # We raise if there is no book to remove
            raise LookupError("book %s by %s not found" % (title, author))
        # raise NotImplementedError()

    def addbook(self, author, title, number=1):
        """Add one or several identical books to inventory"""
        for i, book in enumerate(self.author(author)):
            _title, _number = book
            if _title == title:
                # The book already exist, we add only the amount
                _number += number
                # We may update the book tuple
                _book = (title, _number)
                del self.inventory[author][i]
                self.inventory[author].append(_book)
                # We break the lookup to optimize
                break
        else:
            # In case of the author doesn't exist or the book is never stored for the author
            if author in self.authors():
                # The author exists
                self.inventory[author].append((title, number))
            else:
                # It a new author
                self.inventory[author] = [(title, number)]
        # raise NotImplementedError()

    @staticmethod
    def title_match(title1, title2):
        """This function should return true if title1 and title2 are identical
        with the below allowances:
        - case is ignored
        (ie "le vieil homme et la mer" is the same as "Le Vieil Homme et la Mer")
        - multiple spaces are treated as a single space
        (ie "Le   Vieil   Homme et   la    Mer" is the same as "Le Vieil Homme et la Mer")
        - punctuation is non significant but is considered as a word separator
        (ie "2001 Odyssée de l'espace" is the same as "2001, Odyssée de l'espace")
        - Accentuated characters are treated as equivalent to the matching non accentuated characters
        (ie "2001 Odyssée de l'espace" is the same as "2001 Odyssee de l'espace")
        - the first word of the string can also be appended to the end of the string after a coma
        (ie: "Le Vieil Homme et la mer" is considered to be the same as "Vieil Homme et la Mer, Le")
        """
        # Case ignored
        _title1 = title1.lower()
        _title2 = title2.lower()
        # multiple spaces as single
        _title1 = re.sub(r"\s+", " ", _title1)
        _title2 = re.sub(r"\s+", " ", _title2)
        # ponctuation is non significant
        _title1_without_punt_list = [x for x in _title1 if x not in string.punctuation]
        _title1 = "".join(_title1_without_punt_list)
        # ****
        _title2_without_punt_list = [x for x in _title2 if x not in string.punctuation]
        _title2 = "".join(_title2_without_punt_list)
        # remove accentuated characters
        _title1 = unidecode(_title1)
        _title2 = unidecode(_title2)

        # the first word of the string appended to the end after coma.
        _title1_list = " ".split(_title1)
        _title1_ewfwc = " ".join(_title1_list[1:]+[","]+_title1_list[0:1])
        # ****
        _title2_list = " ".split(_title2)
        _title2_ewfwc = " ".join(_title2_list[1:]+[","]+_title2_list[0:1])

        return _title1 == _title2 or _title1_ewfwc == _title2 or _title1 == _title2_ewfwc
        # raise NotImplementedError()


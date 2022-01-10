import pprint
import json

class MockRequests:
    def __init__(self, case):
        self.case = case
        if case == "case1":
            self.inventory = {
                "Flaubert": [("Bouvard et Pecuchet", 5)],
                "Proust": [("La recherche du temps perdu", 10)],
                "Orwell": [("1984", 3), ("La ferme des animaux", 0)]
                }

    def get(self, url, params = None, **kwargs):
        if url == "https://books.veesion.io/authors" and not kwargs:
            class Response:
                status_code = 200
                text = json.dumps(list(self.inventory.keys()))

            return Response

        elif url == "https://books.veesion.io/authors":
             class Response:
                 status_code = 200
                 text = json.dumps(list(self.inventory.keys()))

             return Response

        else:
            raise RuntimeError(f"Route not mocked : {url} {kwargs}")

from Book import Book
from Magazine import Magazine
from DVD import Dvd

class Catalog():
    def __init__(self, catalog = None):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog in self.catalog:
            for item in catalog:
                if input_search.lower() in item.title.lower():
                    if type(item) == Book:
                        list_result.append(f"Type: {item.type}, Title: {item.title}, Authors: {item.authors}, ISBN: {item.isbn}")
                    elif type(item) == Magazine:
                        list_result.append(f"Type: {item.type}, Title: {item.title}, Volume: {item.volume}, Issue: {item.issue}")
                    elif type(item) == Dvd: 
                        list_result.append(f"Type: {item.type}, Title: {item.title}, Actors: {item.actors}, Director: {item.director}")
                    else:
                        list_result.append("No item matched your search input!")
        return list_result


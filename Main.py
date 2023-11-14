from Book import Book
from Magazine import Magazine
from DVD import Dvd
from Catalog import Catalog
from LibraryData import book_data, magazine_data, dvd_data


magazines = []
for i in range(0,len(magazine_data)):
    magazines.append(Magazine(magazine_data[i]['title'], magazine_data[i]['upc'], magazine_data[i]['subject'], magazine_data[i]['volume'], magazine_data[i]['issue']))

books = []
for i in range(0,len(book_data)):
    books.append(Book(book_data[i]['title'], book_data[i]['upc'], book_data[i]['subject'],  book_data[i]['isbn'], book_data[i]['authors'], book_data[i]['dds_number']))

dvds = []
for i in range(0,len(dvd_data)):
    dvds.append(Dvd(dvd_data[i]['title'], dvd_data[i]['upc'], dvd_data[i]['subject'],  dvd_data[i]['actors'], dvd_data[i]['directors'], dvd_data[i]['genre']))

catalog_all = [books, magazines, dvds]



item_name = input("Enter the name of the item you want to search: ")
result = Catalog(catalog_all).search(item_name)
print(result)



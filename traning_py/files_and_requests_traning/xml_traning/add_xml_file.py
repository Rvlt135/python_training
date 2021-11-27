"""Класс для создания new_library.xml"""
import xml.etree.cElementTree as ET


class Library:
    library = ET.Element("library")
    id = 0

    def __init__(self):
        self.books = []

    def created_book(self, author, price, title, desc):
        id_1 = str(Library.id)
        book = ET.SubElement(self.library, 'book', id=id_1)
        ET.SubElement(book, "author").text = author
        ET.SubElement(book, "price").text = price
        ET.SubElement(book, "title").text = title
        ET.SubElement(book, "Description").text = desc
        self.books.append([id_1, author, price, title, desc])
        Library.id += 1
        tree = ET.ElementTree(self.library)
        tree.write("new_library.xml")


book_1 = Library()
book_1.created_book("Stephen King", "200", "Shining", "desc_1")
book_1.created_book("Conan Doyle", "350", "holmes", "desc_2")

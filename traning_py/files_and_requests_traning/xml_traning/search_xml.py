import xml.etree.ElementTree as ET

file = "library.xml"


def search_element(xml_file, tag_name='genre', text="Fantasy"):
    tree = ET.parse(xml_file)
    catalog = tree.getroot()

    for book in catalog:
        for appt in list(book):
            author_text = appt.text.split()
            if appt.tag == 'author' and text in author_text:
                print(book.attrib, book.text)
            elif appt.tag == tag_name and text in author_text:
                print(book.attrib, book.text)


search_element(file)

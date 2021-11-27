import json
import requests


def get_authors():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors'
    id_author = 1
    authors = requests.get(url)
    print(authors.text)
    author_id = requests.get(f'{url}/{id_author}')
    print(author_id.text)


def add_books():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books"
    data_books = {
        "id": 15,
        "title": "string",
        "description": "string",
        "pageCount": 0,
        "excerpt": "string",
        "publishDate": "2021-08-19T18:54:55.366Z"
    }
    headers = {'Content-Type': 'application/json'}
    books = requests.post(url, data=json.dumps(data_books),
                          headers=headers)
    return print(books.json())


def add_user():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Users"
    headers = {'Content-Type': 'application/json'}
    request_body = {
        "id": 15,
        "userName": "string",
        "password": "string"
    }
    user = requests.post(url, data=json.dumps(request_body),
                         headers=headers)
    return print(user.json())


def update_book():
    num_book = 15
    url = f"https://fakerestapi.azurewebsites.net/api/v1/Books/{num_book}"
    data_books = {
        "id": 15,
        "title": "string",
        "description": "string",
        "pageCount": 0,
        "excerpt": "string",
        "publishDate": "2021-08-19T18:54:55.366Z"
    }
    headers = {'Content-Type': 'application/json'}
    books = requests.put(url, data=json.dumps(data_books),
                         headers=headers)
    return print(books.json())


def delete_user():
    id_user = 1
    url = f"https://fakerestapi.azurewebsites.net/api/v1/Users/{id_user}"
    user = requests.delete(url)
    return print(user)


delete_user()

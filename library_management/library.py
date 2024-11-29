import json
from typing import List
from models import Book


class Library:
    DATA_FILE = "data.json"

    # Инициализация библиотеки, загрузка данных из файла
    def __init__(self):
        self.books: List[Book] = []
        self.load_data()

    def load_data(self) -> None:
        try:
            with open(self.DATA_FILE, "r") as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_data(self) -> None:
        with open(self.DATA_FILE, "w") as file:
            json.dump(self.books, file, indent=4)

    # Добавляет новую книгу
    def add_book(self, title: str, author: str, year: int) -> None:
        new_book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии",
        }
        self.books.append(new_book)
        self.save_data()

    # Удаляет книгу по ID
    def delete_book(self, book_id: int) -> bool:
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                self.save_data()
                return True
        return False

    # Ищет книги по переданным критериям
    def search_books(self, **criteria: str) -> List[Book]:
        results = self.books
        for key, value in criteria.items():
            results = [book for book in results if str(book[key]).lower() == value.lower()]
        return results

    # Возвращает список всех книг
    def list_books(self) -> List[Book]:
        return self.books

    # Обновляет статус книги
    def update_status(self, book_id: int, status: str) -> bool:
        if status not in ["в наличии", "выдана"]:
            return False
        for book in self.books:
            if book["id"] == book_id:
                book["status"] = status
                self.save_data()
                return True
        return False

from library import Library


def main():
    library = Library()

    while True:
        print("\n=== Управление библиотекой ===")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название: ")
            author = input("Введите автора: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)
            print("Книга добавлена.")

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            if library.delete_book(book_id):
                print("Книга удалена.")
            else:
                print("Книга с таким ID не найдена.")

        elif choice == "3":
            print("Поиск по критерию: title, author, year.")
            key = input("Введите критерий: ")
            value = input("Введите значение: ")
            results = library.search_books(**{key: value})
            if results:
                for book in results:
                    print(book)
            else:
                print("Книги не найдены.")

        elif choice == "4":
            books = library.list_books()
            if books:
                for book in books:
                    print(book)
            else:
                print("Библиотека пуста.")

        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус (в наличии/выдана): ")
            if library.update_status(book_id, status):
                print("Статус обновлен.")
            else:
                print("Ошибка: неверный ID или статус.")

        elif choice == "6":
            print("Выход.")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()

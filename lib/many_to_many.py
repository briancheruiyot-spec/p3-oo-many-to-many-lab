class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string")
        self.name = name
        self._contracts = []  # List to hold contracts for this author
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise Exception("Title must be a non-empty string")
        self.title = title
        self._contracts = []  # List to hold contracts for this book
        Book.all.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

        # Add the contract to the author and book lists
        author._contracts.append(self)
        book._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

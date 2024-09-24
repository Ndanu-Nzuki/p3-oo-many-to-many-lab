# many_to_many.py

class Author:
    all_authors = []
    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)
    def contracts(self):
        """Return a list of contracts associated with this author."""
        return self._contracts
    def books(self):
        """Return a list of books associated with this author."""
        return [contract.book for contract in self._contracts]
    def sign_contract(self, book, date, royalties):
        """Create a contract for this author and book."""
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract # Return the created contract
    def total_royalties(self):
        """Return the total royalties from all contracts associated with this author."""
        return sum(contract.royalties for contract in self._contracts)

class Book:
    all_books = []
    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)
    def contracts(self):
        """Return a list of contracts associated with this book."""
        return self._contracts
    def authors(self):
        """Return a list of authors associated with this book."""
        return [contract.author for contract in self._contracts]

class Contract:
    all_contracts = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
        # Update contracts for the author and book
        author.contracts().append(self)
        book.contracts().append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return a list of contracts sorted by date."""
        from datetime import datetime
        def sort_by_date(contract):
            return datetime.strptime(contract.date, "%m/%d/%Y")
        return sorted(
            [contract for contract in cls.all_contracts if contract.date == date],
            key=sort_by_date
        )
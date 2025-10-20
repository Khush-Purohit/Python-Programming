class DuplicatesBookError(Exception):
    pass


books_list = [[123, " Python1"],[345, " Python2"],[456, " Python3"]]


def add_book(book_lst, book):
    for item in book_lst:
        if item[0] == book[0]:
            raise DuplicatesBookError('Book with duplicate isbn exists')
        else:
            book_lst.append(book)


bk= [ 555,'Python5']
try:
    add_book(books_list , bk)
except DuplicatesBookError as e :
    print(e)
else:
    print(books_list)



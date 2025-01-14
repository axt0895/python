from fastapi import FastAPI, HTTPException

app = FastAPI()

books = ['Statistical Learning Books', '100 Page Machine Learning Books', 'Mathematical Statistics', 'Daily Code for 100']

@app.get('/')
async def root():
    return {'message': 'Welcome to the Library'}


@app.get('/books')
async def get_books():
    return {'message': 'Here are the available books', 'Books': books}

@app.get('/books/{book_id}')
async def get_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail='Please enter the valid book id')
    else:
        return {'book': books[book_id]}
    
    
@app.delete('/books/{book_id}')
async def delete_book(book_id:int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail='Please enter the valid Book id')
    else:
        deleted_book = books.pop(book_id)
        return {'message': 'The deleted book is: ', 'Book': deleted_book}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

book = [
   {
         "id": 1,
         "title": "Либертарианский манифест",
         "author": "Родбард",
   },
   {     
         "id": 2,
         "title": "Дорога к рабоству",
         "author": "Хаек",
   },
]

@app.get(
      "/book",
      tags=["КНИГИ"], 
      summary=["Получить полный список книг"]     
)
def read_book():
      return book

@app.get(
      "/book/{id}",
      tags=["КНИГИ"],
      summary=["Получить конкретную книгу"]                
)
def get_book(id: int):
      for bok in book:
            if bok["id"] == id:
                  return bok 
      raise HTTPException(status_code=404, detail="Книга не найдена :(")

class NewBook(BaseModel):
      title: str
      author: str

@app.post(
      "/book",
      tags=["КНИГИ"]    
      )
def create_book(new_book: NewBook):
      book.append({
            "id": len(book) + 1,
            "title": new_book.title,
            "author": new_book.author  
      })
      
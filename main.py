from fastapi import FastAPI, HTTPException
from dataclasses import dataclass
import httpx
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


@dataclass
class Book:
    book_id: str
    title: str
    authors: [str]
    description: str
    image_links: {}

    def __init__(self, book_id, title, authors, description, image_links):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.description = description
        self.image_links = image_links


@dataclass
class BookSearchResponse:
    totalItems: int

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"


@app.get("/books/")
async def get_book(keywords: str, skip: int = 0, limit: int = 10):
    # query = search_string.replace(" ", "+")

    params = {
        "q": keywords,
        "startIndex": skip,
        "maxResults": limit
    }

    # params = f'intitle:${book_name}'

    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        data = response.json()

        books = []

        if "items" in data and data["items"]:
            for item in data["items"]:
                book_info = item["volumeInfo"]

                book_id = item["id"]
                title = book_info.get("title", "Unknown Title")
                authors = book_info.get("authors", ["Unknown Author"])
                description = book_info.get("description", "No description available")
                image_links = book_info.get("imageLinks", {})

                books.append(Book(book_id, title, authors, description, image_links))

            return books
        else:
            raise HTTPException(status_code=404, detail="Book not found")

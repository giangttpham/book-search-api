from fastapi import FastAPI, HTTPException
from dataclasses import dataclass
import httpx
from httpx import codes
from starlette.middleware.cors import CORSMiddleware


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
    total_items: int
    books: [Book]

    def __init__(self, total_items, books):
        self.total_items = total_items
        self.books = books


app = FastAPI()

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

# Allow CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/books/")
async def get_books(keywords: str, skip: int = 0, limit: int = 10):
    params = {
        "q": keywords,
        "startIndex": skip,
        "maxResults": limit
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)

        if response.status_code != codes.OK:
            raise HTTPException(status_code=404, detail="Book not found")

        data = response.json()
        books = []
        if "items" in data and data["items"]:
            for item in data["items"]:
                book_id = item["id"]
                book_info = item["volumeInfo"]
                title = book_info.get("title", "Unknown Title")
                authors = book_info.get("authors", ["Unknown Author"])
                description = book_info.get("description", "No description available")
                image_links = book_info.get("imageLinks", {})
                books.append(Book(book_id, title, authors, description, image_links))
            return BookSearchResponse(data["totalItems"], books)
        else:
            raise HTTPException(status_code=404, detail="Book not found")

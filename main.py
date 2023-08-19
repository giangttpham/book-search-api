from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

@app.get("/books/{book_name}")
async def get_book(book_name: str, skip: int = 0, limit: int = 10):
    params = {
        "q": f"intitle:{book_name}",
        "startIndex": skip,
        "maxResults": limit
    }

    # params = f'intitle:${book_name}'

    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        data = response.json()

        books = []

        items = data["items"]
        if "items" in data and data["items"]:
            for item in data["items"]:
                book_info = item["volumeInfo"]
                title = book_info.get("title", "Unknown Title")
                authors = book_info.get("authors", ["Unknown Author"])
                description = book_info.get("description", "No description available")

                images = book_info.get("imageLinks", [])

                books.append({"title": title,
                    "authors": authors,
                    "description": description,
                    "image_links": images})

            return books
        else:
            raise HTTPException(status_code=404, detail="Book not found")

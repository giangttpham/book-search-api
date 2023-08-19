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
async def get_book(book_name: str):
    params = {
        "q": f"title:{book_name}",
    }

    # params = f'intitle:${book_name}'

    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        data = response.json()

        if "items" in data and data["items"]:
            book_info = data["items"][0]["volumeInfo"]
            title = book_info.get("title", "Unknown Title")
            authors = book_info.get("authors", ["Unknown Author"])
            description = book_info.get("description", "No description available")

            images = book_info.get("imageLinks", [])
            return {"title": title,
                    "authors": authors,
                    "description": description,
                    "image_links": images}
        else:
            raise HTTPException(status_code=404, detail="Book not found")

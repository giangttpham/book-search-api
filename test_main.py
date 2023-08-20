import json
from unittest.mock import patch
import httpx
import pytest
from fastapi import HTTPException
import unittest
import main


class TestBookSearchApi:
    @pytest.mark.anyio
    @patch("main.httpx.AsyncClient.get")
    async def test_get_books_ok_response(self, mock_httpx_get):
        # Mock Google Books API response
        response_ojb = {
            "kind": "books#volumes",
            "totalItems": 14976,
            "items": [
                {
                    "id": "hWgfPQAACAAJ",
                    "volumeInfo": {
                        "title": "Flowers for Algernon - Teacher Guide",
                        "authors": [
                            "Anc Staff Novel Units"
                        ],
                        "description": "Activities to be used in the classroom to accompany the reading of Flowers for Algernon by Daniel Keyes.",
                        "imageLinks": {
                            "smallThumbnail": "http://books.google.com/books/content?id=hWgfPQAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
                            "thumbnail": "http://books.google.com/books/content?id=hWgfPQAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                        }
                    }
                }
            ]
        }
        mock_httpx_get.return_value = httpx.Response(200, content=json.dumps(response_ojb))

        result = await main.get_books("some keywords")
        assert result.total_items == response_ojb["totalItems"]
        assert len(result.books) == len(response_ojb["items"])
        assert result.books[0].title == response_ojb["items"][0]["volumeInfo"].get("title", "")

    @pytest.mark.anyio
    @patch("main.httpx.AsyncClient.get")
    async def test_get_books_bad_response(self, mock_httpx_get):
        mock_httpx_get.return_value = httpx.Response(400)

        with pytest.raises(HTTPException) as err:
            await main.get_books("some keywords")

        assert err.value.status_code == 404

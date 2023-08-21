## AWS EC2 instance
 - Public IPv4 address: `3.137.151.190 `
 - Port: `5000`
 - App doesn't support `https`
 - Example: 
   - URL http://3.137.151.19/books/?keywords=flowers+for+algernon&skip=11&limit=5
   - Expected response:
```json
{
  "total_items": 12742,
  "books": [
    {
      "book_id": "9ygPPQAACAAJ",
      "title": "Flores para Algernon",
      "authors": ["Daniel Keyes"],
      "description": "After a mouse gets out of a maze faster than he does, mentally handicapped Charlie Gordon volunteers for an experiment to enhance his brainpower. Soon he goes from an IQ of 68 to genius level and beyond. Only now does Charlie feel that to be mentally handicapped was to be different. And the experiment is running into trouble. This touching, must-read story is finally available in Spanish.",
      "image_links": {
        "smallThumbnail": "http://books.google.com/books/content?id=9ygPPQAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
        "thumbnail": "http://books.google.com/books/content?id=9ygPPQAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
      }
    },
    {
      "book_id": "_qpwCgAAQBAJ",
      "title": "A Study Guide for Daniel Keyes's Flowers for Algernon",
      "authors": ["Gale, Cengage Learning"],
      "description": "A Study Guide for Daniel Keyes's \"Flowers for Algernon,\" excerpted from Gale's acclaimed Novels for Students.This concise study guide includes plot summary; character analysis; author biography; study questions; historical context; suggestions for further reading; and much more. For any literature project, trust Novels for Students for all of your research needs.",
      "image_links": {
        "smallThumbnail": "http://books.google.com/books/content?id=_qpwCgAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
        "thumbnail": "http://books.google.com/books/content?id=_qpwCgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
      }
    },
    {
      "book_id": "uf1BAAAAIAAJ",
      "title": "Flowers for Algernon",
      "authors": ["David Rogers"],
      "description": "The compelling story of Charlie Gordon, willing victim of a strange experiment - a moron, a genius, a man in search of himself. Poignant, funny, tragic, but with a hope for the indomitable spirit of man, this unusual play tells a story you will long remember. It also offers a magnificent role.",
      "image_links": {
        "smallThumbnail": "http://books.google.com/books/content?id=uf1BAAAAIAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
        "thumbnail": "http://books.google.com/books/content?id=uf1BAAAAIAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
      }
    },
    {
      "book_id": "Ve5oIItoi8UC",
      "title": "Censored Books",
      "authors": ["Nicholas J. Karolides", "Lee Burress", "John M. Kean"],
      "description": "A collection of essays confronting the censorship issue, including six authors' views and defenses of individual books.",
      "image_links": {
        "smallThumbnail": "http://books.google.com/books/content?id=Ve5oIItoi8UC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
        "thumbnail": "http://books.google.com/books/content?id=Ve5oIItoi8UC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
      }
    },
    {
      "book_id": "rUPPPQAACAAJ",
      "title": "Flowers for Algernon (Pack of 16)",
      "authors": ["Daniel Keyes"],
      "description": "No description available",
      "image_links": {}
    }
  ]
}

```
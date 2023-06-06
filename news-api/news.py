from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Article(BaseModel):
    source: dict
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str


articles = [
    {
        "source": {"id": "techcrunch", "name": "TechCrunch"},
        "author": "Manish Singh",
        "title": "Byju’s sues ‘predatory’ lenders on $1.2B term loan, won’t make further payments - TechCrunch",
        "description": "Indian edtech giant Byju's has filed a complaint in the New York Supreme Court to challenge the acceleration of the $1.2 billion term loan B.",
        "url": "https://techcrunch.com/2023/06/05/byjus-files-suit-challenging-acceleration-of-1-2b-loan-seeks-to-disqualify-redwood-for-predatory-tactics/",
        "urlToImage": "https://techcrunch.com/wp-content/uploads/2023/04/GettyImages-1249691017.jpg?resize=1200,800",
        "publishedAt": "2023-06-06T06:22:30Z",
        "content": "Indian edtech giant Byju’s has filed a complaint in the New York Supreme Court to challenge the acceleration of the $1.2 billion term loan B, calling their demands for prepayment of the entire amount… [+2145 chars]",
    }
    # Add more articles as needed
]


@app.get("/api/articles")
def get_articles():
    return articles


@app.get("/api/articles/{article_id}")
def get_article(article_id: int):
    if article_id < 0 or article_id >= len(articles):
        return {"error": "Article not found"}
    return articles[article_id]


@app.post("/api/articles")
def create_article(article: Article):
    articles.append(article)
    return {"message": "Article created successfully"}


@app.put("/api/articles/{article_id}")
def update_article(article_id: int, article: Article):
    if article_id < 0 or article_id >= len(articles):
        return {"error": "Article not found"}
    articles[article_id] = article
    return {"message": "Article updated successfully"}


@app.delete("/api/articles/{article_id}")
def delete_article(article_id: int):
    if article_id < 0 or article_id >= len(articles):
        return {"error": "Article not found"}
    del articles[article_id]
    return {"message": "Article deleted successfully"}

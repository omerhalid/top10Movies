from fastapi import FastAPI

from models import Session, Movie

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/movies")
async def create_movie(title: str, release_date: str):
    session = Session()
    movie = Movie(title=title, release_date=release_date)
    session.add(movie)
    session.commit()
    return {"message": "Movie created"}

@app.get("/movies")
async def get_movies():
    session = Session()
    movies = session.query(Movie).all()
    return movies
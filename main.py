from typing import Annotated, Union

from fastapi import Body, FastAPI
from fastapi.responses import FileResponse

from lib.get_letter_dist import get_letter_dist
from lib.get_dist_plot import get_dist_plot


SCRABBLE_LETTER_COUNTS = {
    "a": 9,
    "b": 2,
    "c": 2,
    "d": 4,
    "e": 12,
    "f": 2,
    "g": 3,
    "h": 2,
    "i": 9,
    "j": 1,
    "k": 1,
    "l": 4,
    "m": 2,
    "n": 6,
    "o": 8,
    "p": 2,
    "q": 1,
    "r": 6,
    "s": 4,
    "t": 6,
    "u": 4,
    "v": 2,
    "w": 2,
    "x": 1,
    "y": 2,
    "z": 1,
}

max_count = max(SCRABBLE_LETTER_COUNTS.values())
SCRABBLE_DIST = dict(
    [letter, count / max_count] for letter, count in SCRABBLE_LETTER_COUNTS.items()
)

app = FastAPI()


@app.get("/")
def read_root():
    return FileResponse("index.html")


@app.get("/index.js")
def read_root_js():
    return FileResponse("index.js")


@app.post("/get-letter-dist")
def submit_words(words_txt: Annotated[str, Body()]):
    if words_txt == "scrabble":
        plot = get_dist_plot(SCRABBLE_DIST)
        return {
            "dist": SCRABBLE_DIST,
            "letter_counts": SCRABBLE_LETTER_COUNTS,
            "plot": plot,
        }

    words = list(filter(len, words_txt.splitlines()))

    letter_counts, dist = get_letter_dist(words)
    plot = get_dist_plot(dist)

    return {"dist": dist, "letter_counts": letter_counts, "plot": plot}


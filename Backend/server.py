from fastapi import FastAPI
from nlp import buildNlp
import main
import uvicorn

app = FastAPI()
nlp = buildNlp()

@app.get('/scrape/{path:path}')
async def scrape(path: str):
    print("test")
    print(path)
    summary = main.getReviewSummaryYelp(path, nlp)
    print(summary)
    return summary

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8001)

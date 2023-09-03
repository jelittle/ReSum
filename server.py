from bottle import *
from nlp import buildNlp
import main

nlp=buildNlp()



@route('/scrape/<path:path>')
def scrape(path):
    print("test")
    print(path)
    summary=main.getReviewSummaryYelp(path,nlp)
    print(summary)
    return summary
   
    
app = default_app()
run(app, port=8001)
from bottle import *
import main


@get('/')
def index():
    # print the request object to the console
    print(request)
    # return a simple message to the client
    return 'Hello, world!'
#if get request includes a url, scrape the url and return the reviews
@get('/scrape')
def scrape():
    url = request.query.url
    reviews = main.getReviewSummary(url)
    print(reviews)
app = default_app()
run(app, port=8001)
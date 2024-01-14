import asyncio
import json
import YelpScraper
import nlp
#todo: filter data for non english, check for bot dumps, 
async def getReviewSummaryYelp(url, model):
    reviews = await YelpScraper.getReviews(url) 
    print("getting summary")
    comments = [x['comment']['text'] for x in reviews]
    
    summary = nlp.Summary(comments, model)
    # Turn summary.summary into JSON
    print(summary.summary)
    # return json.dumps(summary.summary)
    return "test"


    
    

        
# model=nlp.buildNlp()
# getReviewSummaryYelp("https://www.yelp.com/biz/autonation-toyota-irvine-irvine-2?osq=toyota+dealership",model)
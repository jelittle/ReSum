import asyncio
import json
import YelpScraper
import nlp
#todo: filter data for non english, check for bot dumps, 
async def getReviewSummaryYelp(url, model):
    reviews = asyncio.run(YelpScraper.getReviews(url)) 
    print("getting summary")
    comments = [x['comment']['text'] async for x in reviews]
    summary = nlp.Summary(comments, model)
    # Turn summary.summary into JSON
    return json.dumps(summary.summary)

    
    

        
# model=nlp.buildNlp()
# getReviewSummaryYelp("https://www.yelp.com/biz/autonation-toyota-irvine-irvine-2?osq=toyota+dealership",model)
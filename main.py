import nlp
import json
# import getData
import YelpScraper
#todo: filter data for non english, check for bot dumps, 

def getReviewSummaryYelp(url,model):
    reviews=YelpScraper.getReviews(url)
    print("getting summary")
    comments = [x['comment']['text'] for x in reviews]
    summary = nlp.Summary(comments,model)
    #turn summary.summary into json
    return json.dumps(summary.summary)
    
    
    
    
    

        
# model=nlp.buildNlp()
# getReviewSummaryYelp("https://www.yelp.com/biz/autonation-toyota-irvine-irvine-2?osq=toyota+dealership",model)
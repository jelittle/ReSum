


from bs4 import BeautifulSoup

import httpx
import asyncio
import json

BASE_HEADERS = {
    "authority": "www.yelp.com",
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"#,
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "accept-language": "en-US;en;q=0.9",
    # "accept-encoding": "gzip, deflate, br",
    }
    
class Review():
    id: str
    userId: str
    business: dict
    user: dict
    comment: dict
    rating: int

def __getBusinessId(soup):
    # Find the meta tag with name="yelp-biz-id" and get its content attribute
    business_id = soup.find("meta", attrs={"name":"yelp-biz-id"})["content"]
    return business_id

async def __scrapeReviews(businessid: str, session: httpx.AsyncClient):
    #scrape first page
    firstPage = await session.get(
        f"https://www.yelp.com/biz/{businessid}/review_feed?rl=en&q=&sort_by=relevance_desc&start=0"
    )
    firstPageData = json.loads(firstPage.text)
    reviews=firstPageData["reviews"]
    totalReviews=firstPageData["pagination"]["totalResults"]
    print(f"scraping {totalReviews} of business {businessid}")
    toScrape = [
        session.get(
            f"https://www.yelp.com/biz/{businessid}/review_feed?rl=en&q=&sort_by=relevance_desc&start={offset}"
        )
        for offset in range(10, totalReviews + 10, 10)
    ]
    for page in asyncio.as_completed(toScrape):
        response = await page
        data = json.loads(response.text)
        reviews.extend(data["reviews"])
    return reviews
    


async def __run(businessUrl):
    # Use async with to create an asynchronous context manager
    async with httpx.AsyncClient(headers=BASE_HEADERS) as session:
        # Await the session.get coroutine and assign the result to response
        response = await session.get(businessUrl)
        # Get the text attribute of the response object
        webpage = response.text
     
        soup = BeautifulSoup(webpage, "html.parser")
        
        businessId = __getBusinessId(soup)
        reviews= await __scrapeReviews(businessId,session=session)
        return reviews




        

# Call the async function using asyncio.run()


def getReviews(businessUrl):

    ret = asyncio.run(__run(businessUrl))
    print(ret)


    
    
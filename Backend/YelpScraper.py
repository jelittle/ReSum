from bs4 import BeautifulSoup
from typing import TypedDict, List
import httpx
import asyncio
import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()
apikey = os.getenv('API_KEY')

BASE_HEADERS = {
    "Host": "127.0.0.1:65432",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "macOS",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language":" en-GB,en-US;q=0.9,en;q=0.8",
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
        return soup
        businessId = __getBusinessId(soup)
        return businessId
        # reviews= await __scrapeReviews(businessId,session=session)
        # return reviews
        
async def __runZenRows(businessUrl)-> List[Review]:
    # Use async with to create an asynchronous context manager
   
    params = {
    'url': businessUrl,
    'apikey': apikey,
}
    async with httpx.AsyncClient() as session:
        # Await the session.get coroutine and assign the result to response
        response = await session.get('https://api.zenrows.com/v1/', params=params)
        # Get the text attribute of the response object
        webpage = response.text
        

        soup = BeautifulSoup(webpage, "html.parser")
        
        businessId = __getBusinessId(soup)
   
        reviews= await __scrapeReviews(businessId,session=session)
        return reviews



# Call the async function using asyncio.run()


async def getReviews(businessUrl: str):
    print("getting reviews")
    ret = await asyncio.to_thread(__runZenRows, businessUrl)
    return ret

    

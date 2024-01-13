import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import re
import html
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import getData
#push every line of toyota_camry.txt into a string list

def buildNlp():
        nlp = spacy.load('en_core_web_sm')
        nlp.add_pipe('spacytextblob')
        return nlp



class Summary:
    def __init__(self, raw,nlp):
       
        sent=[self.__cleanText(x) for x in raw ]
        self.doc = list(nlp.pipe(sent))
        self.nouns= self.__findNouns()
        self.top5= self.__setTop5()
        self.sentiment=self.__getAvgSentiment(self.top5)
        #dictionary takes keys from top 5 and values from sentiment
        self.summary=dict(zip(self.top5.keys(),self.sentiment))
        
            
            
    def __findNouns(self):
        noun = {}
        for x in self.doc:
            for token in x:
                if token.pos_ == "NOUN":
                    #if noun non in noun dictionary, add it
                    if token.text not in noun:
                        noun[token.text] = 1
                    else:
                        noun[token.text] += 1 
        return noun
    def __setTop5(self):
        top5 = sorted(self.nouns, key=self.nouns.get, reverse=True)[:5]
        top5dict = {}
        for x in top5:
            top5dict[x] = []
            for y in self.doc:
                for token in y:
                    if token.text == x:
                        top5dict[x].append(y)
        return top5dict   
    
    def __getAvgSentiment(self,top5):
        avg=0
        sentiment=[]
        for x in top5:
            for y in top5[x]:
                avg+=y._.blob.polarity
            avg=avg/len(top5[x])
            sentiment.append(avg)
            avg=0
        return sentiment
    def __cleanText(self,text):
    # Remove HTML characters
        text = html.unescape(text)
        # Remove URLs
        text = re.sub(r'https?://\S+', '', text)
        # Remove hashtags
        text = re.sub(r'#', '', text)
        # Remove styles
        text = re.sub(r'^RT[\s]+', '', text)
        # Encode and decode the text
        text = text.encode('ascii', 'ignore').decode('UTF-8')
        # Tokenize the text
        # tokens = word_tokenize(text)
        # # Remove stopwords and punctuation
        # tokens = [word for word in tokens if word not in stopwords.words('english') and word.isalpha()]
        # # Join the tokens back to text
        # text = ' '.join(tokens)
        # Return the cleaned text
        return text
                    
                
               
    
# lst = getData.getListCamry()
# sent=lst

# nlp = buildNlp()
# summary = Summary(sent,nlp)
# for x in summary.top5:
#     print(x)


# print(summary.sentiment)

# print(summary.top5["mpg"])


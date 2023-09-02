import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

import getData
#push every line of toyota_camry.txt into a string list

def buildNlp():
        nlp = spacy.load('en_core_web_sm')
        nlp.add_pipe('spacytextblob')
        return nlp

class Summary:
    def __init__(self, sent,nlp):
        self.nlp = nlp
        self.doc = list(self.nlp.pipe(sent))
        self.nouns= self.__findNouns()
        self.top5= self.__setTop5()
        self.sentiment=self.__getAvgSentiment(self.top5)
            
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
                
                
               
    
lst = getData.getListCamry()
sent=lst

nlp = buildNlp()
summary = Summary(sent,nlp)
for x in summary.top5:
    print(x)


print(summary.sentiment)

print(summary.top5["mpg"])


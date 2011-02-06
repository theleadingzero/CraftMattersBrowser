from xlrd import open_workbook
import random
import nltk


def isWordinTokens(word, tokens):
        if word in tokens:
            return True
        else:
            return False

class craftMatters(object):
    commentsDict = {}
    def __init__(self):
        wb = open_workbook('/Users/Becky/src/chd11/Craft+Matters+E-Sign+ups+pulled+24+March+2010.xls')
        for s in wb.sheets():
            for row in range(s.nrows):
                
                values = []
                
                for col in range(s.ncols):
                    values.append(s.cell(row,col).value)
                    if len(values) == 6:
                        if len(values[3].strip())>0:
                            t = nltk.word_tokenize(values[3])
                            t = [w.lower() for w in t]
                            self.commentsDict[values[0]]={'name':values[1], 'postcode':values[2], 'comments':values[3], 'tokens':t}
        
        if unicode('Id') in self.commentsDict.keys():
            del self.commentsDict[unicode('Id')]
        return
    
    def getRandomComment(self):
        i = random.randint(0,len(self.commentsDict)-1)
        c = self.commentsDict[self.commentsDict.keys()[i]]
        return self.commentsDict.keys()[i], c['name'], c['postcode'], c['comments'], c['tokens']
    
    def getTokens(self, commenterID):
        return self.commentsDict[commenterID]['tokens']
    
    def isWordinComments(self, word):
        for k in self.commentsDict.keys():
            if isWordinTokens(word, self.getTokens(k)):
                # print self.commentsDict[k]['comments']
                return True
            else:
                return False
    
    def whichCommentsContain(self, word):
        commenterIDs = []
        for k in self.commentsDict.keys():
            if isWordinTokens(word, self.getTokens(k)):
                commenterIDs.append(k)
        return commenterIDs
        
    def getCommentThatContains(self, word):
        commenterIDs = self.whichCommentsContain(word)
        if len(commenterIDs) > 0:
            i = random.randint(0,len(commenterIDs)-1)
            c = self.commentsDict[commenterIDs[i]]
            return commenterIDs[i], c['name'], c['postcode'], c['comments'], c['tokens']
        else:
            return '','',''
    

class MakerObjects(object):
    def __init__(self):
        wb = open_workbook('/Users/Becky/src/chd11/Maker+Objects.xls')
        for s in wb.sheets():
            for row in range(s.nrows):
                
                values = []
                
                for col in range(s.ncols):
                    values.append(s.cell(row,col).value)
                    if len(values) == 6:
                        if len(values[3].strip())>0:
                            t = nltk.word_tokenize(values[3])
                            t = [w.lower() for w in t]
                            self.commentsDict[values[0]]={'name':values[1], 'postcode':values[2], 'comments':values[3], 'tokens':t}
        
        if unicode('WorkID') in self.commentsDict.keys():
            del self.commentsDict[unicode('Id')]
        return
    
    
if __name__ == '__main__': main()

    
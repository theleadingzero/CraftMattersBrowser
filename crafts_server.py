import cherrypy
import random, time
import os, signal
import xlsIO


class CraftsExplorer(object):
    @cherrypy.expose
    def index(self, word=None): 
        if (word is None) or (word == ''):
            commenterID, commenterName, postcode, commentsText, tokens = comments.getRandomComment()
        else:
            commenterID, commenterName, postcode, commentsText, tokens = comments.getCommentThatContains(unicode(word).lower())
        
        quote = ''
        for t in tokens:
            quote +="""<a href="http://localhost:8080/index?word=%(tok)s">%(tok)s</a>""" % {'tok':t}
            quote += ' '
            
        return """<html>
        <head>
        <link rel="stylesheet" type="text/css" href="/css/craftcss.css" />
        </head>
        <body>
        <title>Does Craft Matter?</title>
        <p>{0} </p>
        <p>- {1} </p>
        
        <!--<form name="nextRandom" action="http://localhost:8080/index" method="post">
        <input type="submit" value="next" />
        </form>
        <form name="search" action="http://localhost:8080/index" method="post">     
        <input type="text" name="word" />
        <input type="submit" value="next with search" />
        </form> -->
        </body>
        </html>""".format(quote, commenterName)
        

    @cherrypy.expose()
    def randomComment(self):
        commenterID, commenterName, postcode, commentsText = comments.getRandomComment()
        return commentsText

    @cherrypy.expose()
    def sleep(self, sec):
        sec = float(sec)
        time.sleep(sec)
        return str(time.ctime(time.time()))
    

# setup static data structure containing comments
comments= xlsIO.craftMatters()


current_dir = os.path.dirname(os.path.abspath(__file__))
conf = {'/':{'log.screen':True,
        'tools.sessions.on': True,
        'checker.on':False,},
        '/css': 
            {'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(current_dir, 'css')}}

cherrypy.quickstart(CraftsExplorer(), '/', config=conf)
cherrypy.engine.block()
from html.parser import HTMLParser
import os

#create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    posts_pos = 0
    def handle_starttag(self, tag, attrs):
        if(tag == 'div' and attrs[0][1] == 'posts'):
            self.posts_pos = self.getpos()




def mainLoop():
    #Open index file
    indexHTMLfile = open("index.html","r")
    #instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    #TODO : Find more about .read().
    parser.feed(indexHTMLfile.read())
    indexHTMLfile.seek(0)
    countLine = 0
    file_html = ""
    for line in indexHTMLfile:
        countLine += 1
        file_html = file_html + line
        if(countLine == parser.posts_pos[0]):
            add_blog = '<div id="post">' + input("Enter the blog :") + '</div>'
            file_html = file_html + add_blog
    indexHTMLfile.close()
    #TODO : Find a better way to do this
    os.remove("index.html")
    indexHTMLfile = open("index.html","w")
    indexHTMLfile.write(file_html)


mainLoop()

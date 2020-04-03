import xml.sax as sax
'''
SAX是一种基于事件驱动的 API。

利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器。

解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。

而事件处理器则负责对事件作出响应，对传递的XML数据进行处理。

1、对大型文件进行处理；
2、只需要文件的部分内容，或者只需从文件中得到特定信息。
3、想建立自己的对象模型的时候。
在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。
'''

#继承并重写ContentHandler
class movieHandler(sax.ContentHandler) :
    def __init__(self):
        self.currentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

     #元素开始处理
    def startElement(self, name, attrs):
        self.currentData = name
        if name == "movie":
            print("------movie-------")
            title = attrs["title"]
            print("title:", title)

    #元素结束处理
    def endElement(self, name):
        if self.currentData == "type":
            print("type:", self.type)
        elif self.currentData == "format":
            print("format:", self.format)
        elif self.currentData == "year":
            print("year:", self.year)
        elif self.currentData == "rating":
            print("rating:", self.rating)
        elif self.currentData == "stars":
            print("stars:", self.stars)
        elif self.currentData == "description":
            print("description:", self.description)

    #内容事件处理
    def characters(self, content):
        if self.currentData == "type":
           self.type = content
        elif self.currentData == "format":
            self.format = content
        elif self.currentData == "year":
            self.year = content
        elif self.currentData == "rating":
            self.rating = content
        elif self.currentData == "stars":
            self.stars = content
        elif self.currentData == "description":
            self.description = content

#创建一个xml解释器 XMLReader
parser = sax.make_parser()

#重写contextHandler方法
handler = movieHandler()
parser.setContentHandler(handler)

#在python中使用sax方式处理xml要先引入xml.sax中的parse函数
parser.parse("xmltest.xml")
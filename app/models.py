class Sources:

    '''
    source class to define Objects
    '''

    def __init__(self,id,name,description,url):
        self.id= id
        self.name = name
        self.description = description
        self.url = url

class Headlines:
    '''
    class that define instance of headlines
    '''
     def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title

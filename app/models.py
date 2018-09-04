class News:
    '''
    News class to define object news objects
    '''

    def __init__(self , id , name , url , description , language , country , category):  # news attribute
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country = country
        self.category = category






class Article:


 def __init__(self,name,description,url,title,urlToImage,publishedAt,author):
    self.name = name
    self.description = description
    self.url = url
    self.title = title
    self.urlToImage = urlToImage
    self.date = publishedAt
    self.author = author
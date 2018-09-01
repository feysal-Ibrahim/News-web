class News:
    '''
    News class to define object news objects
    '''

    def __init__(self, id, name, url, description, language, country, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country = country
        self.category = category

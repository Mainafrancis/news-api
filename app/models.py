class News_Article:
    '''
    defines news article objects
    '''

    def __init__(self,title,description,url,urlToImage,publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        

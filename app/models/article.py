class Article:
    '''
    News class to define Articles objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url =url
        self.urlToImage = urlToImage
        self.publishedAt  = publishedAt
        

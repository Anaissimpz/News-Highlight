class Config:
    '''
    General configuration parent class
    '''
     MOVIE_API_KEY ='https://newsapi.org/v2/sources?apiKey=fa11784a75904050b3ff499bf5b0ca1e'
    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
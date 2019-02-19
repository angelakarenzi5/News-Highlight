class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=65f23e20a185406a962fb29e07fbf789'
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
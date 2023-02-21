from os import environ
from Tolkien.requests.MovieRequest import MovieRequest
from Tolkien.utils import export


@export
class Client():
    '''
        Exposes objects to interact with the different endpoints
    '''
    def __init__(self, bearer_token):
        environ['BearerToken'] = environ.get('BearerToken', bearer_token)
        self.movieAPI = MovieRequest()
        # self.bookAPI = BookRequest() TBI To be implemented
        # self.charAPI = CharacterRequest() TBI To be implementeds

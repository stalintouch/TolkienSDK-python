from dataclasses import dataclass


@dataclass
class APIResponse:
    '''
        Class container for API responses
    '''
    status_code: str
    ok: bool
    text: str

    def json(self):
        '''
            returns a self representation as a dict that maches the Response object
        '''
        return self.__dict__

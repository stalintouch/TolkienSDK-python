import json
from os import path

import pytest

from Tolkien.requests.MovieRequest import MovieRequest
from Tolkien.requests.SDKRequest import SDKRequest
from Tolkien.utils import TEST_MOCK_DIR


@pytest.fixture()
def mock_movie_req():
    return MovieRequest()


@pytest.fixture()
def mock_sdk_request():
    return SDKRequest()


@pytest.fixture()
def mock_all_movies_payload():
    with open(path.join(TEST_MOCK_DIR, 'all_movies.json')) as f:
        return json.loads(f.read())


@pytest.fixture()
def mock_single_movie_payload():
    with open(path.join(TEST_MOCK_DIR, 'single_movie.json')) as f:
        return json.loads(f.read())

    
@pytest.fixture()
def mock_all_quotes():
    with open(path.join(TEST_MOCK_DIR, 'all_quotes.json')) as f:
        return json.loads(f.read())

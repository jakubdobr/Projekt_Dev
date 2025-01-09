import pytest

from main import app #importuje mi aplikacje z maina

@pytest.fixture
def client():
    app.config['TESTING'] = True #tryb testowy ktory wlacza debugowanie bledw  wkonsoli
    with app.test.client() as client:
        yield client
def test_home(client):
    respone = client.get('/') #wysyla zadanie pod moj get na "/"
    assert response.status_code == 200 #sprawdza czy kod to 200 czy np 500
    assert response.data == b'Hello World!' #sprawdza tresc odpowiedzi - u mnie to jest hello world

def test_hello(client):
    response = client.get('/hello/John') #wysyla zadanie GET na /hello/John
    assert response.status_code == 200 #znowu czy kod odpowiedzi to 2000
    assert response.data == b'Hello John' #sprawdza tresc odpowiedzi
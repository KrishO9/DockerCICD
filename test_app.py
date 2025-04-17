from app import app

#pytest library finds out the testing files
# By indentifying files and functions starting with test

def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data==b"Hello World!"


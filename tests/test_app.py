from app import app

def test_home():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200
    assert b"Hello" in r.data

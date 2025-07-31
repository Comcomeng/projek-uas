from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Daftar Tugas" in response.data

def test_add_page():
    client = app.test_client()
    response = client.get('/add')
    assert response.status_code == 200
    assert b"Tambah Tugas" in response.data

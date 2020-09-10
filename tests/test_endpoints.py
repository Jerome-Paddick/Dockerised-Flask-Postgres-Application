import requests

def test_gifts_get():
    response = requests.get('http://localhost:5000/api/gifts')
    assert response.status_code == 200

def test_gifts_post():
    response = requests.post('http://localhost:5000/api/gifts', json={'product_id': 1})
    assert response.status_code == 200

def test_gift_report():
    response = requests.get('http://localhost:5000/api/gift-report')
    assert response.status_code == 200
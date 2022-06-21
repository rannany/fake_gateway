from main import checkout

def test_payment():
    payment_status = checkout(200)
    assert payment_status == 'paid'

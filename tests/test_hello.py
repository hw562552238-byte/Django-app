from django_app.hello import hello

def test_hello(capsys):
    hello()
    assert "Hello from django_app!" in capsys.readouterr().out

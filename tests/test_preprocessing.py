from src.preprocessing import clean_text


def test_clean_text():

    text = "Hello!!! WORLD 123"

    cleaned = clean_text(text)

    assert cleaned == "hello world 123"
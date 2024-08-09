from watch import parse

def main():
    test_valid_input()
    test_invalid_input()

def test_valid_input():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/lK_ydZ7JiBk"></iframe>') == "https://youtu.be/lK_ydZ7JiBk"

def test_invalid_input():
    assert parse('<iframe src="https://cs50.harvard.edu/python"></iframe>') == None
    assert parse('<iframe width="560" height="315" src="https://vimeo.com/123456"></iframe>') == None

if __name__ == "__main__":
    main()

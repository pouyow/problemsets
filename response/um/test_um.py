from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_multiple_ums():
    assert count("um um um") == 3
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_no_um():
    assert count("hello world") == 0
    assert count("yum, yummy, aluminium") == 0
    assert count("umbrella") == 0

from example2 import cube


def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(10) == 1000


def test_cube_negative():
    assert cube(-1) == -1
    assert cube(-3) == -27


def test_cube_bad_test():
    assert cube("three") == "twenty-seven"

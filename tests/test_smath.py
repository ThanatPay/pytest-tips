from smath import subtract

def setup_function(function):
    print(f"Running Setup: {function.__name__}")
    function.x = 10

def teardown_function(function):
    print(f"Run Teardown: {function.__name__}")
    del function.x

# def test_add():
#     assert subtract(test_subtract.x) == 11

def test_subtract():
    assert subtract(test_subtract.x) == 9
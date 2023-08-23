import pytest

@pytest.fixture()
def set_up():
    print("Star test")
    yield
    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("enter system")
    yield
    print("exit  system ")

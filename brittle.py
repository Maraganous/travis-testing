import datetime

def is_curr_year(year):
    return datetime.datetime.today().year == year

def test_is_curr_year():
    assert is_curr_year(2016) == True
    assert is_curr_year(2015) == False



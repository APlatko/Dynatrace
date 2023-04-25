import request_function


# For function check_currency:

def test_check_currency():
    assert request_function.check_currency('USD') is True
    assert request_function.check_currency('AAA') is False
    assert request_function.check_currency('eur') is True
    assert request_function.check_currency('') is False


# For function check_date:

def test_check_date():
    assert request_function.check_date('2023-04-25') is True
    assert request_function.check_date('2023-04-32') is False
    assert request_function.check_date('2023-13-01') is False
    assert request_function.check_date('') is False


# For function check_period:

def test_check_period():
    assert request_function.check_period('5') is True
    assert request_function.check_period('1000') is False
    assert request_function.check_period('-2') is False
    assert request_function.check_period('abc') is False


# For function get_avg_rate:

def test_get_avg_rate():
    assert request_function.get_avg_rate('USD', '2023-04-22') == -3
    assert request_function.get_avg_rate('USD', '2023-04-25') == 4.1649
    assert request_function.get_avg_rate('AAA', '2023-04-25') == -1
    assert request_function.get_avg_rate('USD', '2023-04-32') == -2


# For function get_max_min_avg_value:

def test_get_max_min_avg_value():
    assert request_function.get_max_min_avg_value('USD', '5') == (4.2244, 4.1649)
    assert request_function.get_max_min_avg_value('EUR', '20') == (4.6902, 4.598)
    assert request_function.get_max_min_avg_value('AAA', '10') == -1
    assert request_function.get_max_min_avg_value('USD', '1000') == -2


# For function get_max_diff_buy_and_ask:
def test_get_max_diff_buy_and_ask():
    assert request_function.get_max_diff_buy_and_ask('GBP', '5') == 0.1048
    assert request_function.get_max_diff_buy_and_ask('KRW', '20') == -3
    assert request_function.get_max_diff_buy_and_ask('AAA', '10') == -1
    assert request_function.get_max_diff_buy_and_ask('USD', '1000') == -2

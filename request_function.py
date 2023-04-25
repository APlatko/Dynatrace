import requests
from datetime import datetime

available_currencies = (
    'AUD', 'THB', 'BRL', 'BGN', 'CAD', 'CLP', 'CZK', 'DKK', 'EUR', 'HUF', 'HKD', 'UAH', 'ISK', 'INR', 'MYR', 'MXN',
    'ILS', 'NZD', 'NOK', 'PHP', 'GBP', 'ZAR', 'RON', 'SGD', 'SEK', 'CHF', 'TRY', 'USD', 'KRW', 'JPY', 'CNY', 'XDR')


def check_currency(currency: str) -> bool:
    """Check if entered currency is in 'available_currencies' list."""
    if currency.upper() not in available_currencies:
        return False
    return True


def check_date(date: str) -> bool:
    """Check if entered date is correct and satisfy format YYYY-MM-DD"""
    try:
        datetime.fromisoformat(date)
    except ValueError as ex:
        print(ex)
        return False
    return True


def check_period(number: str) -> bool:
    """Check if entered period satisfy the condition and number is integer"""
    try:
        if 1 <= int(number) <= 255:
            return True
    except ValueError as ex:
        print(ex)
        return False
    else:
        return False


def get_avg_rate(currency_code: str, date: str) -> int | float:
    """Provide average exchange rate for entered currency and date. Source: https://nbp.pl."""
    if check_currency(currency_code) is False:
        return -1
    if check_date(date) is False:
        return -2
    rates = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{date}/')
    if rates.status_code != 200:
        return -3
    return rates.json()['rates'][0]['mid']


def get_max_min_avg_value(currency_code: str, period: str) -> int | tuple:
    """Provide the max and min average value of entered currency exchange rate and period. Source: https://nbp.pl."""
    if check_currency(currency_code) is False:
        return -1
    if check_period(period) is False:
        return -2
    rates = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/last/{period}/')
    rate_list = [i['mid'] for i in rates.json()['rates']]
    return max(rate_list), min(rate_list)


def get_max_diff_buy_and_ask(currency_code: str, period: str) -> int | float:
    """
    Provide the major difference between the buy and ask rate of entered currency and period.
    Source: https://nbp.pl.
    """
    if check_currency(currency_code) is False:
        return -1
    if check_period(period) is False:
        return -2
    rates = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/{currency_code}/last/{period}/')
    if rates.status_code != 200:
        return -3
    differences = [int((i['ask'] * 10000) - (i['bid'] * 10000)) for i in rates.json()['rates']]
    return max(differences) / 10000

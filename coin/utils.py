# -*- coding: utf-8 -*-

# Utils

__author__ = "nil.gradisnik@gmail.com"

currency = {
    'usd': '$',
    'eur': '€',
    'btc': '฿',
    'gbp': '£'
}

category = {
    'bid': 'Bid:\t\t',
    'high': 'High:\t\t',
    'low': 'Low:\t\t',
    'ask': 'Ask:\t\t',
    'volume': 'Volume:\t',
    'first': 'First:\t\t'
}


def decimal_round(number):
    return "%.2f" % float(number)

def decimal_precision(number):
    return "%.5f" % float(number)

def decimal_auto(number):
    if(number < 1):
        return decimal_precision(number)
    else:
        return decimal_round(number)

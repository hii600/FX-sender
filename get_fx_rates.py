# -*- coding: utf-8 -*-
import os 
import sys
import numpy as np
import urllib2
from bs4 import BeautifulSoup
import requests
import datetime

"""
Get FX rates by scraping
On 24 Aug, 2018
By Hiroaki Ikeuchi
"""

def print_source(url):
    print "Source: {}".format(url)

def add_fxValues(fx):
    list_out.append(float(get_css_text("#{}JPY_chart_bid".format(fx))))
    list_out.append(float(get_css_text("#{}JPY_chart_ask".format(fx))))

def get_css_text(arg):
    return soup.select_one(arg).getText()

def calc_change(fx, ba_flt, ba_str):
    if bool_yestday:
        return " (%+.3f)" % (ba_flt - dict_yestday[fx+ba_str])

def print_fx(fx):
    print get_css_text(".ico{}Jpy{}".format(fx.capitalize(), yr)).encode("utf-8")
    bid = float(get_css_text("#{}JPY_chart_bid".format(fx)))
    ask = float(get_css_text("#{}JPY_chart_ask".format(fx)))
    print "bid: %.3f" % bid, calc_change(fx, bid, "bid") 
    print "ask: %.3f" % ask, calc_change(fx, ask, "ask")
    print

def get_dict_yestday():
    dict_yestday = {}
    if bool_yestday:
        with open(fn_yestday, "r") as f:
            for fx in fx_list:
                for ba in "bid ask".split():
                    dict_yestday[fx+ba] = float(f.readline())
    return dict_yestday

def get_ctime():
    ctime = datetime.datetime.now() 
    print ctime.strftime("%Y/%m/%d %H:%M時点"), u"(前日比)".encode("utf-8")
    print 
    return ctime

# Current time
ctime = get_ctime()
yr = ctime.strftime("%y")
# FX list
fx_list = "GBP EUR USD AUD".split()
# read yesterday's rates
fn_yestday = "../data/{}.txt".format((ctime - datetime.timedelta(days=1)).strftime("%Y%m%d"))
bool_yestday = os.path.exists(fn_yestday)
dict_yestday = get_dict_yestday()
# output list
fn_out = "../data/{}.txt".format(ctime.strftime("%Y%m%d"))
list_out = []
# BeautifulSoup
url = "https://info.finance.yahoo.co.jp/fx/list/"
instance = urllib2.urlopen(url)
soup = BeautifulSoup(instance, "html.parser")
# main
for fx in fx_list:
    print_fx(fx)
    add_fxValues(fx)
# print source
print_source(url)
# save output
np.savetxt(fn_out, list_out, fmt="%e")

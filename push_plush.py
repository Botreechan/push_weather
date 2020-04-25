# encoding: utf-8
# - * - coding: utf - 8 - *

import time

import requests
import weather


class Today:
    @staticmethod
    def minhang():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<闵行区 " \
              "今日天气预报>>←&content=" + weather.today_weather("shanghai_minhang") + "&topic=weather_shanghai"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)

    @staticmethod
    def xuhui():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<徐汇区 " \
              "今日天气预报>>←&content=" + weather.today_weather("shanghai_xuhui") + "&topic=weather_shanghai"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)

    @staticmethod
    def hongkou():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<虹口区 " \
              "今日天气预报>>←&content=" + weather.today_weather("shanghai_hongkou") + "&topic=weather_shanghai"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)

    @staticmethod
    def shangnan():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<商南县 " \
              "今日天气预报>>←&content=" + weather.today_weather("shangnan") + "&topic=weather_shangnan"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)


class Tomorrow:
    @staticmethod
    def minhang():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<闵行区 " \
              "明日天气预报>>←&content=" + weather.today_weather("shanghai_minhang") + "&topic=weather_shanghai"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)

    @staticmethod
    def xuhui():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<徐汇区 " \
              "明日天气预报>>←&content=" + weather.today_weather("shanghai_xuhui") + "&topic=weather_shanghai"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)

    @staticmethod
    def hongkou():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<虹口区 " \
              "明日天气预报>>←&content=" + weather.today_weather("shanghai_hongkou") + "&topic=weather_shanghai"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)

    @staticmethod
    def shangnan():
        url = "http://pushplus.hxtrip.com/customer/push/send?token=30dedc771dce4f5282464ba37c9c6a6c&title=→<<商南县 " \
              "明日天气预报>>←&content=" + weather.today_weather("shangnan") + "&topic=weather_shangnan"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)


while True:
    now_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    # print(now_time)

    if now_time == "22:00:00":
        print("开始")
        Tomorrow.minhang()
        Tomorrow.xuhui()
        Tomorrow.hongkou()
        Tomorrow.shangnan()
    elif now_time == "07:10:00":
        Today.minhang()
        Today.xuhui()
        Today.hongkou()
        Today.shangnan()
# Today.shangnan()
# Tomorrow.shangnan()

# shangnan()
# xuhui()
# hongkou()
# minhang()

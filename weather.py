import requests
import time
base_url = "http://t.weather.sojson.com/api/weather/city/"

shanghai = {
    "shanghai": "101020100",
    "shanghai_minhang": "101020200",
    "shanghai_xuhui": "101021200",
    "shanghai_hongkou": "101021600"
}
shaanxi = {
    "shangluo": "101110601",
    "shangnan": "101110607"
}


def future_weather(city_name):
    if city_name == "shanghai_minhang":
        data = requests.get(base_url + shanghai["shanghai_minhang"]).json()
    elif city_name == "shanghai_xuhui":
        data = requests.get(base_url + shanghai["shanghai_xuhui"]).json()
    elif city_name == "shanghai_hongkou":
        data = requests.get(base_url + shanghai["shanghai_xuhui"]).json()
    elif city_name == "shangnan":
        data = requests.get(base_url + shaanxi["shangnan"]).json()

    for i in range(1, len(data["data"]["forecast"])):
        # print(i)
        city = data["cityInfo"]["city"]
        today_date = data["data"]["forecast"][i]["ymd"]
        low = data["data"]["forecast"][i]["low"]
        low1 = str(low).replace("温 ", "温度：")
        high = data["data"]["forecast"][i]["high"]
        high1 = str(high).replace("温 ", "温度：")
        week = data["data"]["forecast"][i]["week"]
        try:
            aqi = data["data"]["forecast"][i]["aqi"]
        except KeyError:
            aqi = "无"
        weather_type = data["data"]["forecast"][i]["type"]
        wind = data["data"]["forecast"][i]["fx"] + data["data"]["forecast"][i]["fl"]
        notice = data["data"]["forecast"][i]["notice"]
        weather_detail = '''
        <div style="font-size:18px;" class="">
        <hr />
       <li class="">
            预报时间：''' + week + " " + today_date + '''
        </li>
        <li class="">
            天气情况：''' + weather_type + '''
        </li>
        <li class="">
            空气质量： ''' + str(aqi) + '''
        </li>
        <li class="">
            最''' + low1 + '''
        </li>
        <li class="">
            最''' + high1 + '''
        </li>
        <li class="">
            风力情况：''' + wind + '''
        </li>
        <li class="">
            温馨提示：''' + notice + '''
        </li>
        <hr />
        </div>
        '''
        weather_detail_old = "\n-→<<" + city + "天气预报>>←-   " + week + " " + today_date + "\n" + "天气情况：" + weather_type + "\n空气质量：" + str(
            aqi) + "\n最" + low1 + "\n最" + high1 + "\n风力情况：" + wind + "\n温馨提示：" + notice + "\n"
        with open(data["data"]["forecast"][0]["ymd"]+"future_log.txt", "a+") as f:
            f.write(weather_detail_old)
    return weather_detail
    # print(weather_detail)


def today_weather(city_name):
    if city_name == "shanghai_minhang":
        data = requests.get(base_url + shanghai["shanghai_minhang"]).json()
    elif city_name == "shanghai_xuhui":
        data = requests.get(base_url + shanghai["shanghai_xuhui"]).json()
    elif city_name == "shanghai_hongkou":
        data = requests.get(base_url + shanghai["shanghai_xuhui"]).json()
    elif city_name == "shangnan":
        data = requests.get(base_url + shaanxi["shangnan"]).json()

    for i in range(1):
        # print(i)
        city = data["cityInfo"]["city"]
        today_date = data["data"]["forecast"][i]["ymd"]
        low = data["data"]["forecast"][i]["low"]
        low1 = str(low).replace("温 ", "温度：")
        high = data["data"]["forecast"][i]["high"]
        high1 = str(high).replace("温 ", "温度：")
        week = data["data"]["forecast"][i]["week"]
        try:
            aqi = data["data"]["forecast"][i]["aqi"]
        except KeyError:
            aqi = "无"
        weather_type = data["data"]["forecast"][i]["type"]
        wind = data["data"]["forecast"][i]["fx"] + data["data"]["forecast"][i]["fl"]
        notice = data["data"]["forecast"][i]["notice"]
        weather_detail = '''
        <div style="font-size:16px;" class="">
        <hr />
       <li class="">
            预报时间：''' + week + " " + today_date + '''
        </li>
        <li class="">
            天气情况：''' + weather_type + '''
        </li>
        <li class="">
            空气质量： ''' + str(aqi) + '''
        </li>
        <li class="">
            最''' + low1 + '''
        </li>
        <li class="">
            最''' + high1 + '''
        </li>
        <li class="">
            风力情况：''' + wind + '''
        </li>
        <li class="">
            温馨提示：''' + notice + '''
        </li>
        <hr />
        </div>
        '''
        print(weather_detail)
        weather_detail_old = "\n-→<<" + city + "天气预报>>←-   " + week + " " + today_date + "\n" + "天气情况：" + weather_type + "\n空气质量：" + str(
            aqi) + "\n最" + low1 + "\n最" + high1 + "\n风力情况：" + wind + "\n温馨提示：" + notice + "\n"
        with open(data["data"]["forecast"][0]["ymd"]+"_today_log.txt", "a+") as f:
            f.write(weather_detail)
        print(weather_detail_old)
    return weather_detail


def tomorrow_weather(city_name):
    if city_name == "shanghai_minhang":
        data = requests.get(base_url + shanghai["shanghai_minhang"]).json()
    elif city_name == "shanghai_xuhui":
        data = requests.get(base_url + shanghai["shanghai_xuhui"]).json()
    elif city_name == "shanghai_hongkou":
        data = requests.get(base_url + shanghai["shanghai_xuhui"]).json()
    elif city_name == "shangnan":
        data = requests.get(base_url + shaanxi["shangnan"]).json()
    i = 1
    city = data["cityInfo"]["city"]
    today_date = data["data"]["forecast"][i]["ymd"]
    low = data["data"]["forecast"][i]["low"]
    low1 = str(low).replace("温 ", "温度：")
    high = data["data"]["forecast"][i]["high"]
    high1 = str(high).replace("温 ", "温度：")
    week = data["data"]["forecast"][i]["week"]
    try:
        aqi = data["data"]["forecast"][i]["aqi"]
    except KeyError:
        aqi = "无"
    weather_type = data["data"]["forecast"][i]["type"]
    wind = data["data"]["forecast"][i]["fx"] + data["data"]["forecast"][i]["fl"]
    notice = data["data"]["forecast"][i]["notice"]
    weather_detail = '''
    <div style="font-size:18px;" class="">
    <hr />
   <li class="">
        预报时间：''' + week + " " + today_date + '''
    </li>
    <li class="">
        天气情况：''' + weather_type + '''
    </li>
    <li class="">
        空气质量： ''' + str(aqi) + '''
    </li>
    <li class="">
        最''' + low1 + '''
    </li>
    <li class="">
        最''' + high1 + '''
    </li>
    <li class="">
        风力情况：''' + wind + '''
    </li>
    <li class="">
        温馨提示：''' + notice + '''
    </li>
    <hr />
    </div>
    '''
    weather_detail_old = "\n-→<<" + city + "天气预报>>←-   " + week + " " + today_date + "\n" + "天气情况：" + weather_type + "\n空气质量：" + str(
        aqi) + "\n最" + low1 + "\n最" + high1 + "\n风力情况：" + wind + "\n温馨提示：" + notice + "\n"
    with open(data["data"]["forecast"][0]["ymd"]+"future_log.txt", "a+") as f:
        f.write(weather_detail_old)
    return weather_detail_old


if __name__ == "__main__":
    print(tomorrow_weather("shangnan"))

"""
Weather API module for fetching and formatting weather data from wttr.in
"""
import requests
from datetime import datetime


def fetch_weather_data(city: str) -> dict:
    """获取城市天气数据"""
    url = f"https://wttr.in/{city}?format=j1&lang=zh"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"获取天气数据失败: {str(e)}")


def format_weather_info(data: dict, city: str) -> str:
    """格式化天气信息为可读文本"""
    try:
        current = data['current_condition'][0]
        location = data['nearest_area'][0]
        location_name = location.get('areaName', [{}])[0].get('value', city)

        result = f"📍 位置: {location_name}\n"
        result += f"🕐 查询时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        result += f"\n{'='*50}\n"
        result += f"🌡️  当前温度: {current['temp_C']}°C (体感 {current['FeelsLikeC']}°C)\n"
        result += f"☁️  天气状况: {current['lang_zh'][0]['value']}\n"
        result += f"💧 湿度: {current['humidity']}%\n"
        result += f"🌬️  风速: {current['windspeedKmph']} km/h\n"
        result += f"🧭 风向: {current['winddir16Point']}\n"
        result += f"👁️  能见度: {current['visibility']} km\n"
        result += f"🌡️  气压: {current['pressure']} mb\n"

        result += f"\n{'='*50}\n"
        result += "📅 未来三天预报\n"
        result += f"{'='*50}\n"

        for day in data['weather'][:3]:
            date = day['date']
            max_temp = day['maxtempC']
            min_temp = day['mintempC']
            desc = day['hourly'][0]['lang_zh'][0]['value']

            result += f"\n📆 {date}\n"
            result += f"   🌡️  温度: {min_temp}°C ~ {max_temp}°C\n"
            result += f"   ☁️  天气: {desc}\n"

        return result
    except KeyError as e:
        raise Exception(f"解析天气数据失败: {str(e)}")

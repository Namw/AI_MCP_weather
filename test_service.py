#!/usr/bin/env python3
"""
Quick test script to verify the weather service works
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mcp_weather.weather_api import fetch_weather_data, format_weather_info

def test_weather_query():
    """Test weather query for Shenzhen"""
    print("Testing weather query for Shenzhen (深圳)...")

    try:
        # Fetch weather data
        data = fetch_weather_data("shenzhen")
        print("✅ Weather data fetched successfully!")

        # Format weather info
        formatted = format_weather_info(data, "shenzhen")
        print("\n" + formatted)
        print("\n✅ All tests passed!")
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_weather_query()
    sys.exit(0 if success else 1)

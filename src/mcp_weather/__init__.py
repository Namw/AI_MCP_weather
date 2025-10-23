"""
MCP Weather Server - China Weather Query Service
A Model Context Protocol (MCP) server for querying weather information in China
"""

__version__ = "1.0.0"
__author__ = "Weather MCP Developer"

from .main import main, server
from .tools import get_tools
from .weather_api import fetch_weather_data, format_weather_info

__all__ = [
    "main",
    "server",
    "get_tools",
    "fetch_weather_data",
    "format_weather_info",
]

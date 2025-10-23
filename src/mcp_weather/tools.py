"""
MCP Tools definition for weather queries
"""
import json
import mcp.types as types
from .weather_api import fetch_weather_data, format_weather_info


def get_tools() -> list[types.Tool]:
    """列出可用的工具"""
    return [
        types.Tool(
            name="get_weather",
            description="查询中国城市的天气信息，包括当前天气和未来三天预报。支持中文城市名，如'深圳'、'广州'、'北京'等。",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "要查询的城市名称，例如：深圳、广州、北京、上海等",
                    }
                },
                "required": ["city"],
            },
        ),
        types.Tool(
            name="get_weather_json",
            description="获取城市天气的原始JSON数据，适合需要进行进一步处理的场景。",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "要查询的城市名称",
                    }
                },
                "required": ["city"],
            },
        ),
    ]


async def handle_tool_call(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """处理工具调用请求"""
    if not arguments:
        raise ValueError("缺少参数")

    city = arguments.get("city")
    if not city:
        raise ValueError("必须提供城市名称")

    try:
        if name == "get_weather":
            data = fetch_weather_data(city)
            weather_info = format_weather_info(data, city)

            return [
                types.TextContent(
                    type="text",
                    text=weather_info
                )
            ]

        elif name == "get_weather_json":
            data = fetch_weather_data(city)

            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(data, ensure_ascii=False, indent=2)
                )
            ]

        else:
            raise ValueError(f"未知的工具: {name}")

    except Exception as e:
        return [
            types.TextContent(
                type="text",
                text=f"❌ 错误: {str(e)}"
            )
        ]

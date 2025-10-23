"""
MCP Weather Server - China Weather Query Service
Supports querying weather for Chinese cities including Shenzhen
"""
import asyncio
import sys
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio

from .tools import get_tools, handle_tool_call


# 添加日志函数（输出到stderr，不会干扰MCP协议）
def log_debug(message: str):
    """输出调试日志到stderr"""
    print(f"[DEBUG] {message}", file=sys.stderr, flush=True)


server = Server("weather-china-server")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """列出可用的工具"""
    return get_tools()


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """处理工具调用请求"""
    return await handle_tool_call(name, arguments)


def main():
    """主函数：运行MCP服务器"""
    async def _run():
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="weather-china-server",
                    server_version="1.0.0",
                    capabilities=server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )

    asyncio.run(_run())


if __name__ == "__main__":
    main()

# MCP Weather Server - 中国天气查询服务

一个基于 Model Context Protocol (MCP) 的中国天气查询服务，支持查询包括深圳在内的各大城市天气信息。

## 功能特性

- 🌡️ 实时天气查询：获取当前温度、湿度、风速、气压等信息
- 📅 三天天气预报：查看未来三天的天气预报
- 🌍 支持中文城市名：直接输入"深圳"、"广州"、"北京"等城市名称
- 🔧 两种查询模式：
  - 格式化模式：易读的中文格式输出
  - JSON 模式：原始JSON数据，便于进一步处理
- 📡 MCP 协议标准：支持MCP Inspector调试和集成

## 项目结构

```
study_mcp_weather/
├── pyproject.toml                 # uv项目配置
├── uv.lock                        # 依赖锁定文件
├── README.md                      # 本文件
├── weather.py                     # 原始完整实现（备用）
└── src/
    └── mcp_weather/
        ├── __init__.py            # 包初始化
        ├── main.py                # MCP服务主文件
        ├── tools.py               # 工具定义和调用处理
        └── weather_api.py         # 天气API和数据格式化
```

## 快速开始

### 前置要求

- Python 3.9+
- uv 包管理工具

### 安装依赖

```bash
# 使用 uv 安装依赖
uv sync
```

这会创建 `uv.lock` 文件来锁定依赖版本。

### 运行服务

```bash
# 方式1：使用 uv 运行
uv run mcp-weather

# 方式2：直接运行（需要先激活环境）
python -m mcp_weather.main
```

服务会启动并监听标准输入/输出，等待 MCP 客户端连接。

## 使用 MCP Inspector 进行调试

MCP Inspector 是调试 MCP 服务的官方工具。

### 安装 MCP Inspector

```bash
# 使用 npm 安装
npm install -g @modelcontextprotocol/inspector
```

### 配置方法

#### 方法1：使用命令行直接运行

```bash
mcp-inspector "uv" "run" "mcp-weather"
```

#### 方法2：编辑 MCP 配置文件

编辑你的 Claude 配置文件（如 `~/Library/Application Support/Claude/claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": ["run", "mcp-weather"],
      "cwd": "/Users/youname/PycharmProjects/study_mcp_weather"
    }
  }
}
```

然后在 Claude 中调用天气查询。

### 使用 MCP Inspector 调试步骤

1. 打开命令行，进入项目目录
2. 运行 `mcp-inspector "uv" "run" "mcp-weather"`
3. Inspector 会打开本地网页界面
4. 在网页中可以：
   - 查看服务器列出的工具
   - 测试工具调用
   - 查看完整的请求/响应日志

## 可用工具

### 1. `get_weather` - 格式化天气查询

查询城市天气并返回格式化的可读文本。

**参数：**
- `city` (string, 必需)：城市名称，如"深圳"、"广州"、"北京"等

**返回示例：**
```
📍 位置: Shenzhen
🕐 查询时间: 2024-10-24 14:30:45

==================================================
🌡️  当前温度: 28°C (体感 29°C)
☁️  天气状况: 晴天
💧 湿度: 65%
🌬️  风速: 12 km/h
🧭 风向: SE
👁️  能见度: 10 km
🌡️  气压: 1013 mb

==================================================
📅 未来三天预报
==================================================

📆 2024-10-24
   🌡️  温度: 24°C ~ 30°C
   ☁️  天气: 晴天

📆 2024-10-25
   🌡️  温度: 23°C ~ 29°C
   ☁️  天气: 晴天

📆 2024-10-26
   🌡️  温度: 22°C ~ 28°C
   ☁️  天气: 多云
```

### 2. `get_weather_json` - JSON 数据查询

获取城市天气的原始 JSON 数据，适合需要进一步处理的场景。

**参数：**
- `city` (string, 必需)：城市名称

**返回：** 完整的原始 JSON 数据结构

## API 数据来源

本服务使用免费的 [wttr.in](https://wttr.in/) API：
- 无需 API 密钥
- 支持中文查询和中文输出
- 支持全球城市查询
- 响应时间快

## 环境变量

当前版本不需要环境变量配置。天气数据完全来自 wttr.in 公开 API。

## 故障排查

### 问题：连接超时
- 检查网络连接
- 确保能访问 https://wttr.in/ 网站
- 尝试增加超时时间（当前为10秒）

### 问题：城市名称无法识别
- 使用标准的城市中文名称
- wttr.in 会自动匹配最接近的城市
- 可以尝试英文城市名称

### 问题：MCP Inspector 无法连接
- 确保服务已启动
- 检查命令路径是否正确
- 查看终端输出的错误信息

## 开发信息

### 添加新工具

编辑 `src/mcp_weather/tools.py`：

1. 在 `get_tools()` 函数中添加新的 `types.Tool` 定义
2. 在 `handle_tool_call()` 中添加对应的处理逻辑

### 修改天气数据源

编辑 `src/mcp_weather/weather_api.py`：
- 修改 `fetch_weather_data()` 函数中的 API 地址
- 调整 `format_weather_info()` 中的数据解析逻辑

### 运行测试

```bash
uv run pytest
```

## 许可证

MIT License

## 参考资源

- [MCP (Model Context Protocol) 文档](https://modelcontextprotocol.io/)
- [MCP Inspector 工具](https://github.com/modelcontextprotocol/inspector)
- [wttr.in 天气 API](https://wttr.in/)
- [uv 包管理器](https://docs.astral.sh/uv/)

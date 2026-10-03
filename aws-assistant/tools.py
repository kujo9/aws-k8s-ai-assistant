"""Where the tools come from.
"""

from langchain_mcp_adapters.client import MultiServerMCPClient

from config import MCP_ENDPOINT, REGION


async def load_tools():
    """Start the signing proxy and return the tools the AWS MCP Server offers."""
    client = MultiServerMCPClient({
        "aws": {
            "transport": "stdio",
            "command": "uvx",
            "args": ["mcp-proxy-for-aws@latest", MCP_ENDPOINT, "--metadata", f"AWS_REGION={REGION}"],
        }
    })
    return await client.get_tools()
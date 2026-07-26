import hashlib

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

EMAIL = "24f2002227@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-mcp")


@mcp.tool
async def solve_challenge() -> str:
    """
    Solve the exam challenge.
    """

    headers = get_http_headers()

    challenge = headers.get("x-exam-challenge")

    if not challenge:
        return "missing challenge"

    return hashlib.sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()[:16]


app = mcp.streamable_http_app()

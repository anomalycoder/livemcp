import hashlib

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

EMAIL = "24f2002227@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-mcp")


@mcp.tool
def solve_challenge() -> str:
    """Return the challenge response."""

    headers = get_http_headers()

    challenge = (
        headers.get("x-exam-challenge")
        or headers.get("X-Exam-Challenge")
    )

    if not challenge:
        return "missing challenge"

    return hashlib.sha256(
        f"{challenge}:{EMAIL}".encode("utf-8")
    ).hexdigest()[:16]


app = mcp.http_app()

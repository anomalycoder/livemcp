import hashlib
from fastmcp import FastMCP
from starlette.requests import Request

EMAIL = "24f2002227@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-mcp")


@mcp.tool(
    name="solve_challenge",
    description="Solve exam challenge"
)
async def solve_challenge(request: Request):

    challenge = request.headers.get("X-Exam-Challenge")

    if challenge is None:
        return "missing challenge"

    value = hashlib.sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()[:16]

    return value


app = mcp.http_app()

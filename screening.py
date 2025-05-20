from typing import Any, TypedDict, Optional
from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta

# Initialize FastMCP server
mcp = FastMCP("screening")

@mcp.tool()
async def get_candidates() -> str:
    """Fetch available candidates.
    """
    
    data = get_fake_candidates()
    candidates = [format_candidate(candidate) for candidate in data]
    return "\n---\n".join(candidates)

@mcp.tool()
async def propose_interview(id: int, date: str, time: str) -> str:
    """Propose an interview schedule for a candidate.

    Args:
        id (int): The candidate's id.
        date (str): The proposed interview date in YYYY-MM-DD format.
        time (str): The proposed interview time in HH:MM format.
    """
    candidates = get_fake_candidates()
    for candidate in candidates:
        if candidate["ID"] == id:
            return f'Success: Interview with {candidate["名前"]} has been successfully arranged for {date}, {time}.'
    return "No active candidate."

def get_fake_candidates():
    candidates = [
                {
                    "ID": 1,
                    "名前": "川村 真理",
                    "性別": "女性",
                    "年齢": 28,
                    "設問A": 3,
                    "設問B": 5,
                    "設問C": 5,
                    "設問D": "美術館やカフェ巡りをして、インスピレーションを得ています。"
                },
                {
                    "ID": 2,
                    "名前": "佐野 健太",
                    "性別": "男性",
                    "年齢": 33,
                    "設問A": 3,
                    "設問B": 5,
                    "設問C": 4,
                    "設問D": "家で映画やドキュメンタリーを観てのんびり過ごします。"
                },
                {
                    "ID": 3,
                    "名前": "高田 美咲",
                    "性別": "女性",
                    "年齢": 24,
                    "設問A": 4,
                    "設問B": 3,
                    "設問C": 5,
                    "設問D": "友人とショッピングに出かけたり、新しいカフェを開拓しています。"
                },
                {
                    "ID": 4,
                    "名前": "山口 翔",
                    "性別": "男性",
                    "年齢": 37,
                    "設問A": 5,
                    "設問B": 4,
                    "設問C": 3,
                    "設問D": "子どもと一緒に公園や図書館へ行って過ごすのが楽しみです。"
                },
                {
                    "ID": 5,
                    "名前": "藤井 彩音",
                    "性別": "女性",
                    "年齢": 30,
                    "設問A": 4,
                    "設問B": 5,
                    "設問C": 2,
                    "設問D": "読書や音楽を聴いて、静かに自分の時間を楽しんでいます。"
                }
            ]
    return candidates

def format_candidate(candidate: dict) -> str:
    """Format a candidate into a readable string."""
    return f"""
ID: {candidate.get('ID', 'Unknown')}
名前: {candidate.get('名前', 'Unknown')}
性別: {candidate.get('性別', 'Unknown')}
年齢: {candidate.get('年齢', 'Unknown')}
設問A)家族時間の重要性: {candidate.get('設問A', 'Unknown')}
設問B)自分時間の重要性: {candidate.get('設問B', 'Unknown')}
設問C)新しい体験への興味: {candidate.get('設問C', 'Unknown')}
設問D)休日の過ごし方: {candidate.get('設問D', 'Unknown')}
"""

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

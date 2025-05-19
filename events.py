from typing import Any, TypedDict, Optional
from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta

# Initialize FastMCP server
mcp = FastMCP("events")

class PaymentInfo(TypedDict):
    credit: str

@mcp.tool()
async def get_tokyo_events(start: str, end: str) -> str:
    """Fetch events being held in Tokyo.

    Args:
        start: The start date(format:YYYY-MM-DD) for the search range. Events starting on or after this date will be included.
        end: The end date(format:YYYY-MM-DD) for the search range. Events ending before or on this date will be included.
    """
    
    data = get_fake_events()
    events = [format_event(event) for event in data]
    return "\n---\n".join(events)

@mcp.tool()
async def make_reservation(event_id: int, email: str, payment_info: Optional[PaymentInfo] = None) -> str:
    """Make a reservation for an event. Name and email are required.

    Args:
        event_id: id for event
        email: user email
        payment_info: optional payment info for paid events
    """
    events = get_fake_events()
    for event in events:
        if event["id"] == event_id:
            if event["price"] > 0:
                if not payment_info:
                    return "Failed: Need process payment"
                else:
                    return f'Success: Payment of ¥{event["price"]} with {payment_info["credit"]} was processed successfully.'
            else:
                return "Success"
    return "No active events for this id."

# @mcp.tool()
# async def process_payment(amount: int, payment_info: PaymentInfo):
#     """Process payment.

#     Args:
#         amount: amount to be paid
#         payment_info: user's payment info
#     """
#     return {
#         "status": "Success",
#         "message": f"Payment of ¥{amount} with {payment_info["credit"]} was processed successfully."
#         }

def get_fake_events():
    # base_date = datetime.now()
    base_date = datetime(2025, 6, 10)
    events = [
        {
            "id": 1,
            "name": "Tokyo Tech Expo 2025",
            "date": (base_date + timedelta(days=3)).strftime("%Y-%m-%d"),
            "place": "Tokyo Big Sight",
            "price": 1500 
        },
        {
            "id": 2,
            "name": "Shibuya Music Festival",
            "date": (base_date + timedelta(days=7)).strftime("%Y-%m-%d"),
            "place": "Shibuya Station Area",
            "price": 900
        },
        {
            "id": 3,
            "name": "Asakusa Culture Walk",
            "date": (base_date + timedelta(days=10)).strftime("%Y-%m-%d"),
            "place": "Asakusa",
            "price": 0
        },
        {
            "id": 4,
            "name": "Tokyo Food Carnival",
            "date": (base_date + timedelta(days=14)).strftime("%Y-%m-%d"),
            "place": "Yoyogi Park",
            "price": 500
        },
        {
            "id": 5,
            "name": "Ginza Art Night",
            "date": (base_date + timedelta(days=15)).strftime("%Y-%m-%d"),
            "place": "Ginza",
            "price": 0
        },
    ]
    return events

def format_event(event: dict) -> str:
    """Format an event into a readable string."""
    return f"""
ID: {event.get('id', 'Unknown')}
NAME: {event.get('name', 'Unknown')}
DATE: {event.get('date', 'Unknown')}
PLACE: {event.get('place', 'Unknown')}
PRICE: {event.get('price', 'Unknown')}
"""

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

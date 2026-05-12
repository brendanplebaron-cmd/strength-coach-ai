from notion_client import Client
import os

notion = Client(auth=os.environ["NOTION_API_KEY"])

DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

def get_last_workout():
    return notion.databases.query(
        database_id=DATABASE_ID,
        page_size=5
    )

def write_workout(content):
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "Auto Workout"
                        }
                    }
                ]
            },
            "AI Output": {
                "rich_text": [
                    {
                        "text": {
                            "content": str(content)
                        }
                    }
                ]
            }
        }
    )

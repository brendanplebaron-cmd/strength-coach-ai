from gemini_engine import generate_workout
from notion_client import get_last_workout, write_workout

def build_prompt(last_workout):
    return f"""
You are a strength programming engine.

Last workout data:
{last_workout}

Generate next A/B/C progression workout.
Follow all rules:
- A = reduced load or reps
- B = repeat prior performance
- C = progressive overload target
- Exercise-level progression only
- Near failure is acceptable (RPE 8–10)
"""

def run():
    last = get_last_workout()
    prompt = build_prompt(last)

    result = generate_workout(prompt)

    write_workout(result)

if __name__ == "__main__":
    run()

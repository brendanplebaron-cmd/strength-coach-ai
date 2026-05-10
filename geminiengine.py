import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_workout(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")

    response = model.generate_content(prompt)

    return response.text

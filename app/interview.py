import os

from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

    base_url="https://api.groq.com/openai/v1"
)


def generate_questions(skills):

    all_questions = []

    for skill in skills:

        prompt = f"""
Generate 3 technical interview questions
for skill: {skill}

Return ONLY questions.
"""

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3
        )

        result = response.choices[0].message.content

        questions = [

            q.strip()

            for q in result.split("\n")

            if q.strip()
        ]

        all_questions.append({

            "skill": skill,

            "questions": questions
        })

    return all_questions

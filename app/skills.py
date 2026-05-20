import os

from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

    base_url="https://api.groq.com/openai/v1"
)


def extract_skills(resume_text):

    prompt = prompt = f"""
You are a resume skill extractor.

Return ONLY a comma separated list.

NO introduction.
NO explanation.
NO numbering.
NO sentences.

Extract ONLY:
- programming languages
- frameworks
- databases
- cloud tools
- ML libraries

Ignore:
- projects
- responsibilities
- soft skills

Resume:
{resume_text}

"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    result = response.choices[0].message.content

    return [

        skill.strip()

        for skill in result.split(",")

        if skill.strip()
    ]

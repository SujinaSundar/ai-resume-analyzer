from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

MODEL_NAME = (
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)


def generate_questions(skills):

    all_questions = []

    # Limit skills for speed
    skills = skills[:5]

    for skill in skills:

        prompt = f"""
Generate 3 technical interview questions
for a candidate skilled in {skill}.

Return ONLY the questions.
Do not include explanations.
"""

        result = generator(
            prompt,
            max_new_tokens=80,
            temperature=0.3,
            do_sample=False
        )

        generated_text = result[0][
            "generated_text"
        ]

        # Remove prompt from output
        answer = generated_text.replace(
            prompt,
            ""
        ).strip()

        # Split questions
        questions = answer.split("\n")

        cleaned_questions = []

        for question in questions:

            question = question.strip()

            if question:

                cleaned_questions.append(
                    question
                )

        all_questions.append({

            "skill": skill,

            "questions": cleaned_questions
        })

    return all_questions

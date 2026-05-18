from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

tokenizer = AutoTokenizer.from_pretrained(
    "google/flan-t5-base"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "google/flan-t5-base"
)

def generate_questions(skill):

    prompt = (
        f"Generate 5 technical interview "
        f"questions for {skill}."
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        temperature=0.7,
        do_sample=True
    )

    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return result
from app.dataset_loader import (
    load_resume_dataset
)

df = load_resume_dataset()

print(df.columns)
print(df.head())

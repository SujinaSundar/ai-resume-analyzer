import pandas as pd

def load_resume_dataset():

    df = pd.read_csv(
        "data/Resume.csv"
    )

    return df

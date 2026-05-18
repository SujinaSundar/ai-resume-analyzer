from app.ats import (
    calculate_ats_score
)

def test_ats_score():

    score = calculate_ats_score(
        "python fastapi docker",
        "python docker"
    )

    assert score > 0

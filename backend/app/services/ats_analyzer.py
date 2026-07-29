def calculate_ats(skills):

    required_skills = [
        "python",
        "sql",
        "fastapi",
        "docker",
        "git",
        "machine learning",
        "numpy",
        "pandas"
    ]

    matched = 0

    missing = []

    for skill in required_skills:

        if skill in skills:
            matched += 1
        else:
            missing.append(skill)

    score = round((matched / len(required_skills)) * 100)

    return {
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }
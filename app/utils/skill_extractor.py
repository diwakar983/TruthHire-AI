SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "mongodb",
    "mysql",
    "fastapi",
    "flask",
    "docker",
    "git",
    "github",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "scikit-learn",
    "aws",
    "oracle cloud",
    "linux",
    "api"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills
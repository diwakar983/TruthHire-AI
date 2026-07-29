PROJECT_HEADERS = [
    "projects",
    "project",
    "academic projects",
    "relevant projects"
]

EXPERIENCE_HEADERS = [
    "experience",
    "work experience",
    "professional experience",
    "internship"
]

CERTIFICATE_HEADERS = [
    "certification",
    "certifications",
    "training",
    "courses"
]


def get_section(text, headings):

    text = text.lower()

    for heading in headings:

        if heading in text:

            return text.split(heading)[-1]

    return ""


def detect_truth(text, skills):

    projects = get_section(text, PROJECT_HEADERS)

    experience = get_section(text, EXPERIENCE_HEADERS)

    certifications = get_section(text, CERTIFICATE_HEADERS)

    verified = []

    suspicious = []

    evidence = {}

    for skill in skills:

        score = 0

        if skill in projects:
            score += 40

        if skill in experience:
            score += 40

        if skill in certifications:
            score += 20

        evidence[skill] = score

        if score >= 40:
            verified.append(skill)
        else:
            suspicious.append(skill)

    if len(skills) == 0:
        truth_score = 0
    else:
        truth_score = round(sum(evidence.values()) / len(skills))

    return {

        "truth_score": truth_score,

        "verified_skills": verified,

        "suspicious_skills": suspicious,

        "evidence": evidence
    }
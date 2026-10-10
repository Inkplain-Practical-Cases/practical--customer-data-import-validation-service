def normalize_email(email: str) -> str:
    return email.strip().lower()

def validate_rows(rows):
    accepted, rejected, seen = [], [], set()
    for number, row in enumerate(rows, 1):
        name, email = row.get("name"), row.get("email")
        if not isinstance(name, str) or not name.strip():
            rejected.append({"row": number, "reason": "name is required"})
            continue
        if not isinstance(email, str) or "@" not in email:
            rejected.append({"row": number, "reason": "email is invalid"})
            continue
        email = normalize_email(email)
        if email in seen:
            rejected.append({"row": number, "reason": "duplicate email"})
            continue
        seen.add(email)
        accepted.append({"name": name.strip(), "email": email})
    return accepted, rejected

import re

def get_email(raw_txt):
    try:
        regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        match = re.search(regex, raw_txt)
        email = match[0]
    except:
        email = ""

    return email

def get_phone(raw_txt):
    try:
        regex = r"(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}"
        match = re.search(regex, raw_txt)
        phone = match[0]
    except:
        phone = ""

    return phone
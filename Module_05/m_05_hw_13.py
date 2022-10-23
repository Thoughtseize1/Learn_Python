import re


def find_all_emails(text):
    pattern = r"[a-zA-Z]{1,}[a-zA-Z0-9._]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,}"
    result = re.findall(pattern, text)
    print(result)
    return result
# Another working regex
# [a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}


find_all_emails(
    'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net')

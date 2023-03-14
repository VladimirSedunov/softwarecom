from dataclasses import dataclass


@dataclass
class Claim_about:
    fio: str
    phone: str
    email: str
    text: str
    agree: str
    ajax: int
    is_error: bool
    status_code: int
    status: str
    expected_message: str

    def __init__(self, title, fio, phone, email, text, agree, ajax, is_error, status_code, status, expected_message):
        self.title = title
        self.fio = fio
        self.phone = phone
        self.email = email
        self.text = text
        self.agree = agree
        self.ajax = ajax
        self.is_error = is_error
        self.status_code = status_code
        self.status = status
        self.expected_message = expected_message

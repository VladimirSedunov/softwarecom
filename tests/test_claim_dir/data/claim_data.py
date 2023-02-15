# Alla Alekhina
from dataclasses import dataclass


@dataclass
class Claim:
    title: str
    fio: str
    email: str
    phone: str
    text: str
    is_error: bool
    expected_result_message: str

    def __init__(self, title, fio, email, phone, text, is_error, expected_result_message):
        self.title = title
        self.fio = fio
        self.email = email
        self.phone = phone
        self.text = text
        self.is_error = is_error
        self.expected_result_message = expected_result_message

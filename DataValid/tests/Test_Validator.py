import pytest
from DataValidityCheck import __version__
from DataValidityCheck.validate_info_data import DataValidator

def test_version():
	assert __version__ == "0.0.4"


validator = DataValidator()


@pytest.mark.parametrize("email, expected", [
    ("", "Email field cannot be empty."),
    ("verylongemail" + "a" * 310 + "@example.com", "Email is too long. It must not exceed 320 characters."),
    ("plainaddress", "Invalid email format. Ensure it follows the pattern 'example@domain.com'."),
    ("user@domain", "Invalid email format. Ensure it follows the pattern 'example@domain.com'."),
    ("user@domain.com", "Valid email address."),
])
def test_validate_email(email, expected):
    assert validator.validate_email(email) == expected


@pytest.mark.parametrize("phone, expected", [
    ("", "Phone number cannot be empty."),
    ("12345", "Invalid phone number format. Use a valid local or international format."),
    ("+1234567890123456", "Invalid phone number format. Use a valid local or international format."),
    ("+2348012345678", "Valid phone number!"),
    ("08012345678", "Valid phone number!"),
])
def test_validate_phone(phone, expected):
    assert validator.validate_phone(phone) == expected


@pytest.mark.parametrize("date, expected", [
    ("", "Date field cannot be empty."),
    ("32/01/2023", "Invalid date format."),
    ("31/04/2023", "Invalid date format."),  # April has only 30 days
    ("29/02/2023", "Invalid date format."),  # 2023 is not a leap year
    ("15/08/2023", "Valid date"),
])
def test_validate_date(date, expected):
    assert validator.validate_date(date) == expected


@pytest.mark.parametrize("url, expected", [
    ("", "URL field cannot be empty."),
    ("google", "Invalid URL format. Ensure it starts with 'http://' or 'https://'."),
    ("htp://invalid.com", "Invalid URL format. Ensure it starts with 'http://' or 'https://'."),
    ("www.domain.org", "Valid URL."),
    ("https://www.google.com", "Valid URL."),
    ("http://example.com", "Valid URL."),
])
def test_validate_url(url, expected):
    assert validator.validate_url(url) == expected
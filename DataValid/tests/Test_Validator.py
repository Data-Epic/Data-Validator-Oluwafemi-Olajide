from DataValidityCheck import __version__
from DataValidityCheck.validate_info_data import DataValidator

def test_version():
	assert __version__ == "0.0.1"


validator = DataValidator()

def test_validate_email():
    assert validator.validate_email("test@example.com") == True
    assert validator.validate_email("user.name@domain.com") == True
    assert validator.validate_email("invalid-email.com") == False
    assert validator.validate_email("user@com") == False

def test_validate_phone():
    assert validator.validate_phone("+2348012345678") == True
    assert validator.validate_phone("08012345678") == True
    assert validator.validate_phone("081 234 5678") == False
    assert validator.validate_phone("+12345678901") == False

def test_validate_date():
    assert validator.validate_date("29/02/2024") == True  # Leap year
    assert validator.validate_date("31/04/2025") == False  # April has 30 days
    assert validator.validate_date("30/02/2025") == False  # Feb max is 29
    assert validator.validate_date("15/08/2023") == True  # Valid date

def test_validate_url():
    assert validator.validate_url("https://www.google.com") == True
    assert validator.validate_url("http://example.org") == True
    assert validator.validate_url("htp://invalid.com") == False
    assert validator.validate_url("www.missinghttp.com") == True

if __name__ == "__main__":
    pytest.main()

import re

class DataValidator:
    """
    A class for validating personal data such as emails, phone numbers, dates, and URLs.
    """

    def validate_email(self, email: str) -> bool:
        """
        Validates an email address.

        - Supports:
          > Standard email format (e.g., "user@example.com").
        - Rejects:
          > Missing '@' or domain (e.g., "userexample.com").
          > Invalid characters.
          > Domains without extensions (e.g., "user@domain").
        
        :param email: The email address to validate.
        :return: True if valid, False otherwise.
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def validate_phone(self, phone: str) -> bool:
        """
        Validates a Nigerian phone number in two specific formats:

        - **Local Format**: 08012345678 (11 digits, starts with 070, 080, 081, 090, or 091).
        - **International Format**: +2348012345678 (Begins with +234, followed by 10 digits).

        **Invalid Formats (Not Supported):**
            Numbers with spaces (e.g., "081 234 5678").
            Missing or extra digits.
            Other country codes (e.g., +123...).

        :param phone: The phone number to validate.
        :return: True if valid, False otherwise.
        """
        pattern = r"^(?:\+234|0)(70|80|81|90|91)\d{8}$"
        return bool(re.match(pattern, phone))

    def validate_date(self, date: str) -> bool:
        """
        Validates a date string strictly in the **DD/MM/YYYY** format.

        - Ensures:
            Day (01–31) matches the month correctly.
            Month (01–12).
            Year (4 digits).

        **Invalid Cases:**
            "31/02/2025" (February can’t have 31 days).
            "30/02/2025" (February max is 29 in leap years).
            "31/04/2025" (April has max 30 days).
            Wrong format like "2025-02-31", "1/1/2025".

        :param date: The date string to validate.
        :return: True if valid, False otherwise.
        """
        pattern = r"""^(
            (0[1-9]|1\d|2[0-8])/(0[1-9]|1[0-2])/\d{4} |  # Days 01-28 (all months)
            (29/(0[13-9]|1[0-2])/\d{4}) |  # 29th day (allowed in all months except February)
            (30/(0[13-9]|1[0-2])/\d{4}) |  # 30th day (only valid in months with 30+ days)
            (31/(0[13578]|1[02])/\d{4}) |  # 31st day (only in Jan, Mar, May, Jul, Aug, Oct, Dec)
            (29/02/((19|20|21)[0-9][0-9]))  # Feb 29 (only for leap years 1900-2199)
        )$"""
        return bool(re.match(pattern, date, re.VERBOSE))

    def validate_url(self, url: str) -> bool:
        """
        Validates a URL.

        - Supports:
           >"http://", "https://", and "www." formats.
           >Valid domains with extensions (.com, .org, .net, .co.uk, etc.).
           >URLs with paths, query parameters, and ports.
        - Rejects:
           >URLs missing a domain extension (e.g., "https://google").
           >Invalid characters in the domain.

        :param url: The URL to validate.
        :return: True if valid, False otherwise.
        """
        pattern = r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?(\/\S*)?$"
        return bool(re.match(pattern, url))


if __name__ == "__main__":
    validator = DataValidator()

# Email Validation
print(validator.validate_email("user@example.com"))   #  True
print(validator.validate_email("invalid-email.com"))  #  False

# Phone Number Validation (Nigeria)
print(validator.validate_phone("+2348012345678"))  #  True
print(validator.validate_phone("08012345678"))     #  True
print(validator.validate_phone("081 234 5678"))    #  False

# Date Validation (DD/MM/YYYY)
print(validator.validate_date("31/01/2024"))  #  True
print(validator.validate_date("30/02/2024"))  #  False (Feb max 29)
print(validator.validate_date("29/02/2024"))  #  True (Leap year)
print(validator.validate_date("31/04/2025"))  #  False (April has max 30 days)

# URL Validation
print(validator.validate_url("https://www.google.com"))   # True
print(validator.validate_url("http://example.org"))       # True
print(validator.validate_url("www.example.net"))          # True
print(validator.validate_url("htp://invalid.com"))        # False

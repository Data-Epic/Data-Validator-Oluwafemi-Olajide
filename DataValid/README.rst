DataValidityCheck - Data Validation Package
===========================================

Overview
--------

**DataValidityCheck** is a Python package designed to validate personal
data, including emails, phone numbers, dates, and URLs. It provides
robust validation methods to ensure data accuracy and compliance with
common formats.

Table of Contents
-----------------

- `Installation <#installation>`__
- `Features <#features>`__
- `Usage <#usage>`__

  - `Email Validation <#email-validation>`__
  - `Phone Number Validation <#phone-number-validation>`__
  - `Date Validation <#date-validation>`__
  - `URL Validation <#url-validation>`__

- `Contributing <#contributing>`__
- `Author <#author>`__
- `License <#license>`__

Installation
------------

To install **DataValidityCheck**, use:

.. code:: bash

   pip install DataValidityCheck

Features
--------

- **Email Validation**: Ensures a valid email format with proper domain
  structure.
- **Phone Number Validation**: Supports Nigerian phone numbers in local
  and international formats.
- **Date Validation**: Validates dates in the ``DD/MM/YYYY`` format,
  including leap years.
- **URL Validation**: Checks for valid domain structures, including
  ``http://``, ``https://``, and ``www.`` prefixes.

Usage
-----

First, import the ``DataValidator`` class:

.. code:: python

   from DataValidityCheck import DataValidator

   validator = DataValidator()

Email Validation
~~~~~~~~~~~~~~~~

.. code:: python

   print(validator.validate_email("user@example.com"))  # Valid email address
   print(validator.validate_email("invalid-email"))  # Invalid email format, ensure it follows example "example@domain.com."

Phone Number Validation
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   print(validator.validate_phone("08123456789"))  # Valid phone number
   print(validator.validate_phone("+2348123456789"))  # Valid phone number
   print(validator.validate_phone("123456"))  # Invalid phone number format

Date Validation
~~~~~~~~~~~~~~~

.. code:: python

   print(validator.validate_date("29/02/2024"))  # Valid date (Leap year)
   print(validator.validate_date("31/04/2023"))  # Invalid date (April has 30 days)

URL Validation
~~~~~~~~~~~~~~

.. code:: python

   print(validator.validate_url("https://www.google.com"))  # Valid URL
   print(validator.validate_url("htp://invalid.com"))  # Invalid URL format

Contributing
------------

Contributions are welcome! To contribute: 1. Fork the repository. 2.
Create a new branch (``feature-branch``). 3. Commit your changes. 4.
Submit a pull request.

Ensure you run tests before submitting:

.. code:: bash

   pytest tests/

Author
------

**Olajide Oluwafemi Richard**

License
-------

This package is open-source and available under the `MIT
License <LICENSE>`__.

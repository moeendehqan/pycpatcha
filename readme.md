```markdown
# PyCaptcha

## Installation

You can install PyCaptcha using pip:

```bash
pip install pycaptcha
```

## Usage

```python
from pycaptcha import PyCaptcha

captcha = PyCaptcha()
result = captcha.Captcha_generation()
image_data = result['image']
response = result['encrypted_response']
```

To check the user's response:

```python
if captcha.check_response(response, user_response):
    print("Captcha verification successful!")
else:
    print("Captcha verification failed.")
```

## Configuration

PyCaptcha supports the following configuration options:

- `num_char` (int): Number of characters in the CAPTCHA (default is 4).
- `only_num` (bool): If True, only digits are used for characters; otherwise, both letters and digits are used (default is False).

You can customize these options when generating a CAPTCHA:

```python
result = captcha.Captcha_generation(num_char=6, only_num=True)
```

## Author

moeen dehqan
Email: moeen.dehqan@gmail.com


```
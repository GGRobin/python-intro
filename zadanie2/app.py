# app.py
# Implementacja funkcji do lab2

def is_valid_email(email: str) -> bool:
    """Sprawdza podstawowy format email: musi zawierac '@' oraz kropke po @."""
    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False
    local, domain = email.split("@", 1)
    return "." in domain and len(local) > 0 and len(domain) > 0

def calculate_circle_area(radius: float) -> float:
    """Oblicza pole kola: pi * r^2. Rzuca ValueError gdy radius < 0."""
    import math
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

def filter_even_numbers(numbers: list) -> list:
    """Zwraca tylko liczby parzyste (int) z listy."""
    if not isinstance(numbers, list):
        raise ValueError("numbers must be a list")
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]

def convert_date_format(date_str: str) -> str:
    """Konwertuje 'YYYY-MM-DD' na 'DD/MM/YYYY'. Rzuca ValueError dla niepoprawnego formatu."""
    if not isinstance(date_str, str):
        raise ValueError("date_str must be a string")
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError("Niepoprawny format daty, oczekiwany YYYY-MM-DD")

    yyyy, mm, dd = parts

    if not (yyyy.isdigit() and len(yyyy) == 4):
        raise ValueError("Niepoprawny format daty, rok powinien byc YYYY")

    if not (mm.isdigit() and 1 <= int(mm) <= 12 and 1 <= len(mm) <= 2):
        raise ValueError("Niepoprawny format daty, miesiac powinien byc MM (01-12)")

    if not (dd.isdigit() and 1 <= int(dd) <= 31 and 1 <= len(dd) <= 2):
        raise ValueError("Niepoprawny format daty, dzien powinien byc DD (01-31)")

    mm2 = mm.zfill(2)
    dd2 = dd.zfill(2)
    return f"{dd2}/{mm2}/{yyyy}"

def is_palindrome(text: str) -> bool:
    """Sprawdza, czy tekst jest palindromem (ignoruje spacje i znaki nie-alfanumeryczne)."""
    if not isinstance(text, str):
        return False
    s = "".join(ch.lower() for ch in text if ch.isalnum())
    return s == s[::-1]

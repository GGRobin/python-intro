# app.py
# Implementacja funkcji do lab2

def is_valid_email(email: str) -> bool:
    """Sprawdza podstawowy format email:
    - email musi byc stringiem,
    - musi zawierac jednego '@',
    - lokal-part (przed @) nie moze byc pusty,
    - domena (po @) nie moze byc pusta,
    - domena musi zawierac co najmniej jedna kropke,
    - domena nie moze zaczynac sie ani konczyc kropka,
    - zaden fragment domeny (między kropkami) nie moze byc pusty.
    """
    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False

    # rozdzielamy na lokalna i domena tylko po pierwszym '@'
    parts = email.split("@")
    if len(parts) != 2:
        return False  # wiecej niz jedno @ -> odrzucamy
    local, domain = parts
    if not local:
        return False
    if not domain:
        return False

    # domena musi zawierac kropke i nie moze zaczynac/konczyc sie kropka
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False

    # kazdy fragment domeny oddzielony kropka nie moze byc pusty
    labels = domain.split(".")
    if any(label == "" for label in labels):
        return False

    return True

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



import re

def extract_domain(url):
    """
    Функция для извлечения домена из URL.
    """
    # Проверяем, что URL начинается с протокола http или https
    pattern = r"^(http://|https://)?([a-zA-Z0-9.-]+)(/)?$"
    match = re.match(pattern, url)
    
    if not match:
        raise ValueError("Некорректный URL")
    
    # Возвращаем доменное имя из URL (группа 2 в регулярном выражении)
    return match.group(2)

def is_domain(url, domain):
    """
    Функция для проверки, является ли введенная строка доменом из URL.
    """
    try:
        extracted_domain = extract_domain(url)
        return extracted_domain == domain
    except ValueError:
        return False

# Примеры использования
try:
    print(is_domain("http://example.com/", "example.com"))  # True
    print(is_domain("example.com", "net"))                  # False
    print(is_domain("кремль.рф", "кремль.рф"))             # False (некорректный URL)
except ValueError as e:
    print("Ошибка:", e)

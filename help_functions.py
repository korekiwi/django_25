from django.utils.text import slugify as django_slugify
from unidecode import unidecode


def python_slugify(s: str):
    return unidecode(django_slugify(s))

def python_slugify_list(lst: list[str]):
    returned_lst = []
    for item in lst:
        returned_lst.append(python_slugify(item))
    return returned_lst
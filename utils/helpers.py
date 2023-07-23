import random
import string

def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def format_date(date):
   return date.strftime('%d/%m/%Y')

def count_words(text):
    return len(text.split())
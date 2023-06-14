import random
import string

def generate_random_password(length):

    # Определение символов, из которых будет состоять пароль
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерация пароля с помощью случайного выбора символов
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Генерация пароля длиной 8 символов
password = generate_random_password(8)
print(password)

"""
Добавьте к задаче логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

Задача:
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только 
на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
import argparse
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def is_prime(n):
    """Проверяет, является ли число простым."""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    parser = argparse.ArgumentParser(
        description='Проверка, является ли число простым или составным.')
    parser.add_argument('-number', type=int, default=-1, help='Число для проверки')
    args = parser.parse_args()
    number = args.number

    logger.info(f'Получено число: {number}')

    if number < 0 or number > 100000:
        logger.error('Число вне допустимого диапазона (0-100000)')
        print('Число должно быть между 0 и 100000')
        return
    if number <= 1:
        logger.info('Числа 1 и 0 - не являются ни простыми, ни составными')
        print(f'Число {number} - не являются ни простым, ни составным')
    elif is_prime(number):
        logger.info(f'{number} - простое число')
        print(f'{number} - простое число')
    else:
        logger.info(f'{number} - составное число')
        print(f'{number} - составное число')

if __name__ == "__main__":
    main()

# В терминале: Python dz_15_library\task_1.py
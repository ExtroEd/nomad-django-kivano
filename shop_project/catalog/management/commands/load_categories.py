from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Category, SubCategory, SubSubCategory


class Command(BaseCommand):
    help = 'Загружает категории и подкатегории в базу данных'

    def handle(self, *args, **kwargs):
        def check_utf8(value):
            """Проверяет строку на корректность кодировки UTF-8."""
            try:
                value.encode('utf-8').decode('utf-8')
                return True
            except UnicodeDecodeError:
                return False

        def create_categories(categories):
            """Создает основные категории."""
            category_objects = {}
            for name in categories:
                if not check_utf8(name):
                    self.stdout.write(self.style.WARNING(
                        f"Некорректная строка: {name}"))
                category_objects[name], created = Category.objects.get_or_create(name=name)
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Создана категория: {name}"))
                else:
                    self.stdout.write(f"Категория уже существует: {name}")
            return category_objects

        def create_subcategories(category_objects, subcategories):
            """Создает подкатегории."""
            subcategory_objects = {}
            for cat_name, sub_names in subcategories.items():
                category = category_objects.get(cat_name)
                if not category:
                    self.stderr.write(f"Категория '{cat_name}' не найдена!")
                    continue
                for sub_name in sub_names:
                    if not check_utf8(sub_name):
                        self.stdout.write(self.style.WARNING(
                            f"Некорректная строка: {sub_name}"))
                    subcategory_objects[sub_name], created = SubCategory.objects.get_or_create(
                        name=sub_name, category=category
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Создана подкатегория: {sub_name}"))
                    else:
                        self.stdout.write(f"Подкатегория уже существует: {sub_name}")
            return subcategory_objects

        def create_subsubcategories(subcategory_objects, subsubcategories):
            """Создает подподкатегории."""
            for sub_name, subsub_names in subsubcategories.items():
                subcategory = subcategory_objects.get(sub_name)
                if not subcategory:
                    self.stderr.write(f"Подкатегория '{sub_name}' не найдена!")
                    continue
                for subsub_name in subsub_names:
                    if not check_utf8(subsub_name):
                        self.stdout.write(self.style.WARNING(
                            f"Некорректная строка: {subsub_name}"))
                    _, created = SubSubCategory.objects.get_or_create(
                        name=subsub_name, subcategory=subcategory
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(
                            f"Создана подподкатегория: {subsub_name}"))
                    else:
                        self.stdout.write(
                            f"Подподкатегория уже существует: {subsub_name}")

        try:
            with transaction.atomic():
                self.stdout.write(self.style.SUCCESS("Начало загрузки категорий"))

                # Основные категории
                categories = [
                    "Электроника",
                    "Компьютеры",
                    "Бытовая техника",
                    "Красота и Здоровье",
                    "Одежда и Аксессуары",
                    "Детские товары",
                    "Спорт и Отдых",
                    "Автотовары",
                    "Дом Сад Ремонт",
                    "Посуда",
                    "Книги"
                ]
                category_objects = create_categories(categories)

                # Подкатегории
                subcategories = {
                    "Электроника": [
                        "Мобильные телефоны",
                        "Планшеты и Букридеры",
                        "Аксессуары и Гаджеты",
                        "Телефоны для дома и офиса",
                        "ТВ, Аудио, Видео",
                        "Фото и Видео",
                        "Музыкальные инструменты"
                    ],
                    "Компьютеры": [
                        "Ноутбуки и Компьютеры",
                        "Периферия",
                        "Защита питания",
                        "Оргтехника",
                        "Сетевое оборудование",
                        "Софт",
                        "Комплектующие"
                    ],
                    "Бытовая техника": [
                        "Мелкая бытовая техника",
                        "Крупная бытовая техника",
                        "Климатическая техника",
                        "Техника для дома"
                    ],
                    "Красота и Здоровье": [
                        "Товары для красоты",
                        "Парфюмерия",
                        "Медицинская техника"
                    ],
                    "Одежда и Аксессуары": [
                        "Часы",
                        "Аксессуары",
                        "Сумки",
                        "Мужская одежда",
                        "Детская одежда"
                    ],
                    "Детские товары": [
                        "Детский спорт",
                        "Прогулки и путешествия",
                        "Гигиена",
                        "Кормление",
                        "Игрушки",
                        "Коляски",
                        "Безопасность и Здоровье",
                        "Детская комната",
                        "Мамам"
                    ],
                    "Спорт и Отдых": [
                        "Туризм",
                        "Лыжи и Сноуборд",
                        "Тренажеры",
                        "Велосипеды",
                        "Спортивное питание",
                        "Спортивный инвентарь"
                    ],
                    "Автотовары": [
                        "Автомобильная акустика",
                        "Автоэлектроника",
                        "Шины",
                        "Автозапчасти",
                        "Автомобильные аксессуары"
                    ],
                    "Дом Сад Ремонт": [
                        "Сантехника",
                        "Хозяйственные товары",
                        "Текстиль",
                        "Мебель",
                        "Дача и Сад",
                        "Освещение",
                        "Садовая техника",
                        "Силовая техника",
                        "Инструмент",
                        "Интерьер и Декор"
                    ],
                    "Посуда": [
                        "Приготовление пищи",
                        "Хранение продуктов",
                        "Приготовление чая, кофе, напитков",
                        "Сервировка стола"
                    ]
                }
                subcategory_objects = create_subcategories(category_objects,
                                                           subcategories)

                # Подподкатегории
                subsubcategories = {
                    #Электроника
                    "Планшеты и Букридеры": [
                        "Электронные книги",
                        "Планшеты",
                        "Графические планшеты"
                    ],
                    "Аксессуары и Гаджеты": [
                        "Батарейки, аккумуляторы и зарядные устройства",
                        "Беспроводные наушники и Bluetooth гарнитуры",
                        "Виртуальная реальность",
                        "Внешние аккумуляторы (Power bank)",
                        "Карты памяти (флешки)",
                        "Наушники для телефона",
                        "Селфи-палки (моноподы)"
                    ],
                    "Телефоны для дома и офиса": [
                        "Проводные телефоны",
                        "Радиотелефоны"
                    ],
                    "ТВ, Аудио, Видео": [
                        "Диктофоны",
                        "Доски интерактивные",
                        "Колонки портативные",
                        "Кронштейны и стойки для телевизоров",
                        "Медиа плееры",
                        "Радиобудильники и Приемники",
                        "Ресиверы-тюнеры DVB-T2 (цифровое ТВ)",
                        "Телевизоры",
                        "Экраны для проектора",
                        "Проекторы",
                        "Игровые приставки",
                        "DVD и Blu-ray плееры",
                        "Игры для приставок",
                        "Домашние кинотеатры",
                        "Магнитолы и Акустические системы"
                    ],
                    "Фото и Видео": [
                        "Видеокамеры и Экшн камеры",
                        "Вспышки",
                        "Дроны(квадрокоптеры)",
                        "Микроскопы",
                        "Объективы",
                        "Сумки и чехлы для фотоаппаратов",
                        "Фотоаппараты"
                    ],
                    "Музыкальные инструменты": [
                        "Гитары",
                        "Губные гармошки",
                        "Микрофоны",
                        "Синтезаторы"
                    ]
                }
                create_subsubcategories(subcategory_objects, subsubcategories)

                self.stdout.write(self.style.SUCCESS(
                    "Категории и подкатегории были успешно загружены."
                ))

        except UnicodeDecodeError as e:
            self.stderr.write(
                f"UnicodeDecodeError: {e}, строка {e.__traceback__.tb_lineno}")
        except Exception as e:
            self.stderr.write(
                f"Ошибка: {e}, строка {e.__traceback__.tb_lineno}")

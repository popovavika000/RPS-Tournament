# RPS-Tournament
игра в камень-ножницы-бумага
# Проект "Камень, Ножницы, Бумага"

## О чем мой проект?

В этом проекте создаем разных агентов для игры "Камень, Ножницы, Бумага". Каждый агент — программа, решающая, какой ход сделать.

## Структура

1. **Создали папки для агентов и вспомогательных функций**:
   - В папке `agents` хранятся агенты
   - В папке `utils` хранятся вспомогательные функции, которые считают очки в игре

2. **Написали агентов**:
   - Мы создали несколько агентов с разными стратегиями:
     - **rock**: всегда выбирает "Камень".
     - **paper**: всегда выбирает "Бумагу".
     - **scissors**: всегда выбирает "Ножницы".
     - **random**: выбирает случайное действие.
     - **copy**: копирует последний ход противника.
     - И другие агенты с иными интересными стратегиями.

3. **Добавили функцию для подсчета очков**:
   - В `get_score.py` мы написали функцию, которая определяет, кто выиграл, а кто проиграл в нашей игре.

4. **Создали основной файл**:
   - В файле `main.py` мы запускаем игру и проверяем, как наши агенты соревнуются друг с другом.

5. **Подготовили проект к запуску**:
   - Мы добавили файл `requirements.txt`, чтобы указать необходимые библиотеки для работы.

## Как запустить проект?

1. Установить библиотеку `kaggle_environments`.
2. Запустите файл `main.py`, чтобы увидеть, как наши агенты играют друг с другом.

## Заключение

Мы сделали интересный проект, где разные стратегии игры соперничают друг с другом. Мне понравилось задание!

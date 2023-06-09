# API_YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

## Описание

Проект отзывов YaMDb в рамках обучения на Яндекс Практикум. Благодаря этому проекту можно оставлять отзывы на произведения в различных категориях (например -книги, фильмы, музыка). Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и оценивают произведение по шкале от 1 до 10. Исходя из среднего значения оценое формируется рейтинг произведения. На одно произведение уникальный пользователь может оставить только один отзыв.

## Характеристики

Аутентификация по JWT-токену

Работает со всеми модулями социальной YaMDb: произведениями, отзывами, категориями, жанрами, комментариями.

Получение списка всех категорий, добавление новой категории, удаление категории.

Получение списка всех жанров, добавление жанра, удаление жанра.

Получение списка всех произведений, добавление произведения, удаление произведения.

Получение информации о произведении, частичное обновление информации о произведении.

Получение списка всех отзывов, добавление нового отзыва, полуение отзыва по id.

Частичное обновление отзыва по id, удаление отзыва по id.

Получение списка всех комментариев к отзыву, добавление комментария к отзыву, получение комментария к отзыву.

Частичное обновление комментария к отзыву, удаление комментария к отзыву.

Получение списка всех пользователей, добавление пользователя, получение пользователя по username.

Изменение данных пользователя по username, удаление пользователя по username.

Получение данных своей учетной записи, Изменение данных своей учетной записи.

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

## Стек технологий

- Django REST Framework v.3.12.4- написание проекта на Python v.3.11.0+
- Simple JWT(djangorestframework-simplejwt v.5.2.2) - работа с JWT-токеном

## Подготовка ПО

### Инструкция для Windows

Установите программное обеспечение: скачайте установочные файлы и запустите их.

Python: <https://python.org/downloads/>

Visual Studio Code: <https://visualstudio.com/download/>

Git: <https://git-scm.com/download/win/>

### Инструкция для Linux (Ubuntu)

Запустите программу Терминал.

1. Сперва установите Python, для этого в терминале выполните команду. Перед установкой терминал попросит вас ввести пароль администратора — сделайте это.

```bash
sudo apt-get install python 
```

2. По такой же схеме установите Git

```bash
sudo apt-get install git 
```

3. Чтобы установить редактор вам понадобится менеджер пакетов `snap`. Установите его командой

```bash
sudo apt install snap 
```

4. Устанавливаем редактор Visual Studio Code из дополнительного набора пакетов:

```bash
sudo snap install code --classic 
```

5. После того, как всё скачается и установится, вы сможете запустить Visual Studio Code командой `code` в терминале.

## Запуск проекта

1. После установки ПО откройте VSCode и откройте терминал (Терминал - Создать терминал). Внизу спаправа нажмите `+` и выберите Git Bash (если предпочитаете пользоваться стандартной командной строкой powershell, то используйте их).

2. В командной строке войдите в директорию, где планируете развернуть проект. Например:

```bash
cd /c/Dev/
```

3. Необходимо склонировать репозитарий проекта:

```bash
git clone https://github.com/Ampolirosinvest/api_yamdb.git
```

Теперь ваш проект будет храниться в дериктории например: `/c/Dev/api_yamdb`
Все дальнейшние операции проводятся в дериктории вашего проекта.

1. Установить и активировать виртуальное окружение:

```bash
python -m venv venv
sourse venv/Scripts/activate
```

5. Установить необходимые зависимости:

```bash
pip install -r requirements.txt
```

6. Выполните миграции(нужно перейти в директорию, где лежит файл manage.py, например -`/c/Dev/api_yamdb/api_yamdb`):

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Создайте суперпользователя:

```bash
python manage.py createsuperuser
```

8. Запустите сервер:

```bash
python manage.py runserver
```

Ваш проект запустился на ```http://127.0.0.1:8000/```

## Документация к проекту

----------

Документация для API после установки доступна по адресу

```http://127.0.0.1:8000/redoc/```

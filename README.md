# show_weather
Описание
Сайт предоставляет информацию о прогнозе погоды на ближайшее время.
(![image](https://github.com/user-attachments/assets/027b689d-fab8-44c9-b845-f76be723e88f)
![image](https://github.com/user-attachments/assets/24260d6b-29c1-485e-8c53-4bba6acdf1ce)
## Подробное описание проекта и его функций.
### Технологии
- Python 3.10.12
- Django 5.0.7
- API для данных о городах: Geonames
- API для прогноза погоды: Open-Meteo

### Установка и настройка
1. Для изоляции зависимостей проекта рекомендуется использовать виртуальное окружение.
```bash
python -m venv venv
```
   Запуск виртуального окружения:

Windows:
```bash
.\venv\Scripts\activate
```
Linux\macOS:
```bash
source venv/bin/activate
```
2. Клонируйте проект:
```bash
git clone https://github.com/AlnBnd/show_weather.git
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Настройте базу данных и выполните миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```
  Эта команда создаст необходимые таблицы в базе данных согласно моделям приложений Django.
  
5. Запустите сервер разработки:
```bash
python manage.py runserver
```
### Основные шаги при создании проекта
1. Настройки проекта
   - Установка библиотек
   - Создание приложения
     ```
     django-admin startapp weather
     ```
   - Добавление weather в INSTALLED_APPS в settings.py
2. Создание модели Weather для хранения городов в БД. Модель прописана в файле weather/models.py
3. Создание формы для ввода города в weather/forms.py
4. Создание представления для обработки ввода (получение координат города) и получения информации о погоде в файле weather/views.py
5. Написание тестов. Тесты включают в себя тестирования представления для проверки корректной обработки GET и POST запросов.

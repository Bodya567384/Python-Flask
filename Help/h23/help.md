# Заняття 23

## SQLAlchemy 

#### Частина 1  

---

**[Flask-SQLAqlalchemy](https://flask-sqlalchemy.readthedocs.io/en/3.1.x/)** - це 
розширення для Flask, яке додає підтримку SQLAlchemy до вашої програми. 
Воно спрощує використання SQLAlchemy з Flask шляхом налаштування спільних об'єктів 
і шаблонів для використання цих об'єктів, таких як сеанс, прив'язаний до кожного веб-запиту, моделей і рушіїв.


### Встановлення:

Щоб додати підтримку SQLAlchemy у ваш Flask-додаток, виконайте наступну команду для встановлення необхідних пакетів:

```bash
pip install flask-sqlalchemy
```

### Налаштування Flask для роботи з SQLAlchemy

1. **Імпорт та ініціалізація SQLAlchemy у Flask-додатку:**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'   # URI бази даних
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # Вимкнути відстеження змін

db = SQLAlchemy(app)   # Ініціалізація SQLAlchemy
```

2. **Пояснення параметрів конфігурації:**
   - `SQLALCHEMY_DATABASE_URI`: URI бази даних (для SQLite, MySQL, PostgreSQL та інших СУБД).
   - `SQLALCHEMY_TRACK_MODIFICATIONS`: вимкнення додаткового використання пам'яті для відстеження об'єктів.

---

### Створення моделей

Моделі в SQLAlchemy — це класи Python, які представляють таблиці бази даних. Атрибути класу представляють колонки таблиці.

##### Створення моделі:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

#### Основні типи колонок:
- `db.Integer`: цілі числа.
- `db.String(size)`: рядки із зазначенням максимальної довжини.
- `db.Boolean`: булеві значення (True/False).
- `db.DateTime`: дата і час.

#### Ключові параметри для колонок:
- `primary_key=True`: задає колонку як первинний ключ.
- `unique=True`: забезпечує унікальність значення.
- `nullable=False`: забороняє `NULL` значення.

---

### Створення таблиць

Після створення моделей потрібно створити таблиці в базі даних на основі цих моделей.

```python
with app.app_context():
    db.create_all()   # Створює всі таблиці у базі даних
```

---

### CRUD-операції

**CRUD** — це акронім для Create (створити), Read (читати), Update (оновлювати), Delete (видаляти). SQLAlchemy надає прості методи для виконання цих операцій.

#### Створення (Create)

Для додавання нового запису в базу даних потрібно створити об'єкт моделі та додати його до сесії.

```python
new_user = User(username='alex', email='alex@example.com')
db.session.add(new_user)  # Додає об'єкт у сесію
db.session.commit()  # Застосовує зміни до бази даних
```

#### Читання (Read)

Для отримання даних використовуйте методи запитів SQLAlchemy.

- Отримати всі записи:

```python
users = User.query.all()  # Повертає список всіх користувачів
```

- Отримати запис за ID:

```python
user = User.query.get(1)  # Повертає користувача з id=1
```

- Фільтрування:

```python
user = User.query.filter_by(username='alex').first()  # Повертає першого користувача з username='alex'
```

#### Оновлення (Update)

Оновлення виконується шляхом зміни атрибутів об'єкта та застосування змін до бази даних.

```python
user = User.query.get(1)
user.email = 'newemail@example.com'
db.session.commit()  # Застосовує зміни
```

#### Видалення (Delete)

Для видалення запису з бази даних використовуйте метод `delete`.

```python
user = User.query.get(1)
db.session.delete(user)  # Видаляє користувача з бази даних
db.session.commit()  # Підтверджує видалення
```

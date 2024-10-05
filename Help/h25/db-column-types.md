#### https://flask-sqlalchemy.readthedocs.io/en/3.1.x/# 

#### https://www.sqlalchemy.org/

--- 

Flask-SQLAlchemy використовуються різні типи даних для визначення полів таблиць, 
 які дозволяють зберігати різні види інформації. Вони відповідають типам даних, 
 що використовуються в базах даних SQL.


### Основні типи даних

1. **`Integer`**
   - Цілі числа.
   - Приклад: `db.Column(db.Integer)`

2. **`String`**
   - Рядок тексту фіксованої довжини.
   - Аргументом вказується максимальна довжина.
   - Приклад: `db.Column(db.String(150))`

3. **`Text`**
   - Великий блок тексту (без обмеження довжини).
   - Приклад: `db.Column(db.Text)`

4. **`Float`**
   - Числа з плаваючою комою.
   - Приклад: `db.Column(db.Float)`

5. **`Boolean`**
   - Логічний тип даних: `True` або `False`.
   - Приклад: `db.Column(db.Boolean)`

6. **`Date`**
   - Дата (рік, місяць, день).
   - Приклад: `db.Column(db.Date)`
   - Приклад з використанням Python:
     ```python
     from datetime import date
     user_date = date.today()
     ```

7. **`Time`**
   - Час (години, хвилини, секунди).
   - Приклад: `db.Column(db.Time)`

8. **`DateTime`**
   - Дата і час.
   - Приклад: `db.Column(db.DateTime)`
   - Приклад з використанням Python:
     ```python
     from datetime import datetime
     current_time = datetime.utcnow()
     ```

9. **`LargeBinary`**
   - Великий бінарний об'єкт (зазвичай використовується для зберігання файлів або зображень).
   - Приклад: `db.Column(db.LargeBinary)`

### Додаткові типи даних

1. **`Decimal`**
   - Числа з фіксованою кількістю десяткових знаків.
   - Аргументи: загальна кількість цифр і кількість цифр після коми.
   - Приклад: `db.Column(db.Numeric(precision=10, scale=2))`

2. **`Enum`**
   - Поле з можливістю вибору одного з кількох варіантів.
   - Приклад: `db.Column(db.Enum('small', 'medium', 'large'))`

3. **`JSON`**
   - Поле для зберігання даних у форматі JSON.
   - Приклад: `db.Column(db.JSON)`

4. **`PickleType`**
   - Для зберігання Python-об'єктів у вигляді серіалізованих даних (використовує модуль `pickle`).
   - Приклад: `db.Column(db.PickleType)`

5. **`Interval`**
   - Поле для зберігання тривалості часу.
   - Приклад: `db.Column(db.Interval)`

### Спеціальні аргументи для колонок

- **`primary_key=True`** — вказує на те, що поле є первинним ключем.
  ```python
  id = db.Column(db.Integer, primary_key=True)
  ```

- **`nullable=False`** — означає, що поле не може бути `NULL`.
  ```python
  username = db.Column(db.String(80), nullable=False)
  ```

- **`unique=True`** — вказує на те, що значення в полі мають бути унікальними.
  ```python
  email = db.Column(db.String(120), unique=True)
  ```

- **`default=value`** — встановлює значення за замовчуванням для поля.
  ```python
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  ```

### Приклад моделі з різними типами даних
```python
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.LargeBinary)
    tags = db.Column(db.JSON)
```

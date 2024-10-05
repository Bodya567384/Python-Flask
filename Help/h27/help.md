# Заняття 27

## Flask Sessions

---

#### Імпорт Session


У Flask сесії використовуються для зберігання даних між запитами на рівні користувача. 
Це може бути корисно для авторизації, відстеження стану користувача або зберігання тимчасової інформації. 
За замовчуванням Flask зберігає сесії у клієнтських cookies, шифруючи їх за допомогою секретного ключа.

```python
from flask import session
```

#### Налаштування секретного ключа

Flask використовує секретний ключ для підпису сесійних файлів cookie. 

```python
# Секретний ключ для шифрування сесії
app.config['SECRET_KEY'] = 'ваш_секретний_ключ'
# або
# app.secret_key = 'ваш_секретний_ключ'
```

#### Збереження даних у сесії

Щоб зберегти дані у сесії, використовуйте об'єкт `session`. Наприклад, збережемо ім'я користувача:

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Записуємо ім'я користувача у сесію
        session['username'] = request.form['username']        
        return redirect(url_for('index'))    
    return render_template('login.html')
```

#### Доступ до даних сесії

Щоб отримати доступ до даних, збережених у сесії, також використовуйте об'єкт `session`:

```python
@app.route('/profile')
def profile():
    username = session.get('username')    
    if username:
        return f'User: {username}'    
    return 'Not logged in'
```

```python
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username}'
    return 'You are not logged in'
```

### Очищення сесії

Для видалення даних із сесії можна використовувати метод pop(), або можна очистити всю сесію через session.clear().

```python
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
```

### Постійні сесії та таймаути

За замовчуванням сесії у Flask тривають до закриття браузера. 
Якщо ви хочете створити постійну сесію з певним таймаутом, налаштуйте атрибут `permanent` 
та конфігурацію `permanent_session_lifetime`:

```python
from datetime import timedelta

session.permanent = True  # робимо сесію перманентною
app.permanent_session_lifetime = timedelta(minutes=30) # сесія триває 30 хвилин

# app.permanent_session_lifetime = timedelta(days=7)  # сесія триває 7 днів
```



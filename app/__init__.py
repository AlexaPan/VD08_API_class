from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

from app import routes  # подключаем маршруты
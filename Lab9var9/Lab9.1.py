from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='templates')

# Настройка базы данных
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "instance", "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Обработка очистки БД (должно быть ДО обработки POST)
    if request.method == 'GET' and 'clear' in request.args:
        db.session.query(Component).delete()
        db.session.commit()
        return redirect(url_for('index'))  # Важно: редирект после очистки

    # Обработка добавления (POST)
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        db.session.add(Component(name=name, price=price))
        db.session.commit()
        return redirect(url_for('index'))  # Редирект после добавления

    # Получение данных для отображения
    components = Component.query.all()
    total = sum(c.price for c in components)
    return render_template('index.html', components=components, total=total)


if __name__ == '__main__':
    # Создаем папки и БД
    if not os.path.exists(os.path.join(base_dir, 'instance')):
        os.makedirs(os.path.join(base_dir, 'instance'))

    with app.app_context():
        db.create_all()

    app.run(debug=True)
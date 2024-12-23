from flask import Flask, request, render_template_string
import sqlite3
import json
import os

app = Flask(__name__)

# Папка для сохранения загруженных JSON-файлов
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Подключение к базе данных и создание таблицы
def init_db():
    conn = sqlite3.connect("galactic_missions.db")
    cursor = conn.cursor()

    # Создание таблицы для космических миссий
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CosmicMissions (
        mission_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mission_name TEXT NOT NULL,
        launch_date TEXT NOT NULL,
        mission_status TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Главная страница с космическим стилем
@app.route('/')
def home():
    # Вся HTML-разметка в стиле «космоса»
    form_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Космический центр управления</title>
        <style>
            body {
                font-family: 'Trebuchet MS', sans-serif;
                background-color: #0b0b1e;
                color: #e8e8f8;
                margin: 0;
                padding: 0;
                background-image: url('https://www.transparenttextures.com/patterns/stardust.png');
            }
            h1, h2 {
                text-align: center;
                color: #ffa07a;
                margin-top: 30px;
            }
            form, a {
                display: block;
                margin: 20px auto;
                text-align: center;
                max-width: 400px;
            }
            input[type="text"], input[type="file"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #555;
                border-radius: 5px;
                background-color: #2c2c54;
                color: #e8e8f8;
            }
            input[type="submit"] {
                background-color: #ffa07a;
                color: white;
                border: none;
                padding: 10px;
                cursor: pointer;
                border-radius: 5px;
            }
            input[type="submit"]:hover {
                background-color: #ff7f50;
            }
            .link-container {
                text-align: center;
            }
            .cosmic-link {
                color: #ffa07a;
                text-decoration: none;
                font-weight: bold;
            }
            .cosmic-link:hover {
                color: #ff4500;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: #3a3a5f;
                margin: 10px;
                padding: 10px;
                border-radius: 5px;
                color: #ffd700;
                font-size: 1rem;
            }
        </style>
    </head>
    <body>
        <h1>Галактический центр управления</h1>
        <h2>Добавить новую миссию</h2>
        <form action="/add_mission" method="post">
            <label for="mission_name">Название миссии:</label>
            <input type="text" id="mission_name" name="mission_name" placeholder="Введите название миссии"><br><br>
            <label for="launch_date">Дата запуска:</label>
            <input type="text" id="launch_date" name="launch_date" placeholder="YYYY-MM-DD"><br><br>
            <label for="mission_status">Статус миссии:</label>
            <input type="text" id="mission_status" name="mission_status" placeholder="Статус"><br><br>
            <input type="submit" value="Запустить миссию">
        </form>

        <h2>Управление миссиями</h2>
        <div class="link-container">
            <a class="cosmic-link" href="/view_missions">Просмотреть все миссии</a><br><br>
            <a class="cosmic-link" href="/export_missions">Экспортировать миссии в JSON</a><br><br>
        </div>

        <h2>Загрузка данных</h2>
        <form action="/import_missions" method="post" enctype="multipart/form-data">
            <label for="json_file">Импорт миссий из JSON-файла:</label>
            <input type="file" id="json_file" name="json_file"><br><br>
            <input type="submit" value="Импортировать миссии">
        </form>
    </body>
    </html>
    """
    return render_template_string(form_html)

# Маршрут для добавления новой миссии
@app.route('/add_mission', methods=['POST'])
def add_mission():
    # Получаем данные из формы
    mission_name = request.form['mission_name']
    launch_date = request.form['launch_date']
    mission_status = request.form['mission_status']

    # Вставляем новую миссию в базу данных
    conn = sqlite3.connect("galactic_missions.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO CosmicMissions (mission_name, launch_date, mission_status)
        VALUES (?, ?, ?)
    """, (mission_name, launch_date, mission_status))
    conn.commit()
    conn.close()

    return "Миссия успешно добавлена! <a href='/'>Вернуться на главную</a>"

# Маршрут для просмотра всех миссий
@app.route('/view_missions')
def view_missions():
    conn = sqlite3.connect("galactic_missions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CosmicMissions")
    missions = cursor.fetchall()
    conn.close()

    # Формируем HTML для отображения списка миссий
    missions_html = """
    <h1>Список галактических миссий</h1>
    <ul>
    """
    for mission in missions:
        # mission = (mission_id, mission_name, launch_date, mission_status)
        missions_html += (
            f"<li>"
            f"ID: {mission[0]}, Название: {mission[1]}, "
            f"Дата запуска: {mission[2]}, Статус: {mission[3]}"
            f"</li>"
        )
    missions_html += "</ul>"
    missions_html += '<a href="/">Вернуться на главную</a>'
    return missions_html

# Маршрут для экспорта миссий в JSON
@app.route('/export_missions')
def export_missions():
    conn = sqlite3.connect("galactic_missions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CosmicMissions")
    missions = cursor.fetchall()
    conn.close()

    # Сохраняем данные в файл missions.json
    with open("missions.json", "w", encoding='utf-8') as file:
        # missions — список кортежей [(mission_id, mission_name, launch_date, mission_status), ...]
        json.dump(missions, file, ensure_ascii=False, indent=2)

    return "Миссии экспортированы в файл missions.json! <a href='/'>Вернуться на главную</a>"

# Маршрут для импорта миссий из JSON
@app.route('/import_missions', methods=['POST'])
def import_missions():
    # Проверяем, что файл передан
    if 'json_file' not in request.files:
        return "Файл не найден! <a href='/'>Вернуться на главную</a>"

    file = request.files['json_file']
    if file.filename == '':
        return "Файл не выбран! <a href='/'>Вернуться на главную</a>"

    # Проверяем, что это .json
    if file and file.filename.endswith('.json'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            # Предполагаем, что в JSON-файле данные в виде списка списков:
            # [
            #   [mission_id, mission_name, launch_date, mission_status],
            #   ...
            # ]
            missions_raw = json.load(f)

        # Если mission_id генерируется автоматически, игнорируем mission_id при вставке
        missions_data = []
        for item in missions_raw:
            # item = [mission_id, mission_name, launch_date, mission_status]
            mission_name, launch_date, mission_status = item[1], item[2], item[3]
            missions_data.append((mission_name, launch_date, mission_status))

        conn = sqlite3.connect("galactic_missions.db")
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO CosmicMissions (mission_name, launch_date, mission_status)
            VALUES (?, ?, ?)
        """, missions_data)
        conn.commit()
        conn.close()

        return "Миссии успешно импортированы из JSON! <a href='/'>Вернуться на главную</a>"

    return "Неверный формат файла! Нужно выбрать файл .json. <a href='/'>Вернуться на главную</a>"

# Инициализация базы данных при запуске приложения
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

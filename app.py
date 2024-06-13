from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

# Налаштування для підключення до бази даних
db_config = {
    'user': 'root',
    'password': '12345',
    'host': 'localhost',
    'database': 'mysql'
}

@app.route('/index.html', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['user-name']
        user_phone = request.form['user-phone']
        user_mail = request.form['user-mail']
        user_comment = request.form['user-comment']
        

        # Підключення до бази даних та вставка даних
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = ("INSERT INTO pomogite "
                 "(name, phone, email, comment) "
                 "VALUES (%s, %s, %s, %s)")
        cursor.execute(query, (user_name, user_phone, user_mail, user_comment))
        cnx.commit()
        cursor.close()
        cnx.close()

    return render_template('index.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)
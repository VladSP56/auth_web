from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    user_data = {
        'name': 'Владимир Пак',  # Предварительно загруженные данные
        'email': 'parkvls@gmail.com',
    }

    if request.method == 'POST':
        # Получение данных из формы
        user_data['name'] = request.form.get('name')
        user_data['email'] = request.form.get('email')
        user_data['password'] = request.form.get('password')  # Для целей примера, пароль не сохраняется

    return render_template('edit_profile.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
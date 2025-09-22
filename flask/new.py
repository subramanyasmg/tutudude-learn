from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello subramanya!</h1>'

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/confirmation', methods=['POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        phone = request.form['phone']
        return render_template('confirmation.html', name=name, city=city, phone=phone)

if __name__ == '__main__':
    # automatically reloads the page
    app.run(debug=True)

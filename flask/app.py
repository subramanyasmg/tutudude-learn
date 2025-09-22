from flask import Flask, render_template
import os
app = Flask(__name__)
picfolder = os.path.join(os.getcwd(), 'static')

app.config['UPLOAD_FOLDER'] = picfolder
@app.route('/')
def index():
    pic =  os.path.join(app.config['UPLOAD_FOLDER'], 'hero-banner.jpg')
    return render_template('home.html', uer_image=pic)


@app.route('/second')
def second():
    return render_template('second.html')

if __name__ == '__main__':
    app.run(debug=True)
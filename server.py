from flask import Flask, render_template,redirect
from flask import request
from forms import *
from generator import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'levitation'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    if form.is_submitted():
        name2 = request.form['name']
        age2 = request.form['age']
        passion2 = request.form['passion']
        master_password2 = request.form['master_password']
        pass_new2 = generate(name2, age2, passion2)
        return render_template('output.html', nameh=pass_new2)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()

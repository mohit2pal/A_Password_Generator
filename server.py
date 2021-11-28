from flask import Flask, render_template,redirect
from flask import request
from forms import *
from generator import *
from checker import *
from shuffle import *
from creat import *

x_choice = "qwertyuioplkjhgfdazxvbnm,./;;'['']][[>:>?{}{}\[-0909876531@!@#$%^*()--==9&^&%$@!!QWE45TVTBUM<O>??|\(*^7t^&55RE$%56954655494654987*/*+26!###^&)"
y_choice = "QWERTYUIOPASDFGHJZXCVBNMqwertyuiopasdfghklzcbnm1213456789064fds64r645454e65454466584674656634846538543454345454356'.;;.]/';303-923928782736333+*/3-3-3+2362+329+3/2*3/2+38+2398"
z_choice = "12039120938210948214294872198472140172!*(#&!*&!&#^!&#!#!(#^!)#)!#!)#^!#6484654546465468548498*/***/**/*/*/*/*/-+++--*-/-/*-/_+_{}{|:>{)_(*&^%%#@"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    if form.is_submitted():
        name2 = request.form['name']
        age2 = request.form['age']
        passion2 = request.form['passion']
        master_password2 = request.form['master_password']
        pass_new2 = generate(name2, age2, passion2, x_choice, y_choice, z_choice)
        check_return = fid(pass_new2)
        while(check_return == 'found'):
            x_choice2 = shuffl(x_choice)
            y_choice2 = shuffl(y_choice)
            z_choice2 = shuffl(z_choice)
            pass_new2 = generate(name2, age2, passion2, x_choice2, y_choice2, z_choice2)
            check_return = fid(pass_new2)
            if(check_return == 'woohoo'):
                crat(x_choice2, y_choice2, z_choice2)
        if(check_return == 'woohoo'):
            print('Not Found')
        return render_template('output.html', nameh=pass_new2)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()

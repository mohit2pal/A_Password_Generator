from flask import Flask, render_template
from flask import request
from forms import *
from generator import *
from checker import *
from shuffle import *
from creat import *
from master_pass import *

x_choice = "qwertyuioplkjhgfdazxvbnm,./;;'['']][[>:>?{}{}\[-0909876531@!@#$%^*()--==9&^&%$@!!QWE45TVTBUM<O>??|\(*^7t^&55RE$%56954655494654987*/*+26!###^&)"
y_choice = "QWERTYUIOPASDFGHJZXCVBNMqwertyuiopasdfghklzcbnm1213456789064fds64r645454e65454466584674656634846538543454345454356'.;;.]/';303-923928782736333+*/3-3-3+2362+329+3/2*3/2+38+2398"
z_choice = "12039120938210948214294872198472140172!*(#&!*&!&#^!&#!#!(#^!)#)!#!)#^!#6484654546465468548498*/***/**/*/*/*/*/-+++--*-/-/*-/_+_{}{|:>{)_(*&^%%#@"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def gene():
    form = SignUpForm()
    if form.is_submitted():
        name2 = request.form['name']
        age2 = request.form['age']
        passion2 = request.form['passion']
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
            mast = master()
            pass_new2 = pass_new2 + mast
        return render_template('output.html', nameh=pass_new2, masth = mast)
    return render_template('index.html', form=form)

@app.route('/remember', methods=['GET', "POST"])
def rember():
    form = SignUpForm()
    if form.is_submitted():
        name2 = request.form['name']
        age2 = request.form['age']
        passion2 = request.form['passion']
        master_password2 = request.form['master_password']
        master = master_password2[2:4]
        m = int(master)
        m1= (m*3)-2
        m2= (m*3)-1
        m3= (m*3)
        t = 0
        f = open('1.txt', 'r')
        for x in f:
            if(t == m1):
                x_choice2 = x
            elif(t == m2):
                y_choice2 = x
            elif( t == m3):
                z_choice2 = x
            t+=1
        f.close()
        pass_new2 = generate(name2, age2, passion2, x_choice2, y_choice2, z_choice2)
        pass_new2 = pass_new2 + master_password2
        return render_template('output2.html', nameh=pass_new2, masth= master_password2)
    return render_template('index2.html', form=form)

if __name__ == '__main__':
    app.run()

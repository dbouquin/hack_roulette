from flask import Flask
from flask import request
from flask import Flask, render_template, redirect, url_for, request

import glob
import random

app = Flask(__name__)

all_hacks = glob.glob('hacks-collector/dotastro*/*yml')

@app.route('/')
def start():
    return render_template('hackroulette.html') 


@app.route('/hack/', methods=['GET', 'POST'])
@app.route('/hack/<number>', methods=['GET', 'POST'])
def hack(): #old=False, dead=False, length=24, people=4, number=1):
    i = random.randint(0, len(all_hacks)-1)
    hack_str = open(all_hacks[i]).read()
    return render_template('hack.html', hack_str=hack_str)

# route for handling the login page logic
#@app.route('/', methods=['GET', 'POST'])
#def login():
    #error = None
    #if request.method == 'POST':
        #if request.form['password'] != 'tiger':
            #error = 'Invalid Credentials. Please try again. 5 letters, ferocious cuddle cat'
        #else:
            #return redirect(url_for('start'))
    #return render_template('login.html', error=error)

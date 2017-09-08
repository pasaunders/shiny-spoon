from flask import Flask, render_template, request, session, redirect, url_for
from random import choice, randint


app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process():
    visit = request.form['building']
    if visit is 'farm':
        income = randint(10, 20)
        session.gold += income
    if visit is 'cave':
        income = randint(5, 10)
        session.gold += income
    if visit is 'house':
        income = randint(2, 5)
        session.gold += income
    if visit is 'casino':
        income = randint(-50, 50)
        session.gold += income
    
    session.activities.append('You visited the {} and made {} gold.'.format(visit, income))
    return redirect(url_for('index'))
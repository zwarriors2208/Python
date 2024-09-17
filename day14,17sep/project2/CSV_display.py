from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

dF = Flask(__name__)
dF.secret_key = 'secret'

@dF.route('/')
def home():
    return render_template('dF.html')

@dF.route('/csvx', methods=['POST'])
def C1():
    abc = request.form['path']
    df = pd.read_csv(abc)
    x = df.describe()
    return render_template('csv1.html', csv1 = x)


if __name__ == '__main__':
    dF.run(debug=True)
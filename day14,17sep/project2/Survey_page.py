from flask import Flask, render_template,request, redirect, url_for

survey=Flask(__name__)
@survey.route('/')
def home():
    return render_template('home2.html')

@survey.route('/survey')
def surveys():
    return render_template('survey.html')

@survey.route('/results', methods=['POST'])
def results():
    one=request.form['names']
    two=request.form['age']
    three=request.form['hobby']
    four=request.form['gender']
    five=request.form['graduate']

    return (f"The answer to first question is: {one}<br>"
            f"The answer to second question is: {two}<br>"
            f"The answer to third question is: {three}<br>"
            f"The answer to fourth question is: {four}<br>"
            f"The answer to fifth question is: {five}")



if __name__ == '__main__':
    survey.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
appAge=Flask(__name__)
@appAge.route("/")
def home():
    return render_template('home.html')

    # return redirect(url_for('check_age'))


@appAge.route("/check_age")
def check_age():
    return render_template('age.html')

@appAge.route("/result", methods=['POST'])
def result():
    age = request.form['age']
    if int(age) >= 18:
        return render_template('adult.html')
    else:
        return render_template('minor.html')

if __name__ == '__main__':
    appAge.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/') # this route will handle requests to the root URL "/"
def homePage():
    return ("Welcome to Homepage")

if __name__ == '__main__':
    # app.run(debug=True) # the default port is 5000 in case you want to change the default port
    app.run(port = 2346 ,debug=True)
    # app.run(port = 2346 )

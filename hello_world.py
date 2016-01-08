from flask import Flask, render_template
from os import environ


app = Flask(__name__)

@app.route("/")
@app.route("/hello") 
def say_hi():
    return render_template('hello.html', person = "World")


@app.route("/hello/<name>")
def hi_person(name):
    given=name
    return render_template('hello.html', person = given.title())

@app.route("/hello/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
    first = first_name[0:2]
    last = last_name[0:3]
    jedi = str(last) + str(first)
    return render_template('hello.html', person = "Jedi " + jedi.title())
    
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT'])) 
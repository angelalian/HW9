
from flask import Flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def display():
    
    with open('inspiration.txt') as fp:
        quotes = fp.read().split('\n')
   
    import random
    i = random.randint(0,len(quotes))
    quote = quotes[i]

    return render_template('quote.html' , quotes = quote)


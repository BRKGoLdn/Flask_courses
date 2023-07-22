from flask import Flask

app =  Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my website!"

@app.route('/about')
def about():
    return 'Welcome to my About website page!'


@app.route('/team')
def ekibimiz():
    return ' <h1> Our team is made of 5 people! </h1>'

if __name__ == '__main__':
    app.run(debug=True)

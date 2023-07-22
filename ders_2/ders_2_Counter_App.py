from flask import Flask,render_template,request

app =  Flask(__name__)
sonuc=0
@app.route('/',methods=['GET','POST'])
def index():
    global sonuc
    if request.method == 'POST':
        actions= request.form['action']
        if actions == "-":
            sonuc= sonuc-1
        elif actions == "+":
            sonuc = sonuc+1
    return render_template('counter.html',sonucum=sonuc)

if __name__ == '__main__':
    app.run(debug=True)

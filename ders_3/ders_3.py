from flask import Flask,render_template,request

app =  Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        length= request.form.get('length')
        width =  request.form.get('width')
        if width and length:
            alan= int(width) * int(length)
            cevre= 2*(int(width)+int(length))
            return render_template('cevre_alan.html',alanim=alan,cevrem=cevre)
    return render_template('cevre_alan.html')

if __name__ == '__main__':
    app.run(debug=True)

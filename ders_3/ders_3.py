from flask import Flask,render_template,request

app =  Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        height= request.form.get('height')
        width =  request.form.get('width')
        if width and height:
            alan= int(width) * int(height)
            cevre= (int(width)*2)+(int(height)*2)
            return render_template('cevre_alan.html',alanim=alan,cevrem=cevre)
        else:
            message= 'Lutfen yükseklik veya genişliki boş bırakmayın'
            return render_template('cevre_alan.html', messagim= message)
    return render_template('cevre_alan.html')

if __name__ == '__main__':
    app.run(debug=True)

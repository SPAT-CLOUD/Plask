from flask import Flask,render_template,request
from requests import get
app = Flask(__name__)

@app.route('/')
def Hello():
    return render_template("index.html")

@app.route('/table/<int:num>')
def dhoom(num):
    raq = request.args.get('limit',default=10,type=int)
    x=""
    for i in range(1,raq+1):
        x +=f"{num} x {i} = {num*i}<br/>"
    return x

@app.route('/ran')
def ranImg():
    v=request.args.get('url', default="https://spat-cloud.github.io/data/DORAEMON1.png",type=str)
    return f"<img src=\"{v}\" alt=\"loading\">"


if __name__=="__main__":
    app.run(debug=True)

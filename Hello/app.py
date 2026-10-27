from flask import Flask,render_template,request
from requests import get

#from hashlib import md5

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
    return get(v).content

@app.route('/lh/<value_param:str>')
def LowHash():
    dat=get(f"https://foxyware.pythonanywhere.com/lh?val={value_param}")
    if dat.status_code==200:
        return dat.text
    else:
        return f"<b>ERROR STATUS CODE {dat.status_code}</b>"

"""
@app.route('/md5/<val:str>')
def enc(val):
    c=md5(val.encode('utf-8') if val!=None or val!=' ' else "0".encode('utf-8')) 
    return c.hexdigest()

@app.route('/redir')
def Easy():
    Rurl=request.args.get("rurl", default="https://spat-cloud.github.io/default",type=str)
    guys=f"<script>setTimeout(()=>window.location=\"{Rurl}"\,3000);</script>"
    return guys
"""

if __name__=="__main__":
    app.run(debug=True)

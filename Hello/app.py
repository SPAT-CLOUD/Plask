from flask import Flask,render_template,request
from requests import get
from hashlib import md5
from random import randint as rnum
import json
import os

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

@app.route('/lh/<string:vp>')
def LowHash(vp):
    dat=get(f"https://foxyware.pythonanywhere.com/lh?val={vp}")
    if dat.status_code==200:
        return dat.text
    else:
        return f"<b>ERROR STATUS CODE {dat.status_code}</b>"


@app.route('/md5/<string:val>')
def enc(val):
    c=md5(val.encode('utf-8') if val!=None or val!=' ' else "0".encode('utf-8')) 
    return c.hexdigest()

@app.route('/redir')
def Easy():
    imArr = [
                "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExazZrM3FpZDllNmNudmsxbTJkY3ZjZG0xZTA4bXljdzY4eG9mMGIxciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EgzDbaFXWbNKIV1nRJ/giphy.gif",
                "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWpmdDA0Ymk0Ym1paWs2Njhmc3pkbmZmeTRveHg4N2Z4NnozZTZxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yw165bTss3jylzcY3G/giphy.gif",
                "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGV0dGt0aHRlc2hpdG44ZHRobTdoam82bG9jN252a2R5bjJzbmNuNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Kpr1nwrQGNMw4cECXS/giphy.gif",
                "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGlxbW5hM2tvZXIyNmdtczFoMDd2bXd2ODdmZjhiemViaHZpcjM0ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3p3Udf5339smpSqYav/giphy.gif"
            ]
    paka = imArr[rnum(0,len(imArr)-1)]
    img_s = request.args.get('idx',default=paka)
    Msg = request.args.get('umsg',default='Wait Load Loading...',type=str)
    Rurl=request.args.get("rurl", default="https://spat-cloud.github.io/default",type=str)
    # guys=f"<script>setTimeout(()=>window.location=\"{Rurl}"\,3000);</script>"
    dads = render_template("redir.html",img_src=img_s,msg_char=Msg,url_red=Rurl)
    return dads


@app.route('/dummy')
def checkDumi():
    cpath = os.getcwd()
    spath =  os.path.join(cpath,'user_dump')
    # path_chk = os.path.exists(os.path.join('user_dump','dump.txt'))
    # if path_chk:
    #     return True
    # else:
    #     return False
    return f"CURRENT DIR = {cpath}<br>This path {spath} is {os.path.exists(spath)}"

@app.route('/getconts')
def getWroted():
    cpath =  os.getcwd()
    spath =  os.path.join(cpath,'user_dump','dump.txt')
    if os.path.exists(spath):
        data_read = open(spath,'r')
        data_in_file = data_read.read()
        data_read.close()
        return data_in_file
    else:
        return "Error opening file"

@app.route('/wrote')
def Wrote_file():
    cpath =  os.getcwd()
    spath =  os.path.join(cpath,'user_dump','dump.txt')
    Mdata = request.args.get('insert',default=' ')
    if os.path.exists(spath) and Mdata!=' ':
        fbuf = open(spath,'a')
        fbuf.write(Mdata)
        fbuf.close()
        return "INSERTED DATA SUCKSESS"
    else:
        return "ERROR FILE OR NO DATA INSERTION"



@app.route('/api/love')
def Love():
    return "Double path /api/love bool sucksess<br/><video src=\"https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHlwMWV6dTN0djBzdzUxemlscmFsd28ydjdjc3A1Y25oazlzczU1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oVkTSEl6w9gWB7vhXz/giphy.gif\"  width=\"300\" style=\"aspect-ratio:16/9;\">"

@app.route('/read_ip')
def isp():
    x="https://api.ipify.org/"
    g = get(x,proxies={
        'http':'http://0.0.0.0:5515'
    })
    if g.status_code==200:
        Pars = g.text
        return f"IP Public: {Pars}"
    else:
        return f"ERROR Cauting ip {g.status_code}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5515,debug=True)

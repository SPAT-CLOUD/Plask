from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def Hello():
    return render_template("index.html")

@app.route('/table/<int:num>')
def dhoom(request,num):
    raq = request.args.get('limit',default=10,type=int)
    x=""
    for i in range(1,raq+1):
        x +=f"{num} x {i} = {num*i}<br/>"
    return x
    
if __name__=="__main__":
    app.run(debug=True)

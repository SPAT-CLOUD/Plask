from flask import Flask

app = Flask(__name__)

@app.route('/')
def r1():
  return "Second app"

if __name__=="__main__":
  app.run(debug=True)

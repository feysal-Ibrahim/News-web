from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>NEWS IS COMING,STAY TUNED</h1>"
    
if __name__ =="__main__":
    app.run(debug=True) 
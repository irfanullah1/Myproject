from flask import Flask

app = Flask(__name__)

@app.route('/')
app.run(host = '192.168.1.3',port=5005)

def hello():
    return 'I am Irull from Kandahar '




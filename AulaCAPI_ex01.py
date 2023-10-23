from flask import Flask, json 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello{name}'

@app.route('/status/')
def status():
    return jsonify({"status" : "OK"})

@app.route('/soma/') #mac ('/soma/<int:n1>/<int:n2>')#
def soma(n1, n2):
    return f'a soma de {n1} com {n2} é {n1+n2}'

@app.route('/rev/<float>')
def revision(revNo):
    #return 'revision No %f' %revNo 
    return f'Revision No {revNo}'


#principal
if __name__ == "__main__":
    app.run()
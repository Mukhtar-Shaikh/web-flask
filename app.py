from flask import Flask 

app = Flask (__name__)
@app.route("/")

    
def hello():
    name = 'mukhtar'
    return f"\t\t Hello\t{name} !!!!!!!! "

if __name__ ==('__main__'):
    app.run(host= '0.0.0.0' ,debug=True)



from flask import Flask ,render_template

app = Flask (__name__)

@app.route("/")

def hello():
    work = [
    {
        "id" : 1,
        "role" :"backend",
        "salary" :2400000
    },
    {
        "id" : 2,
        "role" :"front-end",
        "salary" :2000000
    },
    {
        "id" : 1,
        "role" :"ml",
        "salary" :2500000
    }
]
    
    return render_template("index.html", name = "mukhtar".upper(), jobs=work)

if __name__ ==('__main__'):
    app.run(host= '0.0.0.0' ,debug=True)



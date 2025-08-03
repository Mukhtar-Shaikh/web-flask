from flask import Flask ,render_template ,jsonify

app = Flask (__name__)
work = [
    {
        "location" : "pune",
        "role" :"backend",
        "salary" :2400000
    },
    {
        "location" : "pune",
        "role" :"front-end",
        "salary" :2000000
    },
    {
        "location" : "mumbai",
        "role" :"ml engineer ",
        "salary" :2500000
    },
    {
        "location" : "mumbai",
        "role" :"Intern "
        
    }
]

@app.route("/")

def hello():
    
    
    return render_template("index.html", name = "mukhtar".upper(), jobs=work)
@app.route("/api/jobs")
def jobs():
    return jsonify(work)

if __name__ ==('__main__'):
    app.run(host= '0.0.0.0' ,debug=True)



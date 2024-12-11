from flask import Flask

"""data = formate_data()

for d in data:
    d_str=str(d)
    preduce_data(data=d_str)"""
    
    
app=Flask(__name__)

@app.route("/")
def index():
    return("index")


@app.route("/get")
def get():
    pass
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
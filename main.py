from flask import Flask

app = Flask(__name__)

@app.route("/get")
def hello_get():
    return "Hello, orang ganteng (GET)"

@app.route("/post")
def hello_post():
    return "Hello, orang ganteng (POST)"

@app.route("/delete")
def hello_delete():
    return "Hello, orang ganteng (DELETE)"

@app.route("/detail/<nama>")
def hello_detail(nama):
    return f"Halo {nama}, ini halaman detail kamu"

if __name__ == "__main__":
    app.run(debug=True)

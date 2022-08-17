from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Story from an Azure Web App running on Linux! Gorillaz are playing tonight!!!!!! Martinelli na na na na na naaaa ooooh"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

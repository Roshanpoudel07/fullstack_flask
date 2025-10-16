from flask import Flask

app = Flask(__name__, static_url_path='/public', static_folder='public')

@app.get("/")
def index():
    return "Welcome to my REST API!"

@app.get("/api/v1/cat")
def get_cat():
    cat = [{
        "cat_id": "sdhsd",
        "name": "Mittens",
        "birthdate": "20018-03-22",
        "weight": 8,
        "owner": "roshan poudel",
        "image": "https://as1.ftcdn.net/jpg/11/53/96/10/1000_F_1153961096_R8H1DRoFuRSKkhF5OUuLqod4YWxRNNKf.jpg"
    }]
    return cat


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
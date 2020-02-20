from flask import Flask

app = Flask(__name__,
            static_url_path='', 
            static_folder='public')

@app.route("/")
def hello():
    return "Welcome to the visualiser! Navigate to /index.html to view visualisations."

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
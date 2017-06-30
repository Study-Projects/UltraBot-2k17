from flask import Flask

app = Flask(__name__)

@app.route('/')
def webhook():
    return "Hello world"

@app.route('/', methods=['POST'])
def vk_confirmation():
    pass


if __name__ == "__main__":
	app.run(debug=True)

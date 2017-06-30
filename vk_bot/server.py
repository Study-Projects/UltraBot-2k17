from flask import Flask
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def vk_confirmation():
    return 'd30692a9' #replace with os module

@app.route('/', methods=['POST'])
def webhook():
    pass
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

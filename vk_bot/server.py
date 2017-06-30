from flask import Flask
import os
from config import CONFIRMATION_TOKEN

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    return CONFIRMATION_TOKEN


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask
from argparse import ArgumentParser
import os

app = Flask(__name__)

def parse_argv():
    parser = ArgumentParser(description="Starts flask server.")
    parser.add_argument('--host', '-H', type=str, default="0.0.0.0",
                        help="Specify host id.")
    parser.add_argument('--port', '-p', type=int, default=int(os.environ.get('PORT', 5000)),
                        help="Specify local port, where to start server.")
    parser.add_argument('--debug', '-d', type=bool, default=True,
                        help="Start server in debug mode.")
    return parser.parse_args()

@app.route('/')
def webhook():
    return "Hello world"

@app.route('/', methods=['POST'])
def vk_confirmation():
    pass


if __name__ == "__main__":
    args = parse_argv()
    app.run(host=args.host, port=args.port, debug=args.debug)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    app.logger.debug('Logger')
    return 'Hello World!\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8000)  # Start the server

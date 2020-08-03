from flask import Flask

app = Flask(__name__)


print('Stop') # Put breakpoint here

if __name__ == "__main__":
    app.run()
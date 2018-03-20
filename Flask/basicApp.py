from flask import Flask

app = Flask(__name__)

# this routes us to the root directory (the homepage)
@app.route('/')
# ties a url to a python function
def index():
    return 'This is the homepage'

# this is a quick check to only run the server when this is called directly
if __name__ == '__main__':
     # this starts up the application in debugging mode
    app.run(debug=True)

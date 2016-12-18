from flask import Flask
from redis import Redis
from compute import getmass

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def compute():
    result = getmass('https://www.dropbox.com/s/aqrmpoc4tqmlfcg/Train1.zip?dl=1')
    return result
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
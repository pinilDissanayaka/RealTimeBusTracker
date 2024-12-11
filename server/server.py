from flask import Flask, render_template, Response
from kafka import get_checkpoint


app = Flask(__name__)


#Consumer API
@app.route('/')
def get_messages():
    topicname = 'busdatat'

    return Response(get_checkpoint(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
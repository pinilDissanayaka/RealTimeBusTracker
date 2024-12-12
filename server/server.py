"""from flask import Flask, render_template, Response
from kafka import get_checkpoint


app = Flask(__name__)
CORS(app)  



#Consumer API
@app.route('/')
def get_messages():
    topicname = 'busdatat'

    return Response(get_checkpoint(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, port=5001)"""


from flask import Flask, Response
from flask_cors import CORS
import time
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


def generate_events():
    """Generator function to yield Server-Sent Events."""

    dummy_data = [
        {"lat": 79.87848236150131, "lon": 6.930243972119172, "bus_id": "152"},
        {"lat": 79.87954137332076, "lon": 6.930115572168091, "bus_id": "152"},
        {"lat": 79.88125519397391, "lon": 6.930492746924699, "bus_id": "152"},
        {"lat": 79.88261331600137, "lon": 6.930934121255461, "bus_id": "152"},
        {"lat": 79.88383400901483, "lon": 6.931359445220096, "bus_id": "152"},
        {"lat": 79.88448881784979, "lon": 6.931415620055702, "bus_id": "152"},
        {"lat": 79.88620263850288, "lon": 6.932250216808285, "bus_id": "152"},
        {"lat": 79.88665534584499, "lon": 6.932370591217946, "bus_id": "152"},
        {"lat": 79.88886665689455, "lon": 6.932618852805263, "bus_id": "152"},
        {"lat": 79.89033795575722, "lon": 6.932610827849487, "bus_id": "152"},
        {"lat": 79.89206028327771, "lon": 6.932490335960566, "bus_id": "152"},
        {"lat": 79.89352431332611, "lon": 6.932819355530967, "bus_id": "152"},
        {"lat": 79.89392851631061, "lon": 6.932241558633947, "bus_id": "152"},
        {"lat": 79.8945186526679, "lon": 6.931406961864795, "bus_id": "152"},
        {"lat": 79.89480159475715, "lon": 6.930363713825301, "bus_id": "152"},
        {"lat": 79.8948905194136, "lon": 6.92985813894542, "bus_id": "152"},
        {"lat": 79.89496327595123, "lon": 6.9292241633281435, "bus_id": "152"},
        {"lat": 79.89503969180276, "lon": 6.928821740303476, "bus_id": "152"},
        {"lat": 79.89519567316415, "lon": 6.928460434923039, "bus_id": "152"}
    ]



    for i in dummy_data:  # Example: send 5 messages
        json_data = json.dumps(i)
        yield f"data:{json_data}\n\n"
        time.sleep(1)  # Simulate a delay between events

@app.route('/')
def stream():
    """Stream events to the client."""
    return Response(generate_events(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
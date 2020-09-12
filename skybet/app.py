"""
App to get the bets
"""

import json

from flask import Flask, jsonify, request
from rq import Queue
from rq.job import Job

from worker import conn
from tasks import get_bets

q = Queue(connection=conn)

app = Flask(__name__)

@app.route('/')
def index():
    with open(r'bets.json', 'r') as f:
        bets = json.load(f)

    return jsonify(bets)

@app.route('/bets', methods=['POST'])
def bets():
    data = request.json
    period = data.get('period', None)
    job = q.enqueue(
        get_bets,
        data['username'],
        data['pin'],
        period
    )

    return job.id

@app.route('/results/<job_key>', methods=['GET'])
def get_results(job_key):
    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return jsonify(job.result), 200
    else:
        return "Nay!", 202

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

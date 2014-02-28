#!/usr/bin/env python
"""
Simple RESTful service returning json output

  output format: {'name': '',
                  'id': '0',
                  'value': '',
                  'timestamp': YYYY-MM-DD HH:MM:SS }

"""
from flask import Flask, jsonify
from datetime import datetime
import random
import string

rest_app = Flask(__name__)

@rest_app.route('/info')
def index():
    now = datetime.now()
    tstamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Generate random string for value and id#
    v = lambda s: ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(s))
    i = lambda s: ''.join(random.choice(string.digits) for x in range(s))

    json_info = { 'name': 'eric', 'id': i(3), 'value': v(8), 'timestamp': tstamp, }
    return jsonify( json_info )

if __name__ == '__main__':
    rest_app.run(debug = True)

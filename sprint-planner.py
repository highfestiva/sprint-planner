#!/usr/bin/env python3

from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import random
import re


app = Flask(__name__)
date_fixer = re.compile(r'20\d\d-(\d+-\d+) .*')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/x-icon')


@app.route('/plan/<name>')
def plan(name):
    dates = pd.date_range(start='2019-06-17', end='2019-07-30')
    dates = [fixdate(d) for d in dates]
    persons = 'JB J RZ RF IB AA GW ML MO SF HSK'.split()
    data = pd.DataFrame(index=dates, columns=persons)
    data = data.fillna(1.0)
    for p in persons:
        ds = random.sample(dates, 8)
        # for d in ds:
            # data[[d,p]] = 0.0
    print(data)
    return render_template('plan.html', name=name, data=data)


def fixdate(d):
    return date_fixer.sub(r'\1', str(d))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=False)
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
    real_dates = dates = pd.date_range(start='2019-06-17', end='2019-07-30')
    dates = [fixdate(d) for d in dates]
    date_names = []
    prev_month = ''
    for date in dates:
        month,day = date.split('-')
        if month == prev_month:
            date_names += ['<br>'+day]
        else:
            date_names += [month+'<br>'+day]
            prev_month = month
    meta = '_date_names _free'.split()
    persons = 'JB J RZ RF IB AA GW ML MO SF HSK'.split()
    data = pd.DataFrame(index=dates, columns=meta+persons)
    data.loc[:, '_date_names'] = date_names
    data.loc[:, '_free'] = [rd.weekday()>=5 for rd in real_dates]
    data = data.fillna(1.0)
    for p in persons:
        ds = random.sample(dates, 8)
        for d in ds:
            data.loc[d,p] = 0.0
    return render_template('plan.html', name=name, data=data)


def fixdate(d):
    return date_fixer.sub(r'\1', str(d))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=False)

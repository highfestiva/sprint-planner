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
    dates = dates = pd.date_range(start='2019-06-17', end='2019-07-30')
    persons = 'JB J RZ RF IB AA GW'.split()
    table1 = _create_table(dates, persons)
    persons = 'ML MO SF HSK'.split()
    table2 = _create_table(dates, persons)
    persons = ['Sprint\nstart']
    table3 = _create_table(dates, persons)
    return render_template('plan.html', name=name, tables=[('ppl_dates', table1), ('ppl_dates', table2), ('sprint_start_dates', table3)])


def _create_table(real_dates, persons):
    dates = [fixdate(d) for d in real_dates]
    date_names = []
    prev_month = ''
    for date in dates:
        month,day = date.split('-')
        if month == prev_month:
            date_names += ['\n'+day]
        else:
            date_names += [month+'\n'+day]
            prev_month = month
    meta = '_date_names _free'.split()
    data = pd.DataFrame(index=dates, columns=meta+persons)
    data.loc[:, '_date_names'] = date_names
    data.loc[:, '_free'] = [rd.weekday()>=5 for rd in real_dates]
    data = data.fillna(1.0)
    for p in persons:
        ds = random.sample(dates, 8)
        for d in ds:
            data.loc[d,p] = 0.0
    return data


def fixdate(d):
    return date_fixer.sub(r'\1', str(d))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=False)

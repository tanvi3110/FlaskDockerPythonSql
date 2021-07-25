from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response
from flask import render_template
app = Flask(__name__)


def cities_import1() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'citiesData1'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblcitiesImport1')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


@app.route('/')
def index1():
    user = {'username': 'Miguel'}
    cities_data = cities_import1()
    return render_template('index.html', title='Home', user=user, cities=cities_data)


@app.route('/api/cities')
def cities() -> str:
    js = json.dumps(cities_import1())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')

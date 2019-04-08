 # This example uses Python 2.7+ and the python-request library
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import date, timedelta, datetime

def get_date_for_endpoint(date): # DATE to string format YY-mm-dd
    strd = date.strftime("%d/%m/%Y")
    splitd = strd.split('/')
    return splitd[2] + '-' + splitd[1] + '-' + splitd[0]

def get_data(): # GET DATA
    today = date.today()
    data = []
    for i in range(0, 15): # 15 requests
        session = Session()
        parameters = {
           'start': '1',
            'limit': '5000',
            'convert': 'USD',
        }
        url = 'http://api.coinlayer.com/' + get_date_for_endpoint(today - timedelta(days=i * 5)) + '?access_key=227da4735f809c417f000fbb048ddcef&symbols=DASH,ETH,LTC'
        response = session.get(url, params=parameters)
        thej = json.loads(response.text)
        appendie = { #SEPERATE INFORMATION AND PREPARE TO APPEND TO THE LIST
            'date' : get_date_for_endpoint(today - timedelta(days=i * 5)),
            'DASH' : thej['rates']['DASH'],
            'ETH' : thej['rates']['ETH'],
            'LTC' : thej['rates']['LTC']
        }
        data.append(appendie)
    finaldata = []
    x = []
    ey = []
    by = []
    ly = []
    for i in data:
        x.append(i['date'])
        by.append(i['DASH'])
        ey.append(i['ETH'])
        ly.append(i['LTC'])
    finaldata.append({
        'x' : x,
        'y' : by,
        'type':'bar'
    })
    finaldata.append({
        'x' : x,
        'y' : ey,
        'type':'bar'
    })
    finaldata.append({
        'x' : x,
        'y' : ly,
        'type':'bar'
    })
    return json.dumps(finaldata)
    
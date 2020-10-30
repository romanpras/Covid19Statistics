# Roman Prasolov - 313091746

import requests
from flask import Flask, jsonify, request

url = "https://corona.lmao.ninja/v3/covid-19/historical"

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
# newCasesPeak - Returns the date (and value) of the highest peak of new
# Covid-19 cases in the last 30 days for a required country.
@app.route('/newCasesPeak', methods=['GET', 'POST'])
def newCasesPeak():
    # The country in which we are looking for the data
    country_id = request.args.get('country')
    # New url with query of the country and concat last 30 days Parameters
    newUrl = url + '/%s' % country_id + '?lastdays=30'
    x = requests.get(newUrl)
    res = x.json()
    return jsonify(dataFromDic(res, 'cases', country_id, 'newCasesPeak'))


# recoveredPeak - Returns the date (and value) of the highest peak of recovered
# Covid-19 cases in the last 30 days for the required country.
@app.route('/recoveredPeak', methods=['GET', 'POST'])
def recoveredPeak():
    # The country in which we are looking for the data
    country_id = request.args.get('country')
    # New url with query of the country and concat last 30 days Parameters
    newUrl = url + '/%s' % country_id + '?lastdays=30'
    x = requests.get(newUrl)
    res = x.json()
    return jsonify(dataFromDic(res, 'recovered', country_id, 'recoveredPeak'))


# deathsPeak - Returns the date (and value) of the highest peak of death Covid-19
# cases in the last 30 days for a required country.
@app.route('/deathsPeak', methods=['GET', 'POST'])
def deathsPeak():
    # The country in which we are looking for the data
    country_id = request.args.get('country')
    # New url with query of the country and concat last 30 days Parameters
    newUrl = url + '/%s' % country_id + '?lastdays=30'
    x = requests.get(newUrl)
    res = x.json()
    return jsonify(dataFromDic(res, 'deaths', country_id, 'deathsPeak'))


# help function- calc the max value and return of each case the data in json format
def dataFromDic(res, lookingFor, country_id, methodName):
    # error handle
    if 'message' in res.keys():
        return {}
    # intro dictionary
    dic = res['timeline'][lookingFor]
    dic = list(dic.items())
    # Returns the date and value of the highest peak
    maxValue = -1
    for i in range(len(dic)-1):
        if dic[i+1][1] - dic[i][1] > maxValue:
            maxValue = dic[i+1][1] - dic[i][1]
            date = dic[i+1][0]
    return {"country": country_id, "method": methodName, "date": date, "value": maxValue}


# status - Returns a value of success/fail to contact the backend API
@app.route('/status')
def status():
    return jsonify({'status': 'success'})


# 404 error handling
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
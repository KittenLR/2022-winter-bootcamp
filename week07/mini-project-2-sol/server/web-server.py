import pandas as pd
from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)


# -- DO NOT EDIT
# sample end point for HTTP Get
@app.route("/")
def default():
    """
    default endpoint for this server, just for demo.

    :return: str
    """
    return "FIRST PROJECT - we have " + str(len(get_client_rates())) + " clients in total."


# sample data load function
# This is a temporary data file - when we get to know more about database and cloud storage
# we would not be using this kind of data storage.
def get_client_rates():
    """
    return all the client - rate pairs we have.

    :return: dict {id: {'rate':float}}
    """
    import pandas as pd
    df = pd.read_json("client_rate.json")
    return df.to_dict()
# -- DO NOT EDIT END


@app.route("/rate/<client_id>")
def get_client_rate(client_id):
    """
    End point for getting rate for a client_id.

    :param client_id: str
    :return: http response
    """
    rates = get_client_rates()
    if client_id in rates:
        return str(rates[client_id]["rate"])
    return "0"


@app.route("/rate", methods=['POST'])
def upsert_client_rate():
    """
    End point for updating or inserting client rate values in the post param.

    :return: http response.
    """
    param = request.get_json()
    client_id = param['client_id']
    rate = param['rate']

    # update new client
    rates = get_client_rates()
    rates[client_id] = {"rate": rate}
    df = pd.DataFrame.from_dict(rates)
    df.to_json("client_rate.json")
    return request.get_json()


if __name__ == "__main__":
    app.run()

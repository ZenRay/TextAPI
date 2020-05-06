#coding:utf8
"""
API is used to check taboo and corrector words:
* Taboo check:
    Request method is `POST`, URL is `http://<hostname>:<port>/text/api/v1.0/taboo`,
    payload data contains some keys, like `id`, `text`

    Example:
    $ curl -i -H "Content-Type: application/json" -X POST -d  '{"id": 123, "text": "历史学系"}' http://localhost:5000/text/api/v1.0/taboo

        HTTP/1.0 200 OK
        Content-Type: application/json
        Content-Length: 192
        Server: Werkzeug/0.11.15 Python/3.6.10
        Date: Wed, 06 May 2020 08:56:39 GMT

        {
        "cost_time": 0.004797935485839844,
        "description": "it's successfull that check taboo words",
        "id": 123,
        "report": false,
        "status": 200,
        "text": "\u5386\u53f2\u5b66\u7cfb"
        }
* Correct check:
    Request method is `POST`, URL is `http://<hostname>:<port>/text/api/v1.0/correct`,
    payload data contains some keys, like `id`, `text`

    Example:
    $ curl -i -H "Content-Type: application/json" -X POST -d  '{"id": 123, "text": "历史学系"}' http://localhost:5000/text/api/v1.0/correct
        HTTP/1.0 200 OK
        Content-Type: application/json
        Content-Length: 186
        Server: Werkzeug/0.11.15 Python/3.6.10
        Date: Wed, 06 May 2020 08:57:16 GMT

        {
        "cost_time": 0.017215967178344727,
        "description": "it's successfull that check words",
        "id": 123,
        "report": false,
        "status": 200,
        "text": "\u5386\u53f2\u5b66\u7cfb"
        }
"""
from __future__ import absolute_import
import time
from flask import Flask, jsonify, make_response, abort, request

from TextAPI import check_taboo, corrector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Homepage"""
    return "<h1>访问文本处理API</h1>"


@app.route("/text/api/v1.0/taboo", methods=["GET"])
def report_taboo(id_):
    return f"<h1>访问文本处理敏感词检验 API，发送 POST 请求</h1>"


@app.route("/text/api/v1.0/correct", methods=["GET"])
def report_corrector(id_):
    return f"<h1>访问文本处理错误检验 API，发送 POST 请求</h1>"


@app.route("/text/api/v1.0/taboo", methods=["POST"])
def taboo_stamp():
    """Request Taboo Check

    Check taboo
    """
    if not request.json or "text" not in request.json:
        abort(400)
    
    # check taboo
    start_time = time.time()
    taboo = check_taboo.taboo_stamp(request.json["text"])
    end_time = time.time()

    result = {
        "id": request.json["id"],
        "cost_time": end_time - start_time,
        "text": request.json["text"],
        "report": taboo,
        "description": "it's successfull that check taboo words",
        "status": 200
    }

    return jsonify(result), 200



@app.route("/text/api/v1.0/correct", methods=["POST"])
def correct_stamp():
    """Request Correct Check

    Check word correct
    """
    if not request.json or "text" not in request.json:
        abort(400)

    # check correct word
    start_time = time.time()
    correct = corrector.text_corrector(request.json["text"])
    end_time = time.time()

    result = {
        "id": request.json["id"],
        "cost_time": end_time - start_time,
        "text": request.json["text"],
        "report": correct if correct else False,
        "description": "it's successfull that check words",
        "status": 200
    }
    
    return jsonify(result), 200


##################################
### flask customize error handler
####
@app.errorhandler(404)
def not_found(error):
    """Not Found
    Status code 404 response
    """
    return make_response(jsonify(
        {"status": "fail", "description": "Not found"}
    ), 404)


@app.errorhandler(400)
def bad_request(error):
    """Bad Request

    Get wrong parameters, which result in can't parse text information.
    """
    return make_response(jsonify(
        {"status": "fail", "description": "Bad Request"}
    ), 400)


if __name__ == "__main__":
    app.run(debug=True)
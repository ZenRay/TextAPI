#coding:utf8
"""
API is used to check taboo and corrector words
"""
from __future__ import absolute_import
import time
from flask import Flask, jsonify, make_response, abort, request

from TextAPI import check_taboo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Homepage"""
    return "<h1>访问文本处理API</h1>"


@app.route("/text/api/v1.0/taboo/<int:id_>", methods=["GET"])
def report(id_):
    return f"<h1>访问文本处理API，发送 POST 请求</h1>"


@app.route("/text/api/v1.0/taboo", methods=["POST"])
def taboo_stamp():
    """Request Taboo Check

    Check taboo
    """
    if not request.json or "text" not in request.json:
        abort(400)
    
    # check taboo
    start_time = time.time()
    taboo = check_taboo.taboo_stamp(request.json["string"])
    end_time = time.time()

    result = {
        "id": request.json["id"],
        "time": end_time - start_time,
        "text": request.json["string"],
        "report": taboo,
        "description": "it's successfull that check taboo words",
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
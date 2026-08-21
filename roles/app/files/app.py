import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

HOSTNAME = socket.gethostname()
VERSION = os.environ.get("APP_VERSION", "unknown")
HEALTH_FLAG = os.environ.get("APP_HEALTH_FLAG", "/etc/hawp/unhealthy")


@app.route("/")
def index():
    return jsonify(served_by=HOSTNAME, version=VERSION)


@app.route("/version")
def version():
    return VERSION + "\n", 200, {"Content-Type": "text/plain"}


@app.route("/healthz")
def healthz():
    if os.path.exists(HEALTH_FLAG):
        return jsonify(status="unhealthy", served_by=HOSTNAME), 503
    return jsonify(status="ok", served_by=HOSTNAME), 200
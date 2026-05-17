from __future__ import annotations

from flask import Blueprint, Response, abort, render_template, request, redirect, url_for
from api.main import prueba_escaneo

scan_bp = Blueprint("scan", __name__, url_prefix="/scan")

@scan_bp.route("")
def index_page_scan():
    return render_template("index.html")

@scan_bp.route("/run", methods = ["POST","GET"])
def start_scan():
    target = request.form["target"]
    scan_type = request.form["scan_type"]
    timing = request.form["timing"]
    ports = request.form["ports"]
    detect_version = True if request.form.get("detect_version") else False
    scan_vuln = True if request.form.get("scan_vuln") else False
    fragment = True if request.form.get("fragment") else False

    res = prueba_escaneo(target, scan_type, timing, ports, detect_version, scan_vuln, fragment)
    
    return res
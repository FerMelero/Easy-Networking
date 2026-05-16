from __future__ import annotations

from flask import Blueprint, Response, abort, render_template, request, redirect, url_for

scan_bp = Blueprint("scan", __name__, url_prefix="/scan")

@scan_bp.route("")
def index_page_scan():
    return render_template("index.html")
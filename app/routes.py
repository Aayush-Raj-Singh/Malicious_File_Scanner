from flask import Blueprint, render_template, request
import os
from .scanner_logic.malware_scanner import scan_file, get_report, scan_with_hybrid_analysis

main = Blueprint('main', __name__)
logs = ""

def log(msg):
    global logs
    print(msg)
    logs += f"{msg}<br>"

# Inject the logger into the malware scanner
import app.scanner_logic.malware_scanner
app.scanner_logic.malware_scanner.log = log

@main.route('/')
def index():
    global logs
    logs = ""
    return render_template('index.html')

@main.route('/scan', methods=['POST'])
def scan():
    global logs
    logs = ""
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        filepath = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(filepath)

        analysis_id = scan_file(filepath)
        if analysis_id:
            get_report(analysis_id, filepath)
            scan_with_hybrid_analysis(filepath)

    return render_template('index.html', logs=logs)

@main.route('/history')
def history():
    if os.path.exists("scan_history.txt"):
        with open("scan_history.txt", "r") as f:
            history_data = f.read()
    else:
        history_data = "No scan history found."

    return render_template("dashboard.html", history=history_data)
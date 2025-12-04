from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "YOUR_GITHUB_PAT"
REPO = "my-org/remediation"

def dispatch(workflow, run_id):
    url = f"https://api.github.com/repos/{REPO}/actions/workflows/{workflow}/dispatches"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    data = {"ref": "main", "inputs": {"run_id": run_id}}
    return requests.post(url, json=data, headers=headers)

@app.get("/approve")
def approve():
    run_id = request.args.get("run_id")
    dispatch("approval.yml", run_id)
    return "Approved — remediation starting."

@app.get("/skip")
def skip():
    run_id = request.args.get("run_id")
    dispatch("skip.yml", run_id)
    return "Skipped — normal deploy starting."

app.run(host="0.0.0.0", port=8080)


import requests

def send_slack_alert(message):
    webhook_url = "<SLACK_WEBHOOK_URL>"
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

send_slack_alert("Alerta crítico! CPU acima de 90%")

import requests

def send_pagerduty_alert(event_type, summary, source, severity, routing_key):
    
    url = "https://events.pagerduty.com/v2/enqueue"

    payload = {
        "routing_key": routing_key,
        "event_action": event_type,
        "payload": {
            "summary": summary,
            "source": source,
            "severity": severity,
        }
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 202:
        print("PagerDuty alert sent successfully!")
    else:
        print(f"Failed to send alert: {response.status_code} - {response.text}")

if __name__ == "__main__":
    ROUTING_KEY = "your-pagerduty-integration-key"
    send_pagerduty_alert(
        event_type="trigger",
        summary="High CPU usage detected on server-1",
        source="server-1",
        severity="critical",
        routing_key=ROUTING_KEY
    )

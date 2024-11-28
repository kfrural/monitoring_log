import numpy as np

def detect_anomaly(data, threshold=0.9):
    
    mean = np.mean(data)
    if mean > threshold:
        return "Anomaly Detected"
    return "Normal"

data = [0.5, 0.6, 0.95, 0.8]
print(detect_anomaly(data))

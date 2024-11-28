from detection import detect_anomaly

def test_anomaly():
    assert detect_anomaly([0.5, 0.6, 0.7], threshold=0.8) == "Normal"
    assert detect_anomaly([0.9, 0.95, 1.0], threshold=0.8) == "Anomaly Detected"

test_anomaly()
print("All tests passed!")

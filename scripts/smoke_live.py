import requests, sys, json
BASE = "https://docker-gtfsdggubmduhehf.uksouth-01.azurewebsites.net"

def must_ok(r): 
    assert r.status_code == 200, (r.status_code, r.text)
    return r.json()

print("health:", must_ok(requests.get(f"{BASE}/health")))
print("single:", must_ok(requests.post(f"{BASE}/predict", json={"text":"great work"})))
print("batch:", must_ok(requests.post(f"{BASE}/predict_batch", json={"texts":["wow","awful"]})))
print("error:", requests.post(f"{BASE}/predict", json={"text":""}).status_code)  # 422 expected

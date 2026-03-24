import requests

BASE_URL = "http://127.0.0.1:5000"
HEADERS = {"Authorization": "12345"}

def create_interface():
    data = {"name": "Loopback0", "ip": "10.0.0.1"}
    try:
        r = requests.post(BASE_URL + "/interfaces", json=data, headers=HEADERS, timeout=5)
        print("POST interface:", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def get_interfaces():
    r = requests.get(BASE_URL + "/interfaces", headers=HEADERS)
    print("GET interfaces:", r.status_code, r.text)

def update_interface():
    data = {"name": "Loopback0", "ip": "10.0.0.2"}
    r = requests.put(BASE_URL + "/interfaces/0", json=data, headers=HEADERS)
    print("PUT interface:", r.status_code, r.text)

def delete_interface():
    r = requests.delete(BASE_URL + "/interfaces/0", headers=HEADERS)
    print("DELETE interface:", r.status_code, r.text)

# ROUTING

def add_route():
    data = {"network": "192.168.1.0/24", "gateway": "10.0.0.1"}
    r = requests.post(BASE_URL + "/routing", json=data, headers=HEADERS)
    print("POST route:", r.status_code, r.text)

def get_routes():
    r = requests.get(BASE_URL + "/routing", headers=HEADERS)
    print("GET routes:", r.status_code, r.text)


def main():
    create_interface()
    get_interfaces()
    update_interface()
    get_interfaces()
    add_route()
    get_routes()
    delete_interface()
    get_interfaces()


if __name__ == "__main__":
    main()

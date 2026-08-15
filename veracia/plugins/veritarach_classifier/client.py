import requests

DEFAULT_BASE_URL = "https://157-230-241-156.sslip.io"


def predict(text: str, base_url: str = DEFAULT_BASE_URL, timeout: float = 30.0) -> dict:
    response = requests.post(f"{base_url}/predict", json={"text": text}, timeout=timeout)
    response.raise_for_status()
    return response.json()

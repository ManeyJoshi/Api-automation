import pytest
from playwright.sync_api import sync_playwright
import time


@pytest.fixture(scope="session")
def api_context():
    """Create Playwright API request context with base URL"""
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url="https://jsonplaceholder.typicode.com")
        yield request_context
        request_context.dispose()


def test_get_posts(api_context):
    """✅ Test GET /posts request"""
    start_time = time.time()
    response = api_context.get("/posts")
    response_time = time.time() - start_time

    print("\n--- GET /posts Response Headers ---")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    data = response.json()
    print("\n--- GET /posts Response Body (first item) ---")
    print(data[0])

    assert response.status == 200
    assert response_time < 2
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

    required_keys = {"userId": int, "id": int, "title": str, "body": str}
    for key, expected_type in required_keys.items():
        assert key in data[0]
        assert isinstance(data[0][key], expected_type)


def test_post_create(api_context):
    """✅ Test POST /posts request"""
    payload = {
        "userId": 1,
        "title": "Automated test post",
        "body": "This is a test post using Playwright + Pytest."
    }

    start_time = time.time()
    response = api_context.post("/posts", data=payload)
    response_time = time.time() - start_time

    print("\n--- POST /posts Response Headers ---")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    data = response.json()
    print("\n--- POST /posts Response Body ---")
    print(data)

    assert response.status == 201
    assert response_time < 2

    required_keys = {"userId": int, "id": int, "title": str, "body": str}
    for key, expected_type in required_keys.items():
        assert key in data
        assert isinstance(data[key], expected_type)

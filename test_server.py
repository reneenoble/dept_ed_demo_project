"""Tests for the Flask app in server.py.

These tests pass against the existing code so teachers can see what a green
pytest run looks like. They use Flask's built-in test client — no real network
calls, no browser needed.
"""
import pytest

from server import app


@pytest.fixture
def client():
    """A Flask test client — like a fake browser."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ─── Home page ──────────────────────────────────────────────────────

def test_home_page_loads(client):
    """GET / should return a successful response."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_is_html(client):
    """The home page should be served as HTML."""
    response = client.get("/")
    assert "text/html" in response.content_type


# ─── About page ─────────────────────────────────────────────────────

def test_about_page_loads(client):
    """GET /about should return a successful response."""
    response = client.get("/about")
    assert response.status_code == 200


def test_about_page_shows_an_activity(client):
    """The about page picks a random activity and shows it in the HTML."""
    response = client.get("/about")
    body = response.get_data(as_text=True)
    # One of the activities in server.py should appear on the page.
    activities = ["studying", "thinking", "learning", "revision"]
    assert any(word in body for word in activities)


# ─── Unknown routes ─────────────────────────────────────────────────

def test_unknown_route_returns_404(client):
    """Flask should return 404 for a URL that doesn't exist."""
    response = client.get("/this-route-does-not-exist")
    assert response.status_code == 404

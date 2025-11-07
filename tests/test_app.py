"""Integration-style tests exercising the Flask application surface."""

import pytest

from app import app as flask_app


@pytest.fixture
def client():
    """Provide a Flask test client for submitting calculator requests."""

    return flask_app.test_client()


def test_index_successful_addition(client):
    """Posting a valid addition expression should display the computed result."""

    response = client.post('/', data={'display': '2+3'})

    assert response.status_code == 200
    assert 'value="5.0"' in response.data.decode()


def test_index_highlights_subtraction(client):
    """A subtraction expression should display the true difference."""

    response = client.post('/', data={'display': '9-4'})

    assert response.status_code == 200
    assert 'value="5.0"' in response.data.decode()


def test_index_highlights_multiplication(client):
    """Multiplication should return the arithmetic product rather than exponentiation."""

    response = client.post('/', data={'display': '3*2'})

    assert response.status_code == 200
    assert 'value="6.0"' in response.data.decode()


def test_index_highlights_division(client):
    """Division should show true division results instead of flooring."""

    response = client.post('/', data={'display': '5/2'})

    assert response.status_code == 200
    assert 'value="2.5"' in response.data.decode()


def test_index_invalid_expression_shows_error(client):
    """Submitting an invalid expression should surface a helpful error message."""

    response = client.post('/', data={'display': '2++3'})

    assert response.status_code == 200
    assert 'Error: only one operator is allowed' in response.data.decode()


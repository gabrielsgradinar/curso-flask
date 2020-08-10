import pytest

from delivery.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instance of main Flask app"""
    return create_app()

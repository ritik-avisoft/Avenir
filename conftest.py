import pytest

@pytest.fixture
def open_app(page):
    page.goto("https://staging-mf-partners.vercel.app/")
    return page

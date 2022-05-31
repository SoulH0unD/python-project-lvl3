# flake8: noqa
import requests_mock
import os, tempfile
from page_loader.page_loader import download


TMP_DIR = tempfile.gettempdir()


def test_download():
    print(TMP_DIR)
    page_html = """
        <html>
            <body>
                <img src="unavailable.png">
                <img src="available.png">
            <body>
        </html>
    """
    page_url = "http://test.com" 

    with requests_mock.Mocker() as m:
        m.get(page_url, text=page_html)
        assert os.path.join(TMP_DIR,'test-com.html') == download(page_url, TMP_DIR)

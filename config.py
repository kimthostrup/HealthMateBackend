def setup_examples():
    """
    Setup environment to easily run examples.
    API credentials needs to be provided here in order
    to set up api object correctly.
    """
    try:
        import infermedica_api
    except ImportError:
        import sys
        import os

        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        import infermedica_api

    # !!! ENTER YOUR CREDENTIALS HERE !!!
    infermedica_api.configure({
        'app_id': '0e59ae9e',
        'app_key': '65e0fa7cedd4a2a3344b0654b55498f5'
    })

    import logging

    # enable logging of requests and responses
    try:
        import httplib
        httplib.HTTPConnection.debuglevel = 1
    except ImportError:
        import http.client
        http.client.HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def application(environ, start_response):
    data = b"Hello WSGI!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    yield data

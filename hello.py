def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return bytes('\n'.join(a.split('&')), encoding='utf8')

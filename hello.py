def app(environ, start_responce):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = '\r\n'.join(environ['QUERY_STRING'].split('&'))
    start_responce(status, headers)
    return body

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import re

import url_handler

PORT = 9091
GENERATE_SHORT_URL_PATH = "/generateShortUrl"

REQUEST_REG_EXP = re.compile('(\\w+) ([\\w|/]+) HTTP/1.1')
URl_TO_GENERATE_SHORT_URL_FOR_REG_EXP = re.compile('url=(.+)')
STATISTICS_PAGE_REG_EXP = re.compile('/?(\\w+)/stats/?')

url_handler = url_handler.UrlHandler()

def generate_root_response(hostname):
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head />
<body>
<h1>URL shortener</h1>
<form method=post action="http://%s:%s%s">
<table>
<tr>
<th align=right>URL to shorten:</th>
<td><input type=text name="url" size=32 /></td>
</tr>
<tr>
<td><input type=submit value="Submit" /></td>
</tr>
</table>
</form>
</body>
</html>
    """ % (hostname, str(PORT), GENERATE_SHORT_URL_PATH)

    return add_headers(body, 200)

def generate_error_request(method, path):
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head />
<body>
 Method: %s and path: %s not supported!
</body>
</html>
    """ % (method, path)

    return add_headers(body, 400)


def generate_short_url_response(hostname, url_to_generate_short_version_of):
    short_url = "http://%s:%d/%s" % (hostname, PORT, url_handler.generate_and_add_short_url(url_to_generate_short_version_of))
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head />
<body>
 The short URL of  %s is: <a href="%s">%s</a>
</body>
</html>
    """ % (url_to_generate_short_version_of, short_url, short_url)

    return add_headers(body, 200)

def generate_redirect_to(long_url):
    s = "HTTP/1.1 301 Moved Permanently"

    s += "\n"
    s += "Location:http://%s:80/" % long_url
    s += "\n"
    return s

def generate_statistics_page(short_url_to_display_statistics_for):
    long_url = url_handler.get_long_url_for_short_url(short_url_to_display_statistics_for)
    number_of_invokations = url_handler.get_number_of_invocations(short_url_to_display_statistics_for)
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head />
<body>
<h1>URL Shortener Statistics </h1>
Short URL: %s
<br />
Long URL: %s
<br />
Number of invokations: %d
</body>
</html>
    """ % (short_url_to_display_statistics_for, long_url, number_of_invokations)

    return add_headers(body, 200)

def add_headers(body, response_code):
    s = "HTTP/1.1 "
    
    if response_code == 200:
        s += "200 OK"
    elif response_code == 400:
        s += "400 Bad Request"
    else:
        s += "404 Not Found"

    s += "\n"
    s += "Content-Type: text/html"
    s += "\n"
    s += "\n"
    s += body
    return s

def get_url_from_body(body):
    url_to_generate_short_url_for = None
    match = URl_TO_GENERATE_SHORT_URL_FOR_REG_EXP.match(body)
    if match:
        url_to_generate_short_url_for = match.group(1)
    return url_to_generate_short_url_for


def handle_post_request(path, body, hostname):
    if path == GENERATE_SHORT_URL_PATH:
        # SHORT URL GENERATOR REQUEST.
        url_to_create_short_url_for = get_url_from_body(body)
        s = generate_short_url_response(hostname, url_to_create_short_url_for)
    else:
        s = generate_error_request('POST', path)
    return s

def handle_get_request(path, hostname):
    if len(path.strip()) == 0:
        return generate_error_request('GET', '')
        
    if path == "/":
        # START PAGE.
        return generate_root_response(hostname)

    # Remove leading slash, if any.
    if path[0] == '/':
        path = path[1:]
    
    if url_handler.short_url_exists_for(path):
        # SHORT URL INVOKATION.
        url_handler.short_url_invoked(path)
        return  generate_redirect_to(url_handler.get_long_url_for_short_url(path))

    matches_statistics_page = STATISTICS_PAGE_REG_EXP.match(path)
    if matches_statistics_page:
        # SHORT URL STATISTICS.
        short_url_to_display_statistics_for = matches_statistics_page.group(1)
        if url_handler.short_url_exists_for(short_url_to_display_statistics_for):
            return generate_statistics_page(short_url_to_display_statistics_for)
    
    return generate_error_request('GET', path)

    
# MAIN SELECTOR METHOD.
def generate_response(method, path, body, hostname):
    print("Method: %s path: %s" % (method, path))

    if method == "GET":
        s = handle_get_request(path, hostname)
    elif method == "POST":
        s = handle_post_request(path, body, hostname)
    else:
        s = generate_error_request(method, path)
    return s

def extract_body(rest_of_request):
    body = None
    print("extract_body: len(rest_of_request): %d" % len(rest_of_request))
    for (index, line) in enumerate(rest_of_request):
        if len(line.strip()) == 0 and index + 1 < len(rest_of_request):
            body = rest_of_request[index + 1]
            break
    return body

def parse_request(request):
    lines = request.split('\n')
    match = REQUEST_REG_EXP.match(lines[0])
    value_to_return = None
    if match:
        method = match.group(1)
        path = match.group(2)
        body = extract_body(lines[1:])
        value_to_return = (method, path, body)
    else:
        print('The request could not matched!')
    return value_to_return

    
def start_server():
    serversocket = None
    try:
        hostname = socket.gethostname()
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((hostname, PORT))
        serversocket.listen(5)

        while True:
            (client_socket, address) = serversocket.accept()
            print("Connection accepted!")
            received_bytes = client_socket.recv(4096)
            received_message_as_string = received_bytes.decode('utf-8')
            print("RECEIVED REQUEST:")
            print(received_message_as_string)
            parsed_request = parse_request(received_message_as_string)
            if parsed_request != None:
                (method, path, body) = parsed_request
                response = generate_response(method, path, body, hostname)
            else:
                response = generate_error_request("", "")
            print("Will respond with the following:")
            print(response)
            message_as_bytes = response.encode('utf-8')
            client_socket.send(message_as_bytes)
            print("Message sent!")
            client_socket.close()
    finally:
        print('In finally')
        if serversocket != None:
            print('Will close server socket.')
            serversocket.close()
            print('Has closed server socket.')


def main():        
    start_server()

### MAIN ###

if __name__ == '__main__':
    main()

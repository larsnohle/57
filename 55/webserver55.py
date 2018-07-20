#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import re
import urllib.parse

import url_handler

PORT = 9096
SAVE_TEXT_SNIPPET_PATH = "/saveTextSnippet"
SHOW_TEXT_SNIPPET_PATH = "showTextSnippet"
DISPLAY_EDIT_TEXT_SNIPPET_PATH = "displayEditTextSnippet"
EDIT_TEXT_SNIPPET_PATH = "editTextSnippet"
REQUEST_REG_EXP = re.compile('(\\w+) ([\\w|/]+) HTTP/1.1')
TEXT_TO_SAVE_REG_EXP = re.compile('text=(.+)')

SHOW_TEXT_SNIPPET_REG_EXP = re.compile("/showTextSnippet/(\\w+)$")
DISPLAY_EDIT_TEXT_SNIPPET_REG_EXP = re.compile("/displayEditTextSnippet/(\\w+)$")
EDIT_TEXT_SNIPPET_REG_EXP = re.compile("/editTextSnippet/(\\w+)$")

url_handler = url_handler.UrlHandler()

def generate_root_response(hostname):
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"> 
</head>
<body>
<h1>Text snippet saver</h1>
<form method=post action="http://%s:%s%s" accept-charset="utf-8">
<table>
<tr>
<th align=right>Text to save:</th>
<td><input type=text name="text" size=32 /></td>
</tr>
<tr>
<td><input type=submit value="Submit" /></td>
</tr>
</table>
</form>
</body>
</html>
    """ % (hostname, str(PORT), SAVE_TEXT_SNIPPET_PATH)

    return add_headers(body, 200)

def generate_error_request(method, path):
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"> 
</head>
<body>
 Method: %s and path: %s not supported!
</body>
</html>
    """ % (method, path)

    return add_headers(body, 400)


def generate_save_text_response(hostname, text_to_save):
    url = "http://%s:%d/%s/%s" % (hostname, PORT, SHOW_TEXT_SNIPPET_PATH, url_handler.generateAndAddSnippet(text_to_save))
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"> 
</head>
<body>
<h1>Text snippet saver</h1>
 The text has been saved. It can be retrieved at this url: <a href="%s">%s</a>
</body>
</html>
    """ % (url, url)
    return add_headers(body, 200)


def generate_edit_text_response(hostname, url, text):
    url_to_display_text_snippet = "http://%s:%d/%s/%s" % (hostname, PORT, SHOW_TEXT_SNIPPET_PATH, url)
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"> 
</head>
<body>
<h1>Text snippet saver</h1>
 The new text has been saved. It can be retrieved at this url: <a href="%s">%s</a>
</body>
</html>
    """ % (url_to_display_text_snippet, url_to_display_text_snippet)
    return add_headers(body, 200)


def generate_show_snippet(hostname, url, text):
    url_to_display_edit_page = "http://%s:%s/%s/%s" % (hostname, str(PORT), DISPLAY_EDIT_TEXT_SNIPPET_PATH, url)
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"> 
</head>
<body>
<h1>Text snippet saver</h1>
The text is:
<br /> 
<strong>%s</strong>
<br /> 
You can edit it by clicking on this <a href="%s">link</a>
</body>
</html>
    """ % (text, url_to_display_edit_page)
    return add_headers(body, 200)

def generate_display_edit_page_response(hostname, url, text_to_edit):
    body = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"> 
</head>
<body>
<h1>Text snippet saver</h1>
<form method=post action="http://%s:%s/%s/%s">
<table>
<tr>
<th align=right>Text to edit:</th>
<td><input type=text name="text" value="%s" size=32 /></td>
</tr>
<tr>
<td><input type=submit value="Edit" /></td>
</tr>
</table>
</form>
</body>
</html>
    """ % (hostname, str(PORT), EDIT_TEXT_SNIPPET_PATH, url, text_to_edit)

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

def get_text_to_save_from_body(body):
    text_to_save = None
    match = TEXT_TO_SAVE_REG_EXP.match(body)
    if match:
        text_to_save = match.group(1)
        text_to_save = urllib.parse.unquote_plus(text_to_save, "utf-8")
    return text_to_save

def handle_post_request(path, body, hostname):
    if path == SAVE_TEXT_SNIPPET_PATH:
        # SAVE TEXT.
        text_to_save = get_text_to_save_from_body(body)
        return generate_save_text_response(hostname, text_to_save)

    match = EDIT_TEXT_SNIPPET_REG_EXP.match(path)
    if match:
        url = match.group(1)
        if url_handler.snippetExistsForUrl(url):
            text_to_save = get_text_to_save_from_body(body)
            url_handler.setTextForUrl(url, text_to_save)
            return generate_edit_text_response(hostname, url, url_handler.getTextForUrl(url))
    
    return generate_error_request('POST', path)

def handle_get_request(path, hostname):
    if len(path.strip()) == 0:
        return generate_error_request('GET', '')
        
    if path == "/":
        # START PAGE.
        return generate_root_response(hostname)

    match = SHOW_TEXT_SNIPPET_REG_EXP.match(path)
    if match:
        url = match.group(1)
        if url_handler.snippetExistsForUrl(url):
            return  generate_show_snippet(hostname, url, url_handler.getTextForUrl(url))

    match = DISPLAY_EDIT_TEXT_SNIPPET_REG_EXP.match(path)
    if match:
        url = match.group(1)
        if url_handler.snippetExistsForUrl(url):
            return  generate_display_edit_page_response(hostname, url, url_handler.getTextForUrl(url))
        
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
    # m = SHOW_TEXT_SNIPPET_REG_EXP.match('/a')
    # if m:
    #     url_to_edit = m.group(1)
    #     print('Matched! URL to edit: %s' % url_to_edit)
    # else:
    #     print('No match')


    # m = SHOW_TEXT_SNIPPET_REG_EXP.match('/editTextSnippet/a')
    # if m:
    #     url_to_edit = m.group(1)
    #     print('SHOW Matched EDIT!!!! URL to edit: %s' % url_to_edit)
    # else:
    #     print('SHOW Did Not Match EDIT!!!!')
    start_server()
    
        
### MAIN ###

if __name__ == '__main__':
    main()

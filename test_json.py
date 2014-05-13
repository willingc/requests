


# Question 1: How to recognize that {'life': '42'} is json?
# Question 2: models.py - where to handle the conversion of {'life': '42'}
#                         to data that can be used by 'request'
#                         request('post', url, **kwargs)
#
# where possible **kwargs params are:
#     :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
#     :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
#     :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
#     :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
#     :param files: (optional) Dictionary of 'name': file-like-objects (or {'name': ('filename', fileobj)}) for multipart encoding upload.


# ------------------------------------------
# *** requests.post will construct a request
# ------------------------------------------
r = request('post', url, json.dumps(json_dict))

# def request(method, url, **kwargs):
#     """Constructs and sends a :class:`Request <Request>`.
#     Returns :class:`Response <Response>` object.
#
#     :param method: method for the new :class:`Request` object.
#     :param url: URL for the new :class:`Request` object.
#     :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
#     :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
#     :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
#     :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
#     :param files: (optional) Dictionary of 'name': file-like-objects (or {'name': ('filename', fileobj)}) for multipart encoding upload.
#     :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
#     :param timeout: (optional) Float describing the timeout of the request in seconds.
#     :param allow_redirects: (optional) Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.
#     :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
#     :param verify: (optional) if ``True``, the SSL cert will be verified. A CA_BUNDLE path can also be provided.
#     :param stream: (optional) if ``False``, the response content will be immediately downloaded.
#     :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.


# *** data and headers seem tp be the important items for json

def prepare_body(self, data, files):

    # *** data
    json.dumps({'life': '42'})

    # *** header
         # content-length
         # content-type


# ----------------------------------------------
# json for the complement of request -- response
# ----------------------------------------------
def json(self, **kwargs):
        """Returns the json-encoded content of a response, if any.

        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
        """

        if not self.encoding and len(self.content) > 3:
            # No encoding set. JSON RFC 4627 section 3 states we should expect
            # UTF-8, -16 or -32. Detect which one to use; If the detection or
            # decoding fails, fall back to `self.text` (using chardet to make
            # a best guess).
            encoding = guess_json_utf(self.content)
            if encoding is not None:
                try:
                    return json.loads(self.content.decode(encoding), **kwargs)
                except UnicodeDecodeError:
                    # Wrong UTF codec detected; usually because it's not UTF-8
                    # but some other 8-bit codec.  This is an RFC violation,
                    # and the server didn't bother to tell us what codec *was*
                    # used.
                    pass
        return json.loads(self.text, **kwargs)

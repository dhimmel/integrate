import io
import gzip

import requests

def rawgit(handle, repo, commit, *args):
    """Returns url for a raw file in a github reposotory."""
    url_head = 'https://raw.githubusercontent.com'
    return '/'.join((url_head, handle, repo, commit) + args)

def open_gz_url(url):
    response = requests.get(url)
    bytes_io = io.BytesIO(response.content)
    return gzip.open(bytes_io, 'rt')

def obo_iri(identifier):
    return 'http://purl.obolibrary.org/obo/' + identifier.replace(':', '_')

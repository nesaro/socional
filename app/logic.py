PRIVATE=0
TRUSTED=1
PUBLIC=2
PRIVACY_LEVELS={PRIVATE, TRUSTED, PUBLIC}


def local_search(string, privacy_level=PRIVATE):
    """Returns a list of tuples (filename, snippet)
    fzf output
    """
    pass


def trusted_search(string):
    """Search in nodes that we trust
    Returns a list of tuples (host, filename, snippet)
    """
    pass

def public_search(string):
    """Search in nodes that we follow (implied also trust)
    Returns a list of tuples (host, filename, snippet)
    """
    pass


def search_endpoint(string):
    """For a given requester, returns the search result in our own database"""
    documents = local_search(string, privacy_level=PRIVATE)
    return documents


def trusted_search_endpoint(string, requester):
    try:
        requester_key = Trust.objects.get(id=requester)
    except Trust.DoesNotExist():
        return 403
    documents = local_search(string, privacy_level=TRUSTED)
    encrypted_documents = requester_key.encrypt(documents)
    return encrypted_documents

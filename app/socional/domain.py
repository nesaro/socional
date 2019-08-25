PRIVATE=0
TRUSTED=1
PUBLIC=2
PRIVACY_LEVELS={PRIVATE, TRUSTED, PUBLIC}
PRIVACY_LEVEL_CHOICES=(('PRIVATE', PRIVATE),
                       ('TRUSTED', TRUSTED),
                       ('PUBLIC', PUBLIC))

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





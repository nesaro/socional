from django.shortcuts import render

def edit_document(request, document_name):
    pass

def local_search_or_create(request):
    pass

def search_endpoint(string):
    """For a given requester, returns the search result in our own database"""
    documents = local_search(string, privacy_level=PRIVATE)
    return documents

def trusted_search_endpoint(string, requester):
    try:
        requester_key = Trustee.objects.get(uri=requester)
    except Trust.DoesNotExist():
        return 403
    documents = local_search(string, privacy_level=TRUSTED)
    encrypted_documents = requester_key.encrypt(documents)
    return encrypted_documents

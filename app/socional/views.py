from django.shortcuts import render
from .domain import local_search, PRIVATE

def edit_document(request, document_name):
    pass

def local_search_or_create(request):
    pass

def search_endpoint(request):
    """For a given requester, returns the search result in our own database"""
    string = request.GET.get('q')
    documents = []
    if string:
        documents = local_search(string, privacy_level=PRIVATE)
    return render(request, 'socional/search.html', {'documents':documents})

def trusted_search_endpoint(string, requester):
    try:
        requester_key = Trustee.objects.get(uri=requester)
    except Trust.DoesNotExist():
        return 403
    documents = local_search(string, privacy_level=TRUSTED)
    encrypted_documents = requester_key.encrypt(documents)
    return encrypted_documents

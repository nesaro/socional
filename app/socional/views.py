from django.shortcuts import render
from .domain import local_search, PRIVATE
from .models import Document

def edit(request):
    document_name = request.GET.get('name')
    try:
        document = Document.objects.get(name=document_name)
    except Document.DoesNotExist:
        document = None
    if request.method == 'POST':
        content = request.POST['content']
        document, _ = Document.objects.update_or_create(name=document_name,
                                                        defaults={'privacy':PRIVATE,
                                                                  'content':content})
    return render(request, 'socional/edit.html', {'document':document})

def local_search_or_create(request):
    pass


def search_endpoint(request):
    """For a given requester, returns the search result in our own database"""
    string = request.GET.get('q')
    documents = []
    if string:
        documents = local_search(string, privacy_level=PRIVATE)
    else:
        documents = Document.objects.all()
    return render(request, 'socional/search.html', {'query':string,
                                                    'documents':documents})

def trusted_search_endpoint(string, requester):
    try:
        requester_key = Trustee.objects.get(uri=requester)
    except Trust.DoesNotExist():
        return 403
    documents = local_search(string, privacy_level=TRUSTED)
    encrypted_documents = requester_key.encrypt(documents)
    return encrypted_documents

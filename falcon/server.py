import os
import os.path
import falcon

class ListFiles:
    def on_get(self, req, resp):
        """Handles GET requests"""
        content = list(os.listdir('/tmp'))
        resp.media = content


class SearchFiles:
    def on_get(self, req, resp):
        """Handles GET requests"""
        q = req.params.get('q')
        content = list(os.listdir('/tmp'))
        if q:
            content = [x for x in content if q in x]
        resp.media = content

class File:
    def on_get(self, req, resp, filename):
        """Handles GET requests"""
        q = req.params.get('q')
        full_path = os.path.join('/tmp/', filename)
        with open(full_path) as f:
            content = f.read()
        resp.media = content

class Network:
    def on_get(self, req, resp):
        """Handles GET requests"""
        content = ['list', 'of', 'urls', 'of', 'friend', 'servers']
        resp.media = content

    def on_post(self, req, resp):
        #add a new friend
        pass

class Friend:
    def on_get(self, req, resp):
        """Return information about a single server"""
        #This information includes score for that server
        # score can be negative as less important or don't show
        resp.media = content

class SearchNetwork:
    def on_get(self, req, resp):
        """Search the network to find results"""
        q = req.params.get('q')
        depth = req.params.get('depth', 2)
        


api = falcon.API()
api.add_route('/', ListFiles())
api.add_route('/q', SearchFiles())
api.add_route('/content/{filename}', File())
